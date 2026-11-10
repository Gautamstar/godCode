"""Grades one exercise. Runs in two places with the same code:

  - in the browser, inside Pyodide (loaded by pyworker.js)
  - at build time, in web/build.py, to prove every reference solution passes

A test is a dict {"args": "<repr of the args tuple>", "call": "fn(1, 2)",
"expected": "<repr of the expected value>"}. Args are rebuilt with eval() for
every call, so a solution that mutates its input cannot leak into the next case.
"""
import contextlib
import io
import json
import traceback

USER_FILE = "solution.py"
MAX_OUT = 20000


def _clip(text, limit=600):
    return text if len(text) <= limit else text[:limit] + " ..."


def _format_error(code):
    """A traceback trimmed to the learner's own lines."""
    etype, exc, tb = __import__("sys").exc_info()
    if isinstance(exc, SyntaxError):
        return "".join(traceback.format_exception_only(etype, exc)).strip()
    lines = code.splitlines()
    out = []
    for frame in traceback.extract_tb(tb):
        if frame.filename == USER_FILE:
            src = lines[frame.lineno - 1].strip() if 0 < frame.lineno <= len(lines) else ""
            out.append("line %d:  %s" % (frame.lineno, src))
    out.append("".join(traceback.format_exception_only(etype, exc)).strip())
    return "\n".join(out)


def grade(code, fn_name, tests, prelude="", limit=None):
    stdout = io.StringIO()
    report = {"status": "error", "error": None, "results": [], "stdout": ""}
    ns = {"__name__": "solution"}
    with contextlib.redirect_stdout(stdout):
        try:
            if prelude:
                exec(prelude, ns)
            exec(compile(code, USER_FILE, "exec"), ns)
        except BaseException:
            report["error"] = _format_error(code)
        else:
            fn = ns.get(fn_name)
            if not callable(fn):
                report["error"] = (
                    "No function named %s was found. Keep the def line as it was given."
                    % fn_name)
            else:
                selected = tests if limit is None else tests[:limit]
                for t in selected:
                    row = {"call": t["call"], "expected": t["expected"],
                           "got": None, "status": "fail", "error": None}
                    try:
                        got = fn(*eval(t["args"], {}))
                    except NotImplementedError:
                        row["status"] = "todo"
                    except BaseException:
                        row["status"] = "error"
                        row["error"] = _format_error(code)
                    else:
                        row["got"] = _clip(repr(got))
                        if got == eval(t["expected"], {}):
                            row["status"] = "pass"
                    report["results"].append(row)
                statuses = [r["status"] for r in report["results"]]
                if statuses and all(s == "pass" for s in statuses):
                    report["status"] = "pass"
                elif statuses and all(s == "todo" for s in statuses):
                    report["status"] = "todo"
                else:
                    report["status"] = "fail"
    report["stdout"] = stdout.getvalue()[:MAX_OUT]
    return report


def grade_json(code, fn_name, tests_json, prelude="", limit=None):
    return json.dumps(grade(code, fn_name, json.loads(tests_json), prelude, limit))
