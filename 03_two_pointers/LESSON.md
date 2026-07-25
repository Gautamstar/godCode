# Module 03: Two Pointers

**NeetCode roadmap position:** unlocked by Arrays & Hashing. Unlocks Binary Search,
Sliding Window, and Linked List. This is the hinge of the whole graph, so learn it well.

---

## The idea

Instead of one index walking the list, you use **two**, and their positions carry meaning.
That extra index is what turns a nested loop (O(n²)) into a single pass (O(n)).

There are two flavours, and knowing which to reach for is most of the skill.

---

## Flavour 1: opposite ends, closing in

```python
left, right = 0, len(nums) - 1
while left < right:
    # look at nums[left] and nums[right]
    # then move ONE of them inward
```

**Use it when the list is SORTED and you are hunting for a pair**, or when you need to
compare the front against the back (palindromes, reversing).

**Picture it:** two people walking toward each other from opposite ends of a hallway,
comparing notes and deciding who steps forward.

The magic in a **sorted** list: the sum tells you which way to move.
- sum too **small** → you need a bigger number → `left += 1`
- sum too **big** → you need a smaller number → `right -= 1`

You never have to check every pair, because sorting already ruled most of them out. That is
Two Sum II.

---

## Flavour 2: same direction, different speeds (read / write)

```python
write = 0
for read in range(len(nums)):
    if <keep this one>:
        nums[write] = nums[read]
        write += 1
```

**Use it when you are filtering or rearranging a list in place.**

**Picture it:** `read` is a scout checking every seat in a row; `write` marks the next open
seat at the front. Whenever the scout finds a keeper, it gets moved up to `write`'s seat.

This is Move Zeroes, Remove Duplicates, and "compact this list" in general.

---

## Flavour 3: one pointer per list

```python
i = j = 0
while i < len(a) and j < len(b):
    if a[i] <= b[j]:
        ...; i += 1
    else:
        ...; j += 1
# do not forget the leftovers
out.extend(a[i:])
out.extend(b[j:])
```

Used to merge two sorted lists, or to check whether one string is a subsequence of another.
**The leftovers line is the step people forget**, when one list runs out, the rest of the
other still has to go somewhere.

---

## The swap trick

```python
nums[left], nums[right] = nums[right], nums[left]
```
Python swaps in one line with no temp variable. Both sides are evaluated before assignment.

---

## How to recognize a two-pointer problem

| Signal in the problem | Reach for |
|---|---|
| "the array is **sorted**" and you need a pair | opposite ends |
| palindrome / compare front to back | opposite ends |
| "remove / move / filter **in place**" | read & write |
| two sorted lists to combine or compare | one pointer each |
| "without extra space" / "O(1) space" | almost always two pointers |

That last row is the big tell. If a problem forbids extra memory, a dict is off the table
and two pointers is usually the intended answer.

---

## The gotcha

Getting the loop condition wrong. `while left < right` stops when they meet; `while left <= right`
lets them land on the same element. For pair-finding you want `<` (an element should not pair
with itself). For scanning every element you want `<=`.

---

## Now practice

Six problems in `problems/`. Do 01 and 03 first, they are the purest version of each flavour.

```bash
python 03_two_pointers/problems/01_two_sum_sorted.py
```
