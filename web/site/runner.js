// Main-thread side of the Python runner.
//   Runner.onStatus(fn)            "loading" | "ready" | "error"
//   Runner.grade(item, code, opts) -> Promise<report>
// A run that takes longer than TIMEOUT_MS is treated as an infinite loop: the
// worker is terminated and a fresh one is started.
const Runner = (() => {
  const TIMEOUT_MS = 6000;
  let worker = null;
  let status = "loading";
  let seq = 0;
  const pending = new Map();
  const listeners = [];

  function setStatus(s) {
    status = s;
    listeners.forEach((fn) => fn(s));
  }

  function start() {
    setStatus("loading");
    worker = new Worker("pyworker.js");
    worker.onmessage = (e) => {
      const m = e.data;
      if (m.type === "ready") setStatus("ready");
      else if (m.type === "boot-error") setStatus("error");
      else if (m.type === "result" && pending.has(m.id)) {
        const p = pending.get(m.id);
        pending.delete(m.id);
        clearTimeout(p.timer);
        p.resolve(m.report);
      }
    };
    worker.onerror = () => setStatus("error");
  }

  function grade(item, code, opts = {}) {
    return new Promise((resolve) => {
      const id = ++seq;
      const arm = () =>
        setTimeout(() => {
          pending.delete(id);
          worker.terminate();
          start();
          resolve({
            status: "error",
            results: [],
            stdout: "",
            error:
              "Timed out after " + TIMEOUT_MS / 1000 + " seconds. This is almost always a loop that never ends: " +
              "check that every pass through the loop moves a pointer or shrinks the input.",
          });
        }, TIMEOUT_MS);
      const entry = { resolve, timer: null };
      pending.set(id, entry);
      const send = () => {
        if (!pending.has(id)) return;
        entry.timer = arm();
        worker.postMessage({ id, code, fn: item.fn, tests: item.tests, prelude: item.prelude, limit: opts.limit });
      };
      // do not start the clock while Python itself is still downloading
      if (status === "ready") send();
      else {
        const wait = (s) => {
          if (s === "ready") {
            listeners.splice(listeners.indexOf(wait), 1);
            send();
          } else if (s === "error") {
            listeners.splice(listeners.indexOf(wait), 1);
            pending.delete(id);
            resolve({ status: "error", results: [], stdout: "", error: "Python failed to load. Check your connection and reload." });
          }
        };
        listeners.push(wait);
      }
    });
  }

  start();
  return {
    grade,
    onStatus(fn) {
      listeners.push(fn);
      fn(status);
    },
  };
})();
