# Module 02: Hash Maps & Sets

This is the single highest-value module in the whole course. Most Easy problems that look
like they need a nested loop are really **one pass plus a dict**. Learning to spot that is
what turns O(n²) brute force into O(n) clean.

---

## Why a dict is fast (the one idea)

Looking for a value in a **list** means checking items one by one: O(n).
Looking up a key in a **dict** or **set** is instant: O(1).

**Picture it:** a list is a pile of coats you have to flip through to find yours. A dict is a
coat check, you hand over the ticket and get your coat immediately, no matter how many coats
there are. Every time you find yourself scanning a list to ask "have I seen this before?",
that is a dict or set asking to be used.

---

## Set vs dict: which one?

| Question you are asking | Use |
|---|---|
| "Have I seen this before?" | **set** |
| "How many times have I seen this?" | **dict** (value = count) |
| "Where did I see this?" | **dict** (value = index) |

A set stores only membership. A dict stores membership *plus* something about it.

---

## Pattern 1: frequency counting

The idiom you will write constantly:

```python
freq = {}
for c in s:
    freq[c] = freq.get(c, 0) + 1
```

`freq.get(c, 0)` means "the current count, or 0 if this is the first time." Without it you
get a `KeyError` on the first sighting.

Then a **second pass** answers the question:
```python
for i, c in enumerate(s):
    if freq[c] == 1:
        return i        # first character that appears exactly once
```

Two passes, still O(n). Counting first and answering second is a very common structure.

---

## Pattern 2: "have I seen the partner?" (the Two Sum move)

The brute force is a nested loop, checking every pair, O(n²):

```python
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == target:
            return [i, j]
```

The fast version flips the question. Instead of *searching* for the partner, **remember what
you have passed** and check if the partner is already behind you:

```python
seen = {}                       # value -> index
for i, n in enumerate(nums):
    if target - n in seen:      # the partner already went by
        return [seen[target - n], i]
    seen[n] = i
```

One pass, O(n).

**Picture it:** instead of every guest searching the whole room for their match, each guest
writes their name on a board as they walk in and just glances at the board. The board is the
dict.

This "store what you have seen, check for what you need" shape solves a whole family of
problems.

---

## Pattern 3: dedupe and membership with sets

```python
len(set(nums)) != len(nums)     # any duplicates?
sorted(set(a) & set(b))         # values in BOTH lists
seen = set()
if x in seen: ...
seen.add(x)
```

Set operators: `&` intersection (in both), `|` union (in either), `-` difference.

---

## Pattern 4: comparing two collections

Anagrams, permutations, "same contents" questions all reduce to **compare the counts**:

```python
sorted(s) == sorted(t)          # simple, O(n log n)
Counter(s) == Counter(t)        # same idea, O(n)
```

`from collections import Counter` gives you the counting dict for free:
```python
from collections import Counter
freq = Counter("aab")           # {"a": 2, "b": 1}
freq.most_common(1)             # [("a", 2)]
```
Counter is just a dict that starts every key at 0. Learn the manual `.get()` version first
so you understand what it is doing, then use Counter for speed.

---

## The mental checklist

When you read an Easy problem, ask in this order:

1. Does it involve **counting** things? → dict / Counter
2. Does it ask **"is it there / seen before / duplicate"**? → set
3. Does it ask for an **index**? → dict mapping value → index, and use `enumerate`
4. Am I about to write a **nested loop**? → stop, a dict probably removes the inner one

That checklist alone will carry you through a large slice of Easy problems.

---

## One gotcha

Dict keys must be **hashable**: numbers, strings, and tuples are fine, **lists are not**.
```python
d[[1, 2]] = 3       # TypeError: unhashable type
d[(1, 2)] = 3       # fine, tuples work
```

---

## Now practice

Eight problems in `problems/`. Two Sum is first for a reason, it is the purest version of
Pattern 2.

```bash
python 02_hashmaps_sets/problems/01_two_sum.py
```
