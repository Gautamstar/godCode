# Module 06: Binary Search

**NeetCode roadmap position:** unlocked by Two Pointers, and (with Linked List) it unlocks
Trees. It is really a two-pointer technique where the pointers jump to the middle instead of
stepping.

---

## The idea

If the data is **sorted**, you never have to check every element. Look at the middle: it
tells you which half to throw away. Halving repeatedly means **O(log n)**, which is why a
list of a million items takes about 20 steps.

**Picture it:** finding a word in a dictionary. You do not start at page 1. You open the
middle, see you have gone too far, and open the middle of what is left.

**The precondition is everything: the data must be sorted** (or have some sorted property).
No sorted order, no binary search.

---

## Template A: find an exact value

```python
lo, hi = 0, len(nums) - 1        # hi is the LAST index
while lo <= hi:                  # note: <=
    mid = (lo + hi) // 2
    if nums[mid] == target:
        return mid
    elif nums[mid] < target:
        lo = mid + 1             # target is right
    else:
        hi = mid - 1             # target is left
return -1
```

Memorize the pairing: **`hi = len - 1`** goes with **`while lo <= hi`** and **`mid ± 1`**.
The `+1` and `-1` are not optional. Without them the range stops shrinking and you get an
infinite loop.

---

## Template B: find the boundary (insert position / lower bound)

```python
lo, hi = 0, len(nums)            # hi is len, ONE PAST the end
while lo < hi:                   # note: <
    mid = (lo + hi) // 2
    if nums[mid] < target:
        lo = mid + 1
    else:
        hi = mid                 # NOT mid - 1
return lo                        # lo is the answer
```

This converges on the **first index whose value is >= target**, which is exactly where the
value is (or where it belongs). Different bounds, different loop condition, and `hi = mid`
rather than `mid - 1`. Do not mix the two templates, that is where the off-by-one bugs live.

---

## Template C: leftmost / rightmost occurrence (duplicates)

The real skill of binary search: **finding a match is not the end.**

```python
# LEFTMOST occurrence
ans = -1
while lo <= hi:
    mid = (lo + hi) // 2
    if nums[mid] == target:
        ans = mid
        hi = mid - 1     # record it, then keep looking LEFT
    elif nums[mid] < target:
        lo = mid + 1
    else:
        hi = mid - 1
return ans
```

For the **rightmost**, change exactly one line: `lo = mid + 1` after recording. Learn these
two as a pair. Together they let you count occurrences of a value in O(log n).

---

## Binary search on the ANSWER (the big idea)

You do not need a list at all. If you can ask *"is this candidate answer good enough?"* and
the answer flips from no to yes at some point, you can binary search the candidate space.

Integer square root is the classic:
```python
lo, hi = 1, x // 2
ans = 1
while lo <= hi:
    mid = (lo + hi) // 2
    if mid * mid <= x:
        ans = mid        # valid, try bigger
        lo = mid + 1
    else:
        hi = mid - 1     # too big
return ans
```

There is no array here. You are searching the range of possible answers. Once you see this,
a whole class of "find the minimum/maximum value such that..." problems opens up.

---

## The three bugs everyone hits

1. **Infinite loop** from writing `lo = mid` instead of `lo = mid + 1` in Template A.
2. **Mixing templates**: `hi = len(nums)` with `while lo <= hi` reads out of bounds.
3. **Forgetting it must be sorted.** If the input is not sorted, sort it first (O(n log n))
   or use a different technique entirely.

`mid = (lo + hi) // 2` is safe in Python (integers are unbounded). In Java or C++ you would
write `lo + (hi - lo) // 2` to avoid overflow, worth knowing for interviews.

---

## Now practice

Six problems in `problems/`. Do 01 (Template A), then 02 (Template B), then 05 and 06 as a
pair (Template C). Those four cover essentially every Easy binary search.

```bash
python 06_binary_search/problems/01_binary_search.py
```
