# Module 05: Sliding Window

**NeetCode roadmap position:** unlocked by Two Pointers. It *is* a two-pointer technique,
specialised for problems about **contiguous** chunks of an array or string.

---

## The idea

A "window" is a contiguous slice `[left .. right]`. Instead of rebuilding the window from
scratch at every position, you **slide** it: add what enters, remove what leaves.

**Picture it:** a train window. As the train moves one metre, you do not re-photograph the
whole landscape. One new tree enters the frame on one side, one leaves on the other. That
difference is all you compute.

That is the entire performance win: recomputing each window is O(n·k), sliding is **O(n)**.

**The keyword that signals it:** *contiguous*, *substring*, *subarray*, *consecutive*.
(If order does not matter and chunks need not be adjacent, it is NOT a window problem.)

---

## Type 1: FIXED window (you are told the size k)

```python
window = sum(nums[:k])          # build the first window
best = window
for i in range(k, len(nums)):
    window += nums[i] - nums[i - k]     # add entering, remove leaving
    best = max(best, window)
return best
```

The single most important line:
```python
window += nums[i] - nums[i - k]
```
`nums[i]` is entering on the right, `nums[i - k]` is the one falling off the left. Getting
that index wrong is the classic bug. Sanity check with `k = 1`: the element leaving should be
the one you just added last time.

---

## Type 2: VARIABLE window (the size is what you are solving for)

```python
left = 0
for right in range(len(s)):
    # 1. expand: include s[right]
    while <window is invalid>:
        # 2. shrink from the left until it is valid again
        left += 1
    # 3. the window is valid here, record the answer
    best = max(best, right - left + 1)
```

Three beats: **expand, fix, record.** The right edge always moves forward; the left edge
only catches up when a rule is broken.

`right - left + 1` is the window length. The `+ 1` is because both ends are inclusive, and
forgetting it is the second classic bug.

---

## The "longest substring without repeats" version

```python
seen = {}                       # char -> most recent index
left = 0
best = 0
for right, c in enumerate(s):
    if c in seen and seen[c] >= left:
        left = seen[c] + 1      # jump past the old copy
    seen[c] = right
    best = max(best, right - left + 1)
```

The subtle part is `seen[c] >= left`. A character might be in the dict from **before** the
window started; that stale sighting must be ignored, otherwise `left` jumps backwards and
the window breaks. Note this is a window **plus a dict**, the two techniques combine
constantly.

---

## Not every "window" needs an actual window

Best Time to Buy and Sell Stock is a one-pass "remember the best so far" problem:
```python
cheapest = min(cheapest, p)
best = max(best, p - cheapest)
```
It lives in this module because it has the same feel: one pass, a couple of running values,
no nested loop. Recognizing that a problem *collapses* to two variables is a real skill.

---

## How to spot the type

| The problem says | Use |
|---|---|
| "of size k" / "of length k" | fixed window |
| "longest / shortest ... such that" | variable window |
| "contains a duplicate within k indices" | window + dict |
| "maximum profit / best so far" | running values, no real window |

---

## Now practice

Five problems in `problems/`. Do 01 first for the fixed window, then 04 for the variable
window, that pair covers the whole module.

```bash
python 05_sliding_window/problems/01_max_sum_subarray_k.py
```
