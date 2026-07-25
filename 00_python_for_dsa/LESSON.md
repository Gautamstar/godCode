# Module 00: The Python You Actually Need for DSA

You know Python. This module is not about learning the language again, it is about the
**small set of tools that show up in almost every algorithm problem**. Master these ten
things and you will rarely be blocked by syntax, only by ideas.

---

## 1. Lists are your default container

```python
nums = [3, 1, 4]
nums.append(5)        # add to the end        -> [3, 1, 4, 5]
nums.pop()            # remove & return last  -> 5
len(nums)             # how many items
nums[0], nums[-1]     # first, last
```

`append` and `pop` from the **end** are fast (O(1)). Inserting or removing from the
**front** is slow (O(n)) because everything shifts. That single fact is why queues use
`collections.deque` instead of a list.

---

## 2. Slicing: grab a piece without a loop

```python
s = "abcdef"
s[1:4]     # "bcd"     from index 1 up to (not including) 4
s[:3]      # "abc"     from start
s[3:]      # "def"     to the end
s[::-1]    # "fedcba"  reversed (step of -1)
```

The pattern `x[::-1]` reverses any sequence (string or list). It shows up constantly in
palindrome problems.

**Picture it:** slicing indices point at the *gaps between* items, not the items. That is
why `s[1:4]` gives you 3 characters, `4 - 1`.

---

## 3. Loop with the index when you need it

```python
for n in nums:                    # just the values
for i in range(len(nums)):        # just the indices
for i, n in enumerate(nums):      # BOTH - use this one
```

`enumerate` is the one to reach for whenever a problem asks you to **return an index**
(like Two Sum). Writing `range(len(...))` and indexing manually works but is noisier.

---

## 4. Dictionaries: the "remember what I have seen" tool

```python
freq = {}
freq["a"] = 1
freq.get("z", 0)        # 0 instead of a KeyError when the key is missing
"a" in freq             # True - membership check is O(1)
for key, value in freq.items():
```

**The counting idiom you will write a hundred times:**
```python
freq[c] = freq.get(c, 0) + 1
```

**Picture it:** a dict is a coat check. You hand it a key and get your item back instantly,
no searching the whole rack. That instant lookup is what turns slow O(n²) nested loops into
fast O(n) single passes.

---

## 5. Sets: membership and dedupe

```python
seen = set()
seen.add(3)
3 in seen           # O(1)
set([1, 2, 2, 3])   # {1, 2, 3}  - duplicates vanish
set(a) & set(b)     # intersection (in both)
set(a) | set(b)     # union (in either)
```

Use a **set** when you only care *whether* you have seen something. Use a **dict** when you
also need to store something about it (a count, an index).

---

## 6. Strings are immutable

```python
s = "hello"
s[0] = "H"        # ERROR - you cannot change a string in place
s = "H" + s[1:]   # you build a NEW string instead
```

Useful string methods:
```python
s.lower()  s.upper()  s.strip()
s.split()          # "a b c" -> ["a", "b", "c"]
"-".join(["a","b"])  # "a-b"
c.isalnum()  c.isdigit()  c.isalpha()
s.startswith("ab")
```

Because strings are immutable, building one character by character in a loop is slow.
Collect pieces in a **list**, then `"".join(list)` at the end.

---

## 7. Sorting

```python
sorted(nums)                    # returns a NEW sorted list
sorted(nums, reverse=True)      # descending
nums.sort()                     # sorts IN PLACE, returns None
sorted(words, key=len)          # sort by a rule
```

**The classic bug:** `nums = nums.sort()` sets `nums` to `None`, because `.sort()` sorts in
place and returns nothing. Use `sorted()` if you want a value back.

Sorting costs O(n log n). Very often the whole trick to a problem is "sort it first."

---

## 8. Comprehensions: build a list in one line

```python
[x * 2 for x in nums]                  # transform
[x for x in nums if x > 0]             # filter
[c for c in s if c.isalnum()]          # filter characters
```

Read it as: *"give me `x * 2`, for each `x` in nums."* Same as a for-loop with `append`,
just tighter. Do not force it, a plain loop is fine and often clearer.

---

## 9. Useful built-ins that save you loops

```python
sum(nums)    min(nums)    max(nums)    abs(-3)
max(a, b)                       # bigger of two
sorted(...)  reversed(...)
range(start, stop, step)
zip(a, b)                       # walk two lists together
```

`max(best, current)` inside a loop is the standard "keep the best so far" move.

---

## 10. Multiple assignment and swapping

```python
a, b = b, a            # swap, no temp variable
left, right = 0, len(s) - 1    # set up two pointers
```

That second line is the opening move of nearly every two-pointer problem.

---

## The Big O you need (just this much)

| Notation | Meaning | Example |
|---|---|---|
| O(1) | constant, instant | dict lookup, list append |
| O(n) | one pass over the data | a single for-loop |
| O(n log n) | sorting | `sorted(nums)` |
| O(n²) | a loop inside a loop | comparing every pair |

**The move that wins most Easy problems:** replace a nested loop (O(n²)) with a dict or set
(O(n)). That is literally what Two Sum teaches.

---

## Now practice

Open `drills.py` in this folder and fill in each tiny function. They are pure syntax reps,
no algorithms yet, just building the reflexes above.

```bash
python 00_python_for_dsa/drills.py
```

When all 12 pass, move on to **Module 01: Arrays & Strings**.
