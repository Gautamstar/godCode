"""Shared runner for every drills.py in this repo. You do not need to edit this.

Each drills.py defines:

    DRILLS = [
        ("SECTION TITLE", [
            ("function_name", function_name, [(args_tuple, expected), ...]),
            ...
        ]),
        ...
    ]

and ends with:

    if __name__ == "__main__":
        run(DRILLS)

USAGE

    python 00_python_for_dsa/drills.py          run everything
    python 00_python_for_dsa/drills.py 34       run drill 34 only
    python 00_python_for_dsa/drills.py 34-40    run drills 34 through 40
    python 00_python_for_dsa/drills.py dict     run every drill whose name contains "dict"
    python 00_python_for_dsa/drills.py -v       show every drill, not just problems

By default finished drills are summarised rather than listed one by one, so a
file with 70 drills does not bury the two you are actually working on.
"""
import sys
import traceback

TODO = "todo"
PASS = "pass"
FAIL = "fail"


def _check(fn, cases):
    """Return (status, detail). detail is '' unless something went wrong."""
    for args, expected in cases:
        try:
            got = fn(*args)
        except NotImplementedError:
            return TODO, ""
        except Exception:
            line = traceback.format_exc().strip().splitlines()[-1]
            return FAIL, "%s%r raised %s" % (fn.__name__, args, line)
        if got != expected:
            return FAIL, "%s%r -> %r   expected %r" % (
                fn.__name__, args, got, expected)
    return PASS, ""


def _selected(arg, number, name):
    """Does this drill match the command-line filter?"""
    if arg is None:
        return True
    if arg.isdigit():
        return number == int(arg)
    if "-" in arg and all(p.isdigit() for p in arg.split("-", 1)):
        lo, hi = (int(p) for p in arg.split("-", 1))
        return lo <= number <= hi
    return arg.lower() in name.lower()


def run(drills):
    args = [a for a in sys.argv[1:]]
    verbose = "-v" in args
    args = [a for a in args if a != "-v"]
    flt = args[0] if args else None

    counts = {PASS: 0, FAIL: 0, TODO: 0}
    number = 0
    first_todo = None
    shown_any = False

    for title, items in drills:
        header_shown = False
        for name, fn, cases in items:
            number += 1
            if not _selected(flt, number, name):
                continue
            status, detail = _check(fn, cases)
            counts[status] += 1
            if status == TODO and first_todo is None:
                first_todo = (number, name)

            noteworthy = status != PASS or verbose
            if noteworthy:
                if not header_shown:
                    print("\n" + title)
                    print("-" * len(title))
                    header_shown = True
                shown_any = True
                if status == PASS:
                    print("  %3d  PASS  %s" % (number, name))
                elif status == TODO:
                    print("  %3d  TODO  %s" % (number, name))
                else:
                    print("  %3d  FAIL  %s" % (number, name))
                    print("            " + detail)

    total = counts[PASS] + counts[FAIL] + counts[TODO]
    if not shown_any and total:
        print("\nAll %d selected drills pass." % total)

    print("\n" + "=" * 46)
    print("  %d/%d complete    %d failing    %d not started"
          % (counts[PASS], total, counts[FAIL], counts[TODO]))
    if first_todo:
        print("  next up: drill %d, %s" % first_todo)
    print("=" * 46)
