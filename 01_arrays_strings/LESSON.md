# Module 01: Arrays & Strings

Arrays (Python lists) and strings are where most Easy problems live. Almost every one of
them is solved by **one pass with a variable that remembers something**. Learn that shape
and a huge chunk of Easy becomes routine.

---

## The core shape: one pass, one accumulator

Nearly every array problem looks like this:

```python
def solve(nums):
    result = <starting value>
    for n in nums:
        result = <update result using n>
    return result
```

What changes is only *what you remember*. Examples:

| Problem | What you remember |
|---|---|
| Sum the list | a running total |
| Find the max | the best seen so far |
| Running sums | a total, appending each step |
| Longest streak of 1s | current streak + best streak |

**Picture it:** you are walking down a hallway of numbered doors, and you can only carry a
small notebook. One pass, and whatever you need at the end must have been written in that
notebook along the way.

---

## Pattern 1: running total / prefix sum

```python
total = 0
out = []
for n in nums:
    total += n
    out.append(total)
```
Each output element is "everything up to here." Used in running-sum problems and as a
building block for range-sum questions later.

---

## Pattern 2: track the best so far

```python
best = nums[0]
for n in nums:
    best = max(best, n)
```
`max(best, n)` is the workhorse. Careful with the starting value: starting `best = 0` breaks
if every number is negative. Start from `nums[0]`, or from `float("-inf")`.

---

## Pattern 3: current streak vs best streak

```python
best = 0
current = 0
for n in nums:
    if <condition>:
        current += 1
        best = max(best, current)
    else:
        current = 0        # the streak breaks, reset
```
This solves "longest run of X" problems. The **reset** in the else branch is the part people
forget.

---

## Pattern 4: the write pointer (in-place rearrange)

When you need to move things around inside the list without a second list:

```python
write = 0
for read in range(len(nums)):
    if <keep this one>:
        nums[write] = nums[read]
        write += 1
# everything from `write` onward is leftover space
```

**Picture it:** two people walking the list. `read` scans every seat; `write` marks the next
open seat at the front. Whenever `read` finds someone worth keeping, they get moved up to
`write`'s seat. This is how Move Zeroes and "remove duplicates in place" work.

---

## Strings: the parts that bite

Strings are **immutable**, you cannot assign into them. So:

```python
s[0] = "H"          # ERROR
cleaned = [c for c in s if c.isalnum()]   # build a LIST instead
"".join(cleaned)                          # then join back into a string
```

The essential toolkit:
```python
s.lower()           # normalize case before comparing
c.isalnum()         # letter or digit?
s[::-1]             # reversed
s.split()           # into words
"".join(parts)      # list of chars/words -> string
```

**The palindrome recipe** (worth memorizing, it appears constantly):
```python
cleaned = [c.lower() for c in s if c.isalnum()]
return cleaned == cleaned[::-1]
```

---

## Two traps that will get you

**1. `.sort()` returns None.**
```python
nums = nums.sort()      # nums is now None. Bug.
nums.sort()             # correct: sorts in place
nums = sorted(nums)     # correct: returns a new list
```

**2. Empty input.** `nums[0]` on an empty list crashes. Many test suites include `[]`.
Guard it:
```python
if not nums:
    return []           # or 0, or whatever makes sense
```

---

## Complexity, quickly

One loop over the list is **O(n)** and that is what almost every Easy array problem wants.
If you find yourself writing a loop inside a loop (**O(n²)**), pause: there is usually a
dict, a set, or a single clever pass that does it faster. Module 02 is exactly that lesson.

---

## Now practice

Eight problems in `problems/`. Do them in order, they build on each other.

```bash
python 01_arrays_strings/problems/01_running_sum.py
```

Write the body, run, fix until green. Only open `solutions/` after a real attempt.
