"""Turns the practice repo into content for the web app.

    python web/build.py

Reads every NN_topic/ folder that has a drills.py, and writes
web/site/content.json. Nothing in the module folders is modified.

It also proves the content is sound before writing it: every reference solution
is run through the same grader the browser uses, and the build fails if any of
them does not pass. Drills and problems you have already solved in the repo are
detected the same way and flagged so the site can import them as progress.
"""
import ast
import importlib.util
import json
import os
import re
import signal
import sys
import textwrap
import warnings

warnings.simplefilter("ignore", SyntaxWarning)

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = os.path.join(ROOT, "web", "site")
sys.path.insert(0, ROOT)
sys.path.insert(0, SITE)
from grader import grade  # noqa: E402

TESTS_MARK = "tests: do not edit"


def read(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def load_module(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


class Timeout(Exception):
    pass


def _alarm(*_):
    raise Timeout()


def passes(code, fn, tests, prelude=""):
    """Grade with a 3 second cap so a looping attempt cannot hang the build."""
    signal.signal(signal.SIGALRM, _alarm)
    signal.alarm(3)
    try:
        return grade(code, fn, tests, prelude)["status"] == "pass"
    except Timeout:
        return False
    finally:
        signal.alarm(0)


def attach_attempt(item, mine, fn, tests, prelude):
    """Code already written in the repo: 'existing' if it passes, else 'draft'."""
    try:
        ok = passes(mine, fn, tests, prelude)
    except Exception:
        ok = False
    item["existing" if ok else "draft"] = mine


def make_tests(fn_name, cases, where):
    tests = []
    for args, expected in cases:
        a, e = repr(args), repr(expected)
        if eval(a, {}) != args or eval(e, {}) != expected:
            raise SystemExit("%s: test case does not survive repr(): %s" % (where, a))
        tests.append({"args": a, "expected": e,
                      "call": "%s(%s)" % (fn_name, ", ".join(repr(x) for x in args))})
    return tests


def node_source(lines, node):
    return "\n".join(lines[node.lineno - 1:node.end_lineno])


def header_of(lines, node):
    """The def line(s), up to but not including the body."""
    first = node.body[0]
    if first.lineno == node.lineno:
        return lines[node.lineno - 1].split(":")[0] + ":"
    stop = first.lineno - 1
    # comments sitting between the def and the body are not part of the header
    while stop > node.lineno and lines[stop - 1].strip().startswith("#"):
        stop -= 1
    return "\n".join(lines[node.lineno - 1:stop])


def is_stub(node):
    if len(node.body) != 1:
        return False
    b = node.body[0]
    if isinstance(b, ast.Pass):
        return True
    if isinstance(b, ast.Raise) and b.exc is not None:
        target = b.exc.func if isinstance(b.exc, ast.Call) else b.exc
        return getattr(target, "id", "") == "NotImplementedError"
    return False


def comment_above(lines, node):
    out = []
    i = node.lineno - 2
    while i >= 0 and lines[i].startswith("#"):
        out.append(lines[i])
        i -= 1
    out.reverse()
    text = "\n".join(re.sub(r"^# ?", "", ln) for ln in out)
    text = re.sub(r"^\d+\.\s+", "", text)
    text = re.sub(r"^ALREADY DONE\.\s+", "", text)
    # continuation lines are indented to sit under the text after "12. "
    first, _, rest = text.partition("\n")
    return (first + "\n" + textwrap.dedent(rest)).strip() if rest else first.strip()


def extras_of(tree, lines, skip_names):
    """Top level constants, imports and helpers: [(names, source)]."""
    out = []
    for node in tree.body:
        names = []
        if isinstance(node, (ast.Import, ast.ImportFrom)):
            mod = getattr(node, "module", None)
            names = [(a.asname or a.name).split(".")[0] for a in node.names]
            if mod == "drill_harness" or set(names) <= {"os", "sys"}:
                continue
        elif isinstance(node, ast.Assign):
            names = [t.id for t in node.targets if isinstance(t, ast.Name)]
        elif isinstance(node, (ast.FunctionDef, ast.ClassDef)):
            names = [node.name]
        names = [n for n in names if n not in skip_names and n != "DRILLS"]
        if names:
            out.append((names, node_source(lines, node)))
    return out


def with_extras(code, extras, skip=()):
    """Prepend whichever extras the code mentions, following helpers of helpers."""
    used = []
    seen = set(skip)
    text = code
    changed = True
    while changed:
        changed = False
        for i, (names, src) in enumerate(extras):
            if i in seen or set(names) & set(skip):
                continue
            if any(re.search(r"\b%s\b" % re.escape(n), text) for n in names):
                seen.add(i)
                used.append(i)
                text += "\n" + src
                changed = True
    if not used:
        return code
    return "\n\n\n".join(extras[i][1] for i in sorted(used)) + "\n\n\n" + code


def build_drills(folder, failures):
    path = os.path.join(ROOT, folder, "drills.py")
    mod = load_module(path, "drills_" + folder)
    src = read(path)
    lines = src.splitlines()
    tree = ast.parse(src)
    defs = {n.name: n for n in tree.body if isinstance(n, ast.FunctionDef)}

    sol_src = read(os.path.join(ROOT, folder, "solutions", "drills.py"))
    sol_lines = sol_src.splitlines()
    sol_tree = ast.parse(sol_src)
    sol_defs = {n.name: n for n in sol_tree.body if isinstance(n, ast.FunctionDef)}

    drill_names = {fn.__name__ for _, items in mod.DRILLS for _, fn, _ in items}
    extras = extras_of(tree, lines, drill_names)
    sol_extras = extras_of(sol_tree, sol_lines, ())
    prelude = "\n".join(s for _, s in extras)

    items = []
    number = 0
    for section, entries in mod.DRILLS:
        for name, fn, cases in entries:
            number += 1
            fname = fn.__name__
            where = "%s drill %d (%s)" % (folder, number, name)
            node = defs[fname]
            tests = make_tests(fname, cases, where)
            prompt = comment_above(lines, node)
            header = header_of(lines, node)
            starter = with_extras(header + "\n    raise NotImplementedError\n",
                                  [(n, s) for n, s in extras
                                   if any(re.search(r"\b%s\b" % x, prompt) for x in n)])
            solution = with_extras(node_source(sol_lines, sol_defs[fname]), sol_extras,
                                   skip=(fname,))
            if not passes(solution, fname, tests, prelude):
                failures.append(where)
            item = {
                "id": "%s/drill/%s" % (folder, fname),
                "kind": "drill", "n": number, "section": section.title()
                if section.isupper() else section,
                "title": name, "fn": fname, "prompt": prompt, "starter": starter,
                "prelude": prelude, "tests": tests, "solution": solution,
            }
            if not is_stub(node):
                attach_attempt(item, node_source(lines, node) + "\n", fname, tests, prelude)
            items.append(item)
    return items


def parse_problem_doc(doc):
    meta = {}
    body = []
    for ln in doc.strip().splitlines():
        m = re.match(r"^(PROBLEM|TOPIC|LEVEL)\s*:\s*(.*)$", ln)
        if m:
            meta[m.group(1).lower()] = m.group(2).strip()
        else:
            body.append(ln)
    text = "\n".join(body)
    text = re.split(r"\n\s*HOW TO RUN", text)[0]
    hint = ""
    parts = re.split(r"\nHint[^\n]*:\n", text, maxsplit=1)
    if len(parts) == 2:
        text, hint = parts[0], textwrap.dedent(parts[1]).strip()
    examples = ""
    parts = re.split(r"\nExamples?:\n", text, maxsplit=1)
    if len(parts) == 2:
        text, examples = parts[0], textwrap.dedent(parts[1]).strip()
    meta.update(statement=textwrap.dedent(text).strip(), examples=examples, hint=hint)
    return meta


def code_between_doc_and_tests(src, stop_pattern):
    tree = ast.parse(src)
    lines = src.splitlines()
    start = tree.body[0].end_lineno if ast.get_docstring(tree) else 0
    stop = len(lines)
    for i, ln in enumerate(lines):
        if i >= start and re.search(stop_pattern, ln):
            stop = i
            break
    return "\n".join(lines[start:stop]).strip() + "\n"


def build_problems(folder, failures):
    pdir = os.path.join(ROOT, folder, "problems")
    items = []
    if not os.path.isdir(pdir):
        return items
    for fname in sorted(f for f in os.listdir(pdir) if f.endswith(".py")):
        path = os.path.join(pdir, fname)
        slug = fname[:-3]
        where = "%s problem %s" % (folder, slug)
        src = read(path)
        # Text based on purpose: a half written attempt may not even parse,
        # and that must not stop the build.
        doc = re.match(r'\s*"""(.*?)"""', src, re.S).group(1)
        fn = re.search(r"got = (\w+)\(\*args\)", src).group(1)
        header = re.search(r"^def %s\(.*?\).*?:[ \t]*$" % fn, src, re.M | re.S).group(0)
        cases = ast.literal_eval(
            re.search(r"^TESTS\s*=\s*(\[.*?^\])", src, re.M | re.S).group(1))
        meta = parse_problem_doc(doc)
        tests = make_tests(fn, cases, where)

        sol_src = read(os.path.join(ROOT, folder, "solutions", fname))
        solution = code_between_doc_and_tests(sol_src, r"^TESTS\s*=")
        sol_doc = ast.get_docstring(ast.parse(sol_src)) or ""
        sol_note = re.sub(r"^SOLUTION[^\n]*\n*", "", sol_doc).strip()
        if not passes(solution, fn, tests):
            failures.append(where)

        item = {
            "id": "%s/problem/%s" % (folder, slug),
            "kind": "problem", "n": int(slug.split("_")[0]),
            "title": meta.get("problem", slug), "level": meta.get("level", "Easy"),
            "topic": meta.get("topic", ""), "fn": fn,
            "prompt": meta["statement"], "examples": meta["examples"],
            "hint": meta["hint"],
            "starter": header + "\n    # YOUR CODE HERE\n    pass\n",
            "prelude": "", "tests": tests,
            "solution": solution, "solutionNote": sol_note,
        }
        mine = src[src.index('"""', src.index('"""') + 3) + 3:]
        mine = mine.split("# ----", 1)[0].strip() + "\n"
        body = [ln.strip() for ln in mine.split(header, 1)[-1].splitlines()]
        if [ln for ln in body if ln and not ln.startswith("#")] != ["pass"]:
            attach_attempt(item, mine, fn, tests, "")
        items.append(item)
    return items


def main():
    failures = []
    modules = []
    for folder in sorted(os.listdir(ROOT)):
        if not re.match(r"^\d\d_", folder):
            continue
        if not os.path.isfile(os.path.join(ROOT, folder, "drills.py")):
            continue
        lesson = read(os.path.join(ROOT, folder, "LESSON.md"))
        m = re.search(r"^#\s+(.*)$", lesson, re.M)
        title = re.sub(r"^Module\s+\d+\s*[:\-]\s*", "", m.group(1)).strip()
        items = [{"id": folder + "/lesson", "kind": "lesson",
                  "title": "Lesson: " + title, "md": lesson}]
        items += build_drills(folder, failures)
        items += build_problems(folder, failures)
        modules.append({"id": folder, "num": folder[:2], "title": title, "items": items})
        d = sum(i["kind"] == "drill" for i in items)
        p = sum(i["kind"] == "problem" for i in items)
        done = sum("existing" in i for i in items)
        wip = sum("draft" in i for i in items)
        print("  %-22s %3d drills  %2d problems  %2d already solved  %d in progress"
              % (folder, d, p, done, wip))

    if failures:
        print("\nReference solutions that do NOT pass:")
        for f in failures:
            print("  " + f)
        raise SystemExit(1)

    out = os.path.join(SITE, "content.json")
    with open(out, "w", encoding="utf-8") as f:
        json.dump({"modules": modules}, f, ensure_ascii=False)
    total = sum(len(m["items"]) for m in modules)
    print("\nAll reference solutions pass. Wrote %d items to %s (%d KB)"
          % (total, os.path.relpath(out, ROOT), os.path.getsize(out) // 1024))


if __name__ == "__main__":
    main()
