// Optional progress sync with a self-hosted server (see web/sync/README.md).
// Signed out, nothing here runs and the site stays purely local. Signed in,
// the whole progress document is sent after each change and the merged result
// comes back, so devices add to each other and never overwrite.
const Sync = (() => {
  const CFG = "godcode:sync"; // { url, user, token, epoch, last }
  const STATE = "godcode:v1";
  const CODE = "godcode:code:";
  const STAMPS = "godcode:stamps"; // itemId -> time the code was last edited
  // Prefilled in the sign-in form. The password is never stored anywhere.
  const DEFAULT_URL = "";

  const read = (k, fallback) => {
    try {
      return JSON.parse(localStorage.getItem(k)) || fallback;
    } catch (e) {
      return fallback;
    }
  };
  const write = (k, v) => {
    try {
      localStorage.setItem(k, JSON.stringify(v));
    } catch (e) {}
  };
  const cfg = () => read(CFG, {});
  const setCfg = (patch) => write(CFG, Object.assign(cfg(), patch));

  let status = { kind: "idle", msg: "" };
  const statusFns = [];
  const appliedFns = [];
  function setStatus(kind, msg) {
    status = { kind, msg: msg || "" };
    statusFns.forEach((f) => f(status));
  }

  // ------------------------------------------------------------ documents
  const blankState = () => ({ done: {}, peeked: {}, days: [] });
  function localState() {
    const s = read(STATE, {});
    return { done: s.done || {}, peeked: s.peeked || {}, days: s.days || [] };
  }
  function codeKeys() {
    const keys = [];
    for (let i = 0; i < localStorage.length; i++) {
      const k = localStorage.key(i);
      if (k && k.startsWith(CODE)) keys.push(k);
    }
    return keys;
  }
  function localDoc() {
    const stamps = read(STAMPS, {});
    const code = {};
    codeKeys().forEach((k) => {
      const id = k.slice(CODE.length);
      // code saved before sync existed has no stamp: it counts as oldest
      code[id] = { v: localStorage.getItem(k) || "", t: stamps[id] || 1 };
    });
    return { epoch: cfg().epoch || 0, state: localState(), code };
  }
  // Same rules the server uses, so a change made while a request was in the
  // air is not lost when the answer lands.
  function mergeState(a, b) {
    const done = Object.assign({}, a.done);
    Object.keys(b.done).forEach((k) => {
      if (!done[k] || b.done[k].at < done[k].at) done[k] = b.done[k];
    });
    return {
      done,
      peeked: Object.assign({}, a.peeked, b.peeked),
      days: Array.from(new Set(a.days.concat(b.days))).sort(),
    };
  }

  function apply(doc) {
    const c = cfg();
    const replaced = doc.epoch > (c.epoch || 0); // progress was reset on another device
    const before = localStorage.getItem(STATE);
    let stamps = read(STAMPS, {});
    if (replaced) {
      codeKeys().forEach((k) => localStorage.removeItem(k));
      stamps = {};
    }
    const st = replaced ? Object.assign(blankState(), doc.state) : mergeState(localState(), doc.state);
    st.xp = Object.keys(st.done).reduce((n, k) => n + (st.done[k].xp || 0), 0);
    write(STATE, st);

    const codeChanged = [];
    Object.keys(doc.code).forEach((id) => {
      const mine = localStorage.getItem(CODE + id);
      const mineAt = mine === null ? 0 : stamps[id] || 1;
      const theirs = doc.code[id];
      if (theirs.t <= mineAt) return;
      stamps[id] = theirs.t;
      if (theirs.v !== mine) {
        localStorage.setItem(CODE + id, theirs.v);
        codeChanged.push(id);
      }
    });
    write(STAMPS, stamps);
    setCfg({ epoch: doc.epoch, last: Date.now() });
    if (replaced || codeChanged.length || localStorage.getItem(STATE) !== before) {
      appliedFns.forEach((f) => f({ replaced, codeChanged }));
    }
  }

  // ------------------------------------------------------------ requests
  async function post(path, body, token) {
    const headers = { "Content-Type": "application/json" };
    if (token) headers.Authorization = "Bearer " + token;
    const res = await fetch(cfg().url + path, { method: "POST", headers, body: JSON.stringify(body || {}) });
    let data = {};
    try {
      data = await res.json();
    } catch (e) {}
    return { ok: res.ok, status: res.status, data };
  }

  let inflight = null;
  let again = false;
  let timer = null;
  function syncNow() {
    if (!cfg().token) return Promise.resolve(false);
    if (inflight) {
      again = true;
      return inflight;
    }
    setStatus("syncing");
    inflight = (async () => {
      try {
        const r = await post("/sync", { doc: localDoc() }, cfg().token);
        if (r.status === 401) {
          setCfg({ token: null });
          setStatus("error", "Signed out by the server. Sign in again.");
          return false;
        }
        if (!r.ok || !r.data.doc) throw new Error("bad response");
        apply(r.data.doc);
        setStatus("idle");
        return true;
      } catch (e) {
        setStatus("error", "Could not reach the sync server. Your progress is safe in this browser.");
        return false;
      } finally {
        inflight = null;
        if (again) {
          again = false;
          touch();
        }
      }
    })();
    return inflight;
  }
  // Called after every local change; batches a burst of edits into one request.
  function touch() {
    if (!cfg().token) return;
    clearTimeout(timer);
    timer = setTimeout(syncNow, 2000);
  }
  function stampCode(id) {
    if (!cfg().token && !localStorage.getItem(STAMPS)) return;
    const stamps = read(STAMPS, {});
    stamps[id] = Date.now();
    write(STAMPS, stamps);
  }

  function cleanUrl(raw) {
    let u = String(raw || "").trim().replace(/\/+$/, "");
    if (!u) throw new Error("Enter the address of your sync server.");
    if (!/^https?:\/\//i.test(u)) u = "https://" + u;
    const p = new URL(u);
    const local = ["localhost", "127.0.0.1", "[::1]"].includes(p.hostname);
    if (p.protocol !== "https:" && !local) throw new Error("The server address has to start with https://");
    return u;
  }
  async function login(url, user, password) {
    let clean;
    try {
      clean = cleanUrl(url);
    } catch (e) {
      return e.message || "That address is not valid.";
    }
    setCfg({ url: clean, user });
    let r;
    try {
      r = await post("/login", { username: user, password });
    } catch (e) {
      return "Could not reach " + clean + ". Check the address and that the server is running.";
    }
    if (!r.ok) return r.data.error || "Sign in failed.";
    // Taking the server's epoch means progress already in this browser is
    // merged in on the first sync instead of being discarded.
    setCfg({ token: r.data.token, epoch: r.data.epoch || 0 });
    await syncNow();
    return null;
  }
  async function logout() {
    const token = cfg().token;
    setCfg({ token: null });
    setStatus("idle");
    try {
      if (token) await post("/logout", {}, token);
    } catch (e) {}
  }
  // Erase progress on the server so no other device brings it back.
  async function reset() {
    if (!cfg().token) return true;
    clearTimeout(timer);
    try {
      if (inflight) await inflight;
      const r = await post("/reset", {}, cfg().token);
      if (!r.ok) return false;
      setCfg({ epoch: r.data.doc.epoch, last: Date.now() });
      return true;
    } catch (e) {
      return false;
    }
  }

  document.addEventListener("visibilitychange", () => {
    if (document.visibilityState === "visible") syncNow(); // pick up work from other devices
    else if (timer) {
      clearTimeout(timer); // leaving the page: send pending changes now
      timer = null;
      syncNow();
    }
  });

  return {
    login, logout, reset, syncNow, touch, stampCode,
    info: () => {
      const c = cfg();
      return { signedIn: !!c.token, url: c.url || DEFAULT_URL, user: c.user || "", last: c.last || 0, status };
    },
    onStatus: (f) => statusFns.push(f),
    onApplied: (f) => appliedFns.push(f),
    CFG,
  };
})();
