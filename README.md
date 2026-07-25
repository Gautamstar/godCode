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

## How to use this

1. **Read the lesson**: `NN_topic/LESSON.md`
2. **Open a problem** in `NN_topic/problems/` and write the function body.
3. **Run it** to grade yourself instantly:

```bash
python 03_two_pointers/problems/01_two_sum_sorted.py
```

You get PASS/FAIL per test case and a tally. Fix until it is all green.

4. Only after a real attempt, compare with `NN_topic/solutions/` for the clean version and
   an explanation of *why* it works.

## Rules that make this work
- **Write from memory.** Do not copy a solution and move on. The struggle is the learning.
- **Never edit the TESTS block.**
- Stuck 10+ minutes? Read the `Hint` line in the file. Still stuck? Read the solution, then
  **close it and rewrite from memory.**
- Redo old problems cold a few days later. Spacing is what makes it stick.

## What is built

| # | Module | Problems |
|---|--------|---------|
| 00 | Python for DSA | 12 drills |
| 01 | Arrays & Strings | 8 |
| 02 | Hash Maps & Sets | 8 |
| 03 | Two Pointers | 6 |
| 04 | Stack | 6 |
| 05 | Sliding Window | 5 |
| 06 | Binary Search | 6 |

**41 exercises.** Next up: Linked List, then Trees.

## Suggested order
`00` (syntax reps) → `01` → `02` → `03` → `04` → `05` → `06`

Module **02 (hash maps)** gives the biggest single jump in problems you can solve.
Module **03 (two pointers)** is the hinge that unlocks most of the rest of the graph.

## Run a whole module at once
```bash
for f in 03_two_pointers/problems/*.py; do echo "== $f"; python "$f" | tail -1; done
```
