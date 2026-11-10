// Runs Python off the main thread so a slow or looping attempt cannot freeze
// the page. The main thread kills and restarts this worker on a timeout.
importScripts("https://cdn.jsdelivr.net/pyodide/v0.26.4/full/pyodide.js");

let gradeJson = null;

const boot = (async () => {
  const pyodide = await loadPyodide();
  const src = await (await fetch("grader.py")).text();
  pyodide.FS.writeFile("grader.py", src);
  pyodide.runPython("import grader");
  gradeJson = pyodide.globals.get("grader").grade_json;
  postMessage({ type: "ready" });
})().catch((err) => postMessage({ type: "boot-error", error: String(err) }));

onmessage = async (e) => {
  const { id, code, fn, tests, prelude, limit } = e.data;
  try {
    await boot;
    const out = gradeJson(code, fn, JSON.stringify(tests), prelude || "", limit ?? undefined);
    postMessage({ type: "result", id, report: JSON.parse(out) });
  } catch (err) {
    postMessage({ type: "result", id, report: { status: "error", error: String(err), results: [], stdout: "" } });
  }
};
