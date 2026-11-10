# godCode - LeetCode Mastery Workspace

## What this project is
Gautam is learning data structures and algorithms in Python from the ground up, following
the **NeetCode roadmap** ordering.

**Goal: solve most LeetCode EASY problems in Python confidently**, and learn the Python each
algorithm needs along the way.

He is a CS grad, strong in Python fundamentals but has **no prior LeetCode experience**.
Teach the pattern, not memorized solutions.

## How to coach in this repo
- **Teach one concept, then drill it.** Lesson first, then he writes code from memory.
- **Give hints, not solutions.** Only hand over a full line if he asks for it directly.
- **Run his code and report PASS/FAIL** with the exact diff. Every problem file self-tests.
- **One problem at a time.** Wait for his attempt, give tight feedback, then move on.
- Plain language, **no em dashes ever**.
- When he gets something wrong, name the concept behind the mistake, not just the fix.
- **Do not restructure existing folders.** Add new modules; leave finished work alone.

## Layout
```
godCode/
  drill_harness.py       shared runner for every drills.py
  NN_topic/
    LESSON.md            teaching for that topic (read first)
    drills.py            many small reps, ramped - do these BEFORE problems
    problems/*.py        stubs he fills in - each file self-tests
    solutions/*.py       reference answers (verified passing)
    solutions/drills.py  reference answers for the drills
```

## Two tracks
**Drills** are volume: 240 small exercises across modules 00-06, most a few lines, one idea
each, difficulty climbing inside every module. **Problems** are application. He does drills
first; the problems assume those moves are automatic.

Drill stubs `raise NotImplementedError` so the runner can separate "not started" from
"wrong". The runner counts finished drills rather than printing them, names the next
unsolved one, and takes a filter argument (`9`, `20-30`, or a name substring). Never edit
the DRILLS block at the bottom of a drills file.

## How problems work
Each file in `problems/` has the statement, examples, a hint, a function stub, and a `TESTS`
list with a runner at the bottom. He writes the body, then:

```bash
python 03_two_pointers/problems/01_two_sum_sorted.py
```

It prints PASS/FAIL per case and a tally. **Never edit the TESTS block.**

## The NeetCode roadmap (dependency graph)

```
                        Arrays & Hashing
                        /              \
                Two Pointers            Stack
               /     |      \
      Binary Search  |   Linked List
        Sliding Window  \      |
               \         \     |
                +--------> Trees <------+
                          /  |  \
                     Tries   |   Backtracking
                             |      /      \
              Heap / Priority Queue    Graphs   1-D DP
               /     |      \            |  \    /   \
        Intervals Greedy  Advanced Graphs |   2-D DP  Bit Manipulation
                                          |      \      /
                                          +---> Math & Geometry
```

## Module status

| Folder | NeetCode node | Easy-rich? | Status |
|---|---|---|---|
| `00_python_for_dsa` | (prerequisite, not a node) | - | built, 80 drills |
| `01_arrays_strings` | **Arrays & Hashing** (part 1) | yes | built, 8 problems |
| `02_hashmaps_sets` | **Arrays & Hashing** (part 2) | yes | built, 8 problems |
| `03_two_pointers` | **Two Pointers** | yes | built, 6 problems |
| `04_stack` | **Stack** | yes | built, 6 problems |
| `05_sliding_window` | **Sliding Window** | mixed | built, 5 problems |
| `06_binary_search` | **Binary Search** | yes | built, 6 problems |
| `07_linked_list` | **Linked List** | yes | TO BUILD (next) |
| `08_trees` | **Trees** | yes | TO BUILD |
| `09_tries` | **Tries** | no (Medium) | later |
| `10_heap` | **Heap / Priority Queue** | mixed | later |
| `11_backtracking` | **Backtracking** | no (Medium) | later |
| `12_graphs` | **Graphs** | no (Medium) | later |
| `13_1d_dp` | **1-D DP** | mixed | later |
| `14_2d_dp` | **2-D DP** | no | later |
| `15_greedy` | **Greedy** | mixed | later |
| `16_intervals` | **Intervals** | mixed | later |
| `17_advanced_graphs` | **Advanced Graphs** | no | later |
| `18_bit_manipulation` | **Bit Manipulation** | yes | later |
| `19_math_geometry` | **Math & Geometry** | yes | later |
| `20_react_ts` | (off-roadmap, interview prep) | - | built, 12 exercises |

Note: `01` and `02` together are NeetCode's single "Arrays & Hashing" root node. They were
built before adopting the roadmap and are deliberately left split.

## Priority for his stated goal (most Easy problems)
Finish **07 Linked List** and **08 Trees**, then jump to **18 Bit Manipulation** and
**19 Math & Geometry**, which are Easy-rich despite sitting late in the graph. Backtracking,
Graphs, and DP are mostly Medium and Hard, so they come after the Easy goal is met.

**Build the next module only when he finishes the previous one**, so the workspace stays
digestible instead of dumping 150 unused files.

## The one module that breaks the layout
`20_react_ts` is React and TypeScript, not DSA, and it is not a NeetCode node. It was added
for a technical assessment that has React (Basic) and TypeScript (Basic) sections. Because
JavaScript cannot self-test the way the Python files do, it is an npm package graded by
vitest instead of a `TESTS` block:

```
20_react_ts/
  LESSON_TYPESCRIPT.md, LESSON_REACT.md
  problems/ts/*.ts       + matching *.test.ts     (the graders)
  problems/react/*.tsx   + matching *.test.tsx
  solutions/             verified passing
  src/                   playground for npm run dev
```

Same coaching rules apply: hints not solutions, he writes it, run it and report PASS/FAIL.
Never edit a `.test.ts` or `.test.tsx` file, those are the grader.

## The web app
`web/` turns modules 00-06 into a boot.dev-style site (lesson left, editor right, Python
in the browser via Pyodide, XP and streaks in localStorage). See `web/README.md`.
After changing any lesson, drill, problem, or solution, or adding a module, regenerate the
content with `python3 web/build.py`. It fails if any reference solution stops passing.
Preview with the `godcode-web` entry in `.claude/launch.json`.

## Progress log
- 2026-07-23: workspace created. Modules 00, 01, 02 built.
- 2026-07-23: adopted the NeetCode roadmap ordering. Added 03 Two Pointers, 04 Stack,
  05 Sliding Window, 06 Binary Search. All 39 reference solutions verified passing.
  Nothing attempted by him yet.
- 2026-08-04: added `20_react_ts` for the OverClocked Services technical assessment
  (75 min, 4 sections: Machine Learning, React Basic, TypeScript Basic, Problem Solving,
  strict linear progression with no going back). 5 TypeScript exercises, 7 React exercises,
  60 grader assertions, all reference solutions verified passing.
- 2026-08-08: sat the OverClocked assessment, went well.
- 2026-08-08: drills track added across modules 00-06. 00 expanded from 12 to 80 (his
  original twelve preserved with his own solutions), and 01-06 each gained 24-30. 240
  drills total, all reference solutions verified passing. Shared `drill_harness.py`
  replaces the runner that used to be inlined at the bottom of each file.
- 2026-11-10: added `web/`, the browser version of modules 00-06 (286 items).
