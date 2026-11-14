"""End to end check of the sync service against a throwaway database.

    python3 web/sync/test_server.py
"""
import http.client
import json
import os
import sys
import tempfile
import threading
import urllib.error
import urllib.request
from http.server import ThreadingHTTPServer

tmp = tempfile.mkdtemp()
os.environ["SYNC_DB"] = os.path.join(tmp, "test.db")
os.environ["SYNC_ORIGINS"] = "https://site.example"
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import server  # noqa: E402

httpd = ThreadingHTTPServer(("127.0.0.1", 0), server.Handler)
threading.Thread(target=httpd.serve_forever, daemon=True).start()
BASE = "http://127.0.0.1:%d" % httpd.server_address[1]
checks = []


def call(path, body=None, token=None, origin="https://site.example", method=None):
    req = urllib.request.Request(BASE + path, method=method or ("POST" if body is not None else "GET"))
    data = None
    if body is not None:
        data = json.dumps(body).encode()
        req.add_header("Content-Type", "application/json")
    if token:
        req.add_header("Authorization", "Bearer " + token)
    if origin:
        req.add_header("Origin", origin)
    try:
        with urllib.request.urlopen(req, data) as r:
            return r.status, json.loads(r.read() or b"{}"), r.headers
    except urllib.error.HTTPError as e:
        return e.code, json.loads(e.read() or b"{}"), e.headers


def check(name, ok):
    checks.append(ok)
    print(("PASS  " if ok else "FAIL  ") + name)


def doc(done=None, days=None, code=None, peeked=None, epoch=0):
    return {"epoch": epoch, "state": {"done": done or {}, "peeked": peeked or {}, "days": days or []},
            "code": code or {}}


server.set_password("gautam", "correct horse battery")

s, b, h = call("/health")
check("health responds", s == 200 and b == {"ok": True})
check("allowed origin gets a CORS header", h.get("Access-Control-Allow-Origin") == "https://site.example")
s, b, h = call("/health", origin="https://evil.example")
check("other origins get no CORS header", h.get("Access-Control-Allow-Origin") is None)

s, b, _ = call("/login", {"username": "gautam", "password": "wrong"})
check("wrong password is refused", s == 401)
s, b, _ = call("/login", {"username": "nobody", "password": "correct horse battery"})
check("unknown user is refused", s == 401)
s, b, _ = call("/sync", {"doc": doc()})
check("sync without a token is refused", s == 401)
s, b, _ = call("/sync", {"doc": doc()}, token="made-up")
check("sync with a made-up token is refused", s == 401)

s, b, _ = call("/login", {"username": "gautam", "password": "correct horse battery"})
laptop = b.get("token")
check("right password signs in", s == 200 and bool(laptop) and b.get("epoch") == 0)
s, b, _ = call("/login", {"username": "gautam", "password": "correct horse battery"})
phone = b["token"]

# laptop finishes drill a and writes code; phone finishes drill b later
s, b, _ = call("/sync", {"doc": doc(done={"a": {"at": 100, "xp": 10}}, days=["2026-11-14"],
                                    code={"a": {"v": "laptop v1", "t": 100}})}, laptop)
check("first sync stores the document", s == 200 and "a" in b["doc"]["state"]["done"])
s, b, _ = call("/sync", {"doc": doc(done={"b": {"at": 200, "xp": 30}}, days=["2026-11-15"],
                                    peeked={"b": True}, code={"a": {"v": "phone old", "t": 50}})}, phone)
d = b["doc"]
check("progress from both devices is kept", set(d["state"]["done"]) == {"a", "b"})
check("streak days are unioned", d["state"]["days"] == ["2026-11-14", "2026-11-15"])
check("peeked marks are kept", d["state"]["peeked"] == {"b": True})
check("older code does not overwrite newer code", d["code"]["a"]["v"] == "laptop v1")
s, b, _ = call("/sync", {"doc": doc(code={"a": {"v": "phone new", "t": 300}})}, phone)
check("newer code wins", b["doc"]["code"]["a"]["v"] == "phone new")
s, b, _ = call("/sync", {"doc": doc(done={"a": {"at": 999, "xp": 5}})}, laptop)
check("earliest completion is kept", b["doc"]["state"]["done"]["a"] == {"at": 100, "xp": 10})
s, b, _ = call("/sync", {"doc": doc()}, laptop)
check("an empty device document removes nothing", set(b["doc"]["state"]["done"]) == {"a", "b"})

s, b, _ = call("/sync", {"doc": {"state": {"done": {"x": "junk", "y": {"at": "no", "xp": 1}}},
                                 "code": {"z": {"v": 5, "t": 1}}}}, laptop)
check("malformed entries are dropped", set(b["doc"]["state"]["done"]) == {"a", "b"} and "z" not in b["doc"]["code"])
s, b, _ = call("/sync", {"nope": 1}, laptop)
check("a missing document is harmless", s == 200 and set(b["doc"]["state"]["done"]) == {"a", "b"})

s, b, _ = call("/reset", {}, laptop)
check("reset empties the document and bumps the epoch", b["doc"]["epoch"] == 1 and not b["doc"]["state"]["done"])
s, b, _ = call("/sync", {"doc": doc(done={"b": {"at": 200, "xp": 30}}, epoch=0)}, phone)
check("a device from before the reset cannot bring data back", not b["doc"]["state"]["done"] and b["doc"]["epoch"] == 1)
s, b, _ = call("/sync", {"doc": doc(done={"c": {"at": 400, "xp": 10}}, epoch=1)}, phone)
check("after adopting the new epoch, syncing works again", set(b["doc"]["state"]["done"]) == {"c"})

# a browser sends many requests down one connection; none may disturb the next
conn = http.client.HTTPConnection("127.0.0.1", httpd.server_address[1])
codes = []
for path, token in [("/sync", "made-up"), ("/reset", phone), ("/nowhere", phone), ("/sync", phone)]:
    conn.request("POST", path, json.dumps({"doc": doc(epoch=2)}),
                 {"Content-Type": "application/json", "Authorization": "Bearer " + token})
    r = conn.getresponse()
    r.read()
    codes.append(r.status)
conn.close()
check("requests sharing one connection do not corrupt each other", codes == [401, 200, 404, 200])

s, b, _ = call("/logout", {}, phone)
s, b, _ = call("/sync", {"doc": doc()}, phone)
check("a signed-out token stops working", s == 401)
server.set_password("gautam", "a brand new password")
s, b, _ = call("/sync", {"doc": doc()}, laptop)
check("changing the password signs every device out", s == 401)

for _ in range(server.MAX_FAILS):
    call("/login", {"username": "gautam", "password": "guess"})
s, b, _ = call("/login", {"username": "gautam", "password": "a brand new password"})
check("repeated wrong passwords lock the address out", s == 429)

raw = open(os.environ["SYNC_DB"], "rb").read()
check("no password is stored in plain text", b"a brand new password" not in raw and b"correct horse" not in raw)

print("\n%d/%d passed" % (sum(checks), len(checks)))
sys.exit(0 if all(checks) else 1)
