# godCode sync

The site on GitHub Pages keeps progress in the browser. This small service, run on your
own server, adds accounts: every browser signed in to the same account shares one copy
of the completed items, XP, streak days, and code. Visitors create their own accounts
from the site, and each account sees only its own data.

- `server.py` is the whole service: Python standard library and one SQLite file.
- `test_server.py` checks it end to end: `python3 web/sync/test_server.py`
- The site talks to it from `web/site/sync.js`. Signed out, the site never contacts it.

## What it needs

**HTTPS.** The site is served over HTTPS, and browsers refuse to let it call a plain
   HTTP address. Something in front of the service has to provide a certificate.

## Accounts

Anyone can create an account from the site's dashboard (username and a password of 8 or
more characters). Passwords are stored only as salted scrypt hashes. There is no email
and so no self-service password reset. Limits that keep a public service safe on a small
box: 5 new accounts per address per hour, 500 accounts in total (`SYNC_MAX_USERS`), about
3 MB of data per account, and a lockout after 5 wrong passwords. Set `SYNC_SIGNUP=off` to
stop new sign-ups.

Admin commands, run on the server:

```bash
sudo docker compose exec sync python server.py users
sudo docker compose exec sync python server.py adduser NAME    # create, or reset a password
sudo docker compose exec sync python server.py deluser NAME
```

## Setup with Docker and a Cloudflare Tunnel

This is the setup for a box that already runs a tunnel (`cloudflared`) in Docker. Nothing
is opened in the firewall.

```bash
scp -r web/sync ubuntu@YOUR_VPS:/opt/godcode-sync
```

```bash
ssh ubuntu@YOUR_VPS
cd /opt/godcode-sync
sudo docker compose up -d --build
sudo docker compose exec sync python server.py adduser YOURNAME
```

`adduser` is optional, since people can sign up from the site. Running it for an
existing name resets that password and signs every device out.

Then, in the Cloudflare Zero Trust dashboard, open the tunnel, add a **public hostname**
(for example `godcode-sync.yourdomain.com`), and point it at `http://godcode-sync:8787`.

`TUNNEL_NETWORK` in the compose file names the Docker network the tunnel container is on
(default `deploy_default`). `SYNC_ORIGINS` lists the sites allowed to call the service
(default `https://gautamstar.github.io`).

## Setup without Docker

Any reverse proxy that gives you HTTPS works. With Caddy and a hostname that points at
the server, the whole proxy config is:

```
sync.example.com {
    reverse_proxy 127.0.0.1:8787
}
```

Run the service with `python3 server.py serve` under systemd (it listens on
`127.0.0.1:8787` by default) and open ports 80 and 443.

## Using it

On the site's dashboard choose **Create account** once, then **Sign in** in every other
browser you use. The browser keeps a random session token, never the password. The server
address is prefilled (`DEFAULT_URL` in `web/site/sync.js`) and can be changed under
"Server" in the dialog.

## How devices are reconciled

Every sync sends the browser's whole progress document and gets the merged one back.

| Data | Rule |
|---|---|
| Completed items | once done on any device, done everywhere; earliest completion kept |
| Streak days, peeked solutions | union |
| Code per item | the most recently edited version wins |
| XP | recomputed from the completed items |

Reset on the dashboard erases progress on the server too. The server then raises an
epoch number, and a device still holding older data has it replaced on its next sync
instead of bringing the old progress back.

## Backup

Everything is in one SQLite file, in the `data` volume:

```bash
sudo docker compose exec sync python -c "import sqlite3; sqlite3.connect('/data/godcode-sync.db').backup(sqlite3.connect('/data/backup.db'))"
```

The dashboard's Export button also still works as a per-browser backup.
