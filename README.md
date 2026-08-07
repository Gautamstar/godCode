# godCode

Learning DSA in Python from zero LeetCode experience to solving most **Easy** problems,
following the **NeetCode roadmap** ordering.

## The roadmap

```
                        Arrays & Hashing          <- 01 + 02
                        /              \
                Two Pointers            Stack     <- 03, 04
               /     |      \
      Binary Search  |   Linked List              <- 06, 07
        Sliding Window  \      |                  <- 05
               \         \     |
                +--------> Trees <------+         <- 08
                          /  |  \
                     Tries   |   Backtracking
                             |      /      \
              Heap / Priority Queue    Graphs   1-D DP
               /     |      \            |  \    /   \
        Intervals Greedy  Advanced Graphs |   2-D DP  Bit Manipulation
                                          |      \      /
                                          +---> Math & Geometry
```

Follow the arrows. Each topic assumes the ones pointing into it.

## Two tracks

**Drills** are the volume track: 240 small exercises, most of them a few lines, difficulty
climbing slowly inside each module. Do these first. They build the reflexes.

**Problems** are the application track: full LeetCode-style questions that assume the
drills are automatic.

## How to use this

1. **Read the lesson**: `NN_topic/LESSON.md`
2. **Grind the drills**: `NN_topic/drills.py`

```bash
python 02_hashmaps_sets/drills.py
```

Finished drills are counted, not printed, so what you are working on stays visible. The
footer names the next unsolved one. You can also target a single drill, a range, or a name:

```bash
python 02_hashmaps_sets/drills.py 9
```

```bash
python 02_hashmaps_sets/drills.py 20-30
```

```bash
python 02_hashmaps_sets/drills.py group
```

3. **Then the problems** in `NN_topic/problems/`. Write the body and run the file:

```bash
python 03_two_pointers/problems/01_two_sum_sorted.py
```

4. Only after a real attempt, compare with `NN_topic/solutions/` for the clean version and
   an explanation of *why* it works. Drill answers live in `NN_topic/solutions/drills.py`.

## Rules that make this work
- **Write from memory.** Do not copy a solution and move on. The struggle is the learning.
- **Never edit the TESTS block.**
- Stuck 10+ minutes? Read the `Hint` line in the file. Still stuck? Read the solution, then
  **close it and rewrite from memory.**
- Redo old problems cold a few days later. Spacing is what makes it stick.

## What is built

| # | Module | Drills | Problems |
|---|--------|-------:|---------:|
| 00 | Python for DSA | 80 | - |
| 01 | Arrays & Strings | 30 | 8 |
| 02 | Hash Maps & Sets | 30 | 8 |
| 03 | Two Pointers | 26 | 6 |
| 04 | Stack | 26 | 6 |
| 05 | Sliding Window | 24 | 5 |
| 06 | Binary Search | 24 | 6 |
| 20 | React & TypeScript | 50 | 12 |

**240 Python drills and 39 Python problems.** Next up: Linked List, then Trees.

Module 20 is off the DSA roadmap. It is React and TypeScript interview prep and it runs on
npm and vitest rather than Python. See [20_react_ts/README.md](20_react_ts/README.md).

## Suggested order
`00` (syntax reps) → `01` → `02` → `03` → `04` → `05` → `06`

Within a module: lesson, then drills, then problems. Do not start the problems until the
drills are green, because the problems assume those moves are automatic.

Module **02 (hash maps)** gives the biggest single jump in problems you can solve.
Module **03 (two pointers)** is the hinge that unlocks most of the rest of the graph.

## Run a whole module at once
```bash
for f in 03_two_pointers/problems/*.py; do echo "== $f"; python "$f" | tail -1; done
```
