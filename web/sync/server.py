#!/usr/bin/env python3
"""godCode sync service. One file, standard library only, Python 3.8+.

Stores each user's progress (completed items, streak days, saved code) in a
SQLite file so the site shows the same progress on every device.

    python3 server.py serve            run the service
    python3 server.py adduser NAME     create a user or reset their password
    python3 server.py users            list users
    python3 server.py deluser NAME     delete a user and their progress

People can also create their own account from the site (POST /signup).

Settings, all optional environment variables:

    SYNC_DB       path to the SQLite file        (default ./godcode-sync.db)
    SYNC_HOST     address to listen on           (default 127.0.0.1)
    SYNC_PORT     port to listen on              (default 8787)
    SYNC_ORIGINS  comma separated site origins allowed to call the service
                  (default https://gautamstar.github.io)
    SYNC_SIGNUP   "off" stops new accounts being created from the site
    SYNC_MAX_USERS  most accounts the service will hold (default 500)

It listens on localhost by default and speaks plain HTTP. Put it behind a
reverse proxy that terminates HTTPS (see README.md); browsers will not let an
HTTPS page talk to a plain HTTP service.

HOW MERGING WORKS
Devices never overwrite each other. Every sync sends the device's whole
document and the server merges it into what it has:

  - a completed item stays completed (the earliest completion time is kept)
  - streak days and "peeked at the solution" marks are unioned
  - for code, the most recently edited version of each item wins

The one thing a merge cannot express is a deliberate reset, so the document
carries an epoch number. Reset bumps the epoch on the server, and anything a
device sends with an older epoch is ignored and replaced.
"""
import getpass
import hashlib
import hmac
import json
import os
import re
import secrets
import sqlite3
import sys
import threading
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

DB_PATH = os.environ.get("SYNC_DB", "godcode-sync.db")
HOST = os.environ.get("SYNC_HOST", "127.0.0.1")
PORT = int(os.environ.get("SYNC_PORT", "8787"))
ORIGINS = [o.strip().rstrip("/") for o in
           os.environ.get("SYNC_ORIGINS", "https://gautamstar.github.io").split(",") if o.strip()]

SIGNUP = os.environ.get("SYNC_SIGNUP", "on").lower() != "off"
MAX_USERS = int(os.environ.get("SYNC_MAX_USERS", "500"))

MAX_BODY = 2 * 1024 * 1024      # a full document is a few hundred KB at most
MAX_DOC = 3 * 1024 * 1024       # most the service stores for one user
MAX_ITEMS = 2000
MAX_CODE = 50000                # characters of code per item
MAX_FAILS = 5                   # failed logins per address before a lockout
LOCKOUT = 300                   # seconds
MAX_SIGNUPS = 5                 # new accounts per address per hour
MIN_PASSWORD = 8
NAME_RE = re.compile(r"^[a-z0-9][a-z0-9_-]{2,31}$")

_db_lock = threading.Lock()
_fails = {}                     # address -> (count, first_failure_time)
_signups = {}                   # address -> (count, first_signup_time)


def db():
    con = sqlite3.connect(DB_PATH, timeout=10)
    con.execute("PRAGMA journal_mode=WAL")
    con.execute("CREATE TABLE IF NOT EXISTS users ("
                "name TEXT PRIMARY KEY, salt BLOB, hash BLOB, doc TEXT, updated REAL)")
    con.execute("CREATE TABLE IF NOT EXISTS sessions ("
                "token_hash TEXT PRIMARY KEY, name TEXT, created REAL)")
    return con


def hash_password(password, salt):
    return hashlib.scrypt(password.encode("utf-8"), salt=salt, n=2 ** 14, r=8, p=1, dklen=32)


def set_password(name, password):
    salt = secrets.token_bytes(16)
    with _db_lock, db() as con:
        con.execute(
            "INSERT INTO users (name, salt, hash, doc, updated) VALUES (?, ?, ?, NULL, ?) "
            "ON CONFLICT(name) DO UPDATE SET salt = excluded.salt, hash = excluded.hash",
            (name, salt, hash_password(password, salt), time.time()))
        # changing the password signs every device out
        con.execute("DELETE FROM sessions WHERE name = ?", (name,))


def create_user(name, password):
    """Create a new account. Returns "ok", "taken" or "full"."""
    salt = secrets.token_bytes(16)
    digest = hash_password(password, salt)
    with _db_lock, db() as con:
        if con.execute("SELECT 1 FROM users WHERE name = ?", (name,)).fetchone():
            return "taken"
        if con.execute("SELECT COUNT(*) FROM users").fetchone()[0] >= MAX_USERS:
            return "full"
        con.execute("INSERT INTO users (name, salt, hash, doc, updated) VALUES (?, ?, ?, NULL, ?)",
                    (name, salt, digest, time.time()))
    return "ok"


def delete_user(name):
    with _db_lock, db() as con:
        con.execute("DELETE FROM sessions WHERE name = ?", (name,))
        return con.execute("DELETE FROM users WHERE name = ?", (name,)).rowcount > 0


def check_password(name, password):
    with _db_lock, db() as con:
        row = con.execute("SELECT salt, hash FROM users WHERE name = ?", (name,)).fetchone()
    if row is None:
        # spend the same time as a real check so user names cannot be probed
        hash_password(password, b"0" * 16)
        return False
    return hmac.compare_digest(hash_password(password, row[0]), row[1])


def token_hash(token):
    return hashlib.sha256(token.encode("utf-8")).hexdigest()


def new_session(name):
    token = secrets.token_urlsafe(32)
    with _db_lock, db() as con:
        con.execute("INSERT INTO sessions VALUES (?, ?, ?)", (token_hash(token), name, time.time()))
    return token


def session_user(token):
    with _db_lock, db() as con:
        row = con.execute("SELECT name FROM sessions WHERE token_hash = ?",
                          (token_hash(token),)).fetchone()
    return row[0] if row else None


def end_session(token):
    with _db_lock, db() as con:
        con.execute("DELETE FROM sessions WHERE token_hash = ?", (token_hash(token),))


# ------------------------------------------------------------------ documents
def empty_doc(epoch=0):
    return {"epoch": epoch, "state": {"done": {}, "peeked": {}, "days": []}, "code": {}}


def clean(doc):
    """Keep only well-formed parts of a document a device sent."""
    out = empty_doc()
    if not isinstance(doc, dict):
        return out
    if isinstance(doc.get("epoch"), int) and doc["epoch"] >= 0:
        out["epoch"] = doc["epoch"]
    state = doc.get("state") if isinstance(doc.get("state"), dict) else {}

    done = state.get("done") if isinstance(state.get("done"), dict) else {}
    for key, val in list(done.items())[:MAX_ITEMS]:
        if (isinstance(key, str) and len(key) <= 200 and isinstance(val, dict)
                and isinstance(val.get("at"), (int, float))
                and isinstance(val.get("xp"), int) and 0 <= val["xp"] <= 1000):
            out["state"]["done"][key] = {"at": val["at"], "xp": val["xp"]}

    peeked = state.get("peeked") if isinstance(state.get("peeked"), dict) else {}
    for key in list(peeked)[:MAX_ITEMS]:
        if isinstance(key, str) and len(key) <= 200 and peeked[key]:
            out["state"]["peeked"][key] = True

    days = state.get("days") if isinstance(state.get("days"), list) else []
    out["state"]["days"] = sorted({d for d in days[:MAX_ITEMS]
                                   if isinstance(d, str) and len(d) == 10})

    code = doc.get("code") if isinstance(doc.get("code"), dict) else {}
    for key, val in list(code.items())[:MAX_ITEMS]:
        if (isinstance(key, str) and len(key) <= 200 and isinstance(val, dict)
                and isinstance(val.get("v"), str) and len(val["v"]) <= MAX_CODE
                and isinstance(val.get("t"), (int, float))):
            out["code"][key] = {"v": val["v"], "t": val["t"]}
    return out


def merge(stored, incoming):
    """Merge a device's document into the stored one. Order does not matter."""
    if incoming["epoch"] < stored["epoch"]:
        return stored                      # the device predates a reset
    out = empty_doc(stored["epoch"])

    done = dict(stored["state"]["done"])
    for key, val in incoming["state"]["done"].items():
        if key not in done or val["at"] < done[key]["at"]:
            done[key] = val
    out["state"]["done"] = done

    out["state"]["peeked"] = dict(stored["state"]["peeked"], **incoming["state"]["peeked"])
    out["state"]["days"] = sorted(set(stored["state"]["days"]) | set(incoming["state"]["days"]))

    code = dict(stored["code"])
    for key, val in incoming["code"].items():
        if key not in code or val["t"] > code[key]["t"]:
            code[key] = val
    out["code"] = code
    return out


def load_doc(con, name):
    row = con.execute("SELECT doc FROM users WHERE name = ?", (name,)).fetchone()
    if row is None or row[0] is None:
        return empty_doc()
    return clean(json.loads(row[0]))


def save_doc(con, name, doc):
    con.execute("UPDATE users SET doc = ?, updated = ? WHERE name = ?",
                (json.dumps(doc, separators=(",", ":")), time.time(), name))


def sync(name, incoming):
    with _db_lock, db() as con:
        merged = merge(load_doc(con, name), clean(incoming))
        if len(json.dumps(merged, separators=(",", ":"))) > MAX_DOC:
            return None                    # over the per-user allowance: store nothing
        save_doc(con, name, merged)
    return merged


def reset(name):
    with _db_lock, db() as con:
        doc = empty_doc(load_doc(con, name)["epoch"] + 1)
        save_doc(con, name, doc)
    return doc


def current_epoch(name):
    with _db_lock, db() as con:
        return load_doc(con, name)["epoch"]


# ------------------------------------------------------------------ http
class Handler(BaseHTTPRequestHandler):
    server_version = "godcode-sync"
    protocol_version = "HTTP/1.1"

    def log_message(self, fmt, *args):
        sys.stderr.write("%s %s\n" % (self.client(), fmt % args))

    def client(self):
        # behind a reverse proxy the real address arrives in this header
        fwd = self.headers.get("X-Forwarded-For")
        return fwd.split(",")[0].strip() if fwd else self.client_address[0]

    def reply(self, status, body=None):
        data = json.dumps(body if body is not None else {}).encode("utf-8")
        self.send_response(status)
        origin = (self.headers.get("Origin") or "").rstrip("/")
        if origin in ORIGINS:
            self.send_header("Access-Control-Allow-Origin", origin)
            self.send_header("Vary", "Origin")
            self.send_header("Access-Control-Allow-Headers", "Authorization, Content-Type")
            self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
            self.send_header("Access-Control-Max-Age", "86400")
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(data)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(data)

    def body(self):
        """Read the request body. It is always read in full, even when the
        request will be refused: browsers reuse connections, and bytes left
        unread would be parsed as the start of the next request."""
        try:
            length = int(self.headers.get("Content-Length") or 0)
        except ValueError:
            length = -1
        if length < 0 or length > MAX_BODY:
            self.close_connection = True      # cannot drain it, so drop the connection
            return None
        raw = self.rfile.read(length) if length else b""
        try:
            data = json.loads(raw.decode("utf-8"))
        except (ValueError, UnicodeDecodeError):
            return None
        return data if isinstance(data, dict) else None

    def user(self):
        auth = self.headers.get("Authorization") or ""
        if not auth.startswith("Bearer "):
            return None, None
        token = auth[7:].strip()
        return session_user(token), token

    def do_OPTIONS(self):
        self.reply(204)

    def do_GET(self):
        if self.path == "/health":
            return self.reply(200, {"ok": True})
        self.reply(404, {"error": "Not found"})

    def do_POST(self):
        data = self.body()
        if self.path == "/login":
            return self.login(data or {})
        if self.path == "/signup":
            return self.signup(data or {})
        name, token = self.user()
        if name is None:
            return self.reply(401, {"error": "Sign in again."})
        if self.path == "/sync":
            if data is None:
                return self.reply(400, {"error": "Bad request."})
            doc = sync(name, data.get("doc"))
            if doc is None:
                return self.reply(413, {"error": "This account is holding too much data."})
            return self.reply(200, {"doc": doc})
        if self.path == "/reset":
            return self.reply(200, {"doc": reset(name)})
        if self.path == "/logout":
            end_session(token)
            return self.reply(200, {"ok": True})
        self.reply(404, {"error": "Not found"})

    def login(self, data):
        who = self.client()
        count, since = _fails.get(who, (0, 0))
        if count >= MAX_FAILS and time.time() - since < LOCKOUT:
            return self.reply(429, {"error": "Too many attempts. Wait five minutes."})
        name, password = data.get("username"), data.get("password")
        if isinstance(name, str):
            name = name.strip().lower()
        if (isinstance(name, str) and isinstance(password, str) and len(password) <= 500
                and check_password(name, password)):
            _fails.pop(who, None)
            return self.reply(200, {"token": new_session(name), "epoch": current_epoch(name)})
        if time.time() - since >= LOCKOUT:
            count, since = 0, time.time()
        if len(_fails) > 20000:
            _fails.clear()
        _fails[who] = (count + 1, since or time.time())
        self.reply(401, {"error": "Wrong username or password."})

    def signup(self, data):
        if not SIGNUP:
            return self.reply(403, {"error": "New accounts are closed on this server."})
        who = self.client()
        count, since = _signups.get(who, (0, 0))
        if time.time() - since >= 3600:
            count, since = 0, time.time()
        if count >= MAX_SIGNUPS:
            return self.reply(429, {"error": "Too many new accounts from this network. Try again in an hour."})
        name, password = data.get("username"), data.get("password")
        name = name.strip().lower() if isinstance(name, str) else ""
        if not NAME_RE.match(name):
            return self.reply(400, {"error": "Usernames are 3 to 32 characters: letters, digits, - and _."})
        if not isinstance(password, str) or not MIN_PASSWORD <= len(password) <= 500:
            return self.reply(400, {"error": "Use a password of at least %d characters." % MIN_PASSWORD})
        result = create_user(name, password)
        if result == "taken":
            return self.reply(409, {"error": "That username is taken."})
        if result == "full":
            return self.reply(403, {"error": "This server is not taking new accounts right now."})
        if len(_signups) > 20000:
            _signups.clear()
        _signups[who] = (count + 1, since)
        self.reply(200, {"token": new_session(name), "epoch": 0})


def main():
    args = sys.argv[1:]
    if len(args) == 2 and args[0] == "adduser":
        name = args[1].strip().lower()
        if not NAME_RE.match(name):
            raise SystemExit("Usernames are 3 to 32 characters: letters, digits, - and _.")
        first = getpass.getpass("Password for %s: " % name)
        if len(first) < MIN_PASSWORD:
            raise SystemExit("Use at least %d characters." % MIN_PASSWORD)
        if first != getpass.getpass("Again: "):
            raise SystemExit("The two entries did not match.")
        set_password(name, first)
        print("Saved. Any device signed in as %s has been signed out." % name)
    elif args == ["users"]:
        with db() as con:
            for name, doc, updated in con.execute("SELECT name, doc, updated FROM users ORDER BY name"):
                done = len(json.loads(doc)["state"]["done"]) if doc else 0
                print("%-32s %4d done   last change %s"
                      % (name, done, time.strftime("%Y-%m-%d", time.localtime(updated))))
    elif len(args) == 2 and args[0] == "deluser":
        print("Deleted." if delete_user(args[1].strip().lower()) else "No such user.")
    elif args == ["serve"]:
        db().close()
        print("godcode-sync on http://%s:%d  db=%s  origins=%s"
              % (HOST, PORT, DB_PATH, ", ".join(ORIGINS)), flush=True)
        ThreadingHTTPServer((HOST, PORT), Handler).serve_forever()
    else:
        raise SystemExit(__doc__)


if __name__ == "__main__":
    main()
