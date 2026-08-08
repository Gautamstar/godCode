# Module 30: C++ for low-level roles

Same format as the Python drills: many small exercises, one idea each, difficulty climbing
slowly, graded instantly.

Off the DSA roadmap. This is a language track, not an algorithms one.

## Setup

There is no C++ compiler on the Windows side of this machine. WSL has g++ 11.4 and make,
so everything runs there.

```bash
wsl -e bash -c "cd /mnt/c/Users/Gautam/Desktop/godCode/30_cpp && make"
```

Easier: open a WSL shell, `cd /mnt/c/Users/Gautam/Desktop/godCode/30_cpp`, and use plain
`make` from then on. All the commands below assume you are inside WSL.

## Grade yourself

```bash
make                    build and run every set
make 01_pointers        one set
make list               show the set names
make clean
```

Same filters as the Python drills, passed through `ARGS`:

```bash
make 01_pointers ARGS=14        drill 14 only
make 01_pointers ARGS=10-20     a range
make 01_pointers ARGS=array     name substring
make 01_pointers ARGS=-v        list passing drills too
```

Finished drills are counted, not printed, and the footer names the next unsolved one.

## Sanitisers are on by default

`-fsanitize=address,undefined` is in `CXXFLAGS`, and in this module that is the point.
Most C++ mistakes are silent: a dangling pointer returns plausible garbage, a signed
overflow quietly wraps, an out-of-bounds read grabs the neighbouring variable. The
sanitiser turns those into a loud abort with a stack trace, which is the only way to
learn what is actually undefined rather than merely unusual.

Turn them off only if something is slow:

```bash
make SAN=0 01_pointers
```

## Layout

```
30_cpp/
  harness/drill_harness.hpp    the runner, no external test framework
  drills/NN_topic.cpp          stubs you fill in, plus the test block
  solutions/NN_topic.cpp       reference answers, implementations only
  Makefile
```

`TODO` in a stub throws, and the runner reports it as "not started" rather than failing
it, so a fresh file reads `0/28 not started` instead of 28 wrong answers.

**Never edit the test block** at the bottom of a drills file.

## What is built

| Set | Drills | Covers |
|---|---:|---|
| `00_basics` | 30 | types, sizes, integer conversions, references vs copies, const correctness, overloads, lambdas |
| `01_pointers` | 28 | address-of and dereference, array decay, pointer arithmetic, C strings, `const` placement, out-parameters, function pointers |
| `02_memory` | 28 | `new`/`delete[]`, RAII by hand, destruction order, cleanup on the exception path, `unique_ptr` and ownership transfer, `shared_ptr`, `weak_ptr`, reference cycles, custom deleters |

## Leak detection

Off in the normal loop, because an unfinished drill throws before it can free what the test
handed it, and a wall of leak reports from TODOs is noise rather than signal. Turn it on
deliberately once a section is green:

```bash
make leaks SET=02_memory
```

That is worth doing every time you finish a section of `02_memory`. The whole module is
about not leaking, and this is the only thing that actually checks it.

Planned, in order:

| Set | Will cover |
|---|---|
| `03_classes` | constructors, destructors, the rule of three, copy semantics, operator overloading, slicing |
| `04_move` | rvalue references, `std::move`, move constructors, the rule of five, why `std::vector` growth is cheap |
| `05_templates` | function and class templates, specialisation, `constexpr`, basic concepts |
| `06_stl` | containers and their cost, iterators, iterator invalidation, the algorithm header |
| `07_bits` | masks, shifts, endianness, `alignof`, struct padding, bitfields |
| `08_concurrency` | `std::thread`, `mutex`, `atomic`, data races the thread sanitiser catches |

## Rules that make this work

- **Write from memory.** Reading a solution and moving on teaches nothing.
- Stuck 10+ minutes? Re-read the comment above the drill; the explanation is there.
  Still stuck? Read the solution, then close it and rewrite from an empty body.
- **Read the warnings.** `-Wall -Wextra -Wpedantic -Wshadow` is on. In C++ a warning is
  usually a bug you have not hit yet.
- Redo a whole set cold a week later. Spacing is what makes it stick.
