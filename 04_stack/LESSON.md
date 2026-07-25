# Module 04: Stack

**NeetCode roadmap position:** unlocked directly by Arrays & Hashing (it sits beside Two
Pointers). Self-contained and quick to learn, which makes it a great confidence module.

---

## What a stack is

Last In, First Out. The last thing you put on is the first thing you take off.

**Picture it:** a stack of plates. You add to the top, you take from the top. You cannot
pull one from the middle without lifting everything above it.

In Python you do **not** need a special class. A plain list **is** a stack:

```python
stack = []
stack.append(x)     # push
stack.pop()         # pop the top and return it
stack[-1]           # peek at the top without removing
if not stack:       # is it empty?
```

`append` and `pop` at the end are both O(1). That is the whole data structure.

---

## The one question that reveals a stack problem

> **"Does something here need to be matched with, or undone by, something that comes later?"**

If yes, it is a stack. Nesting, pairing, undoing, and "most recent unresolved thing" are all
stack shapes.

---

## Pattern 1: matching pairs (nesting)

```python
pairs = {")": "(", "]": "[", "}": "{"}
stack = []
for c in s:
    if c in "([{":
        stack.append(c)
    elif c in pairs:
        if not stack or stack.pop() != pairs[c]:
            return False
return not stack
```

Why a stack fits perfectly: **the most recently opened bracket must be the first one closed.**
That is literally LIFO. The final `return not stack` catches unclosed leftovers like `"((("`.

---

## Pattern 2: cancelling neighbours

```python
stack = []
for c in s:
    if stack and stack[-1] == c:
        stack.pop()          # cancel
    else:
        stack.append(c)
```

Here **the stack itself is the answer**, not a helper. Finish with `"".join(stack)`.
Same shape solves backspace strings (`#` pops instead of pushing).

---

## Pattern 3: simulation / undo

Keep a running record where operations can add or remove the most recent entry. The
Baseball Game problem is exactly this: `C` cancels the last score, `D` doubles it, `+` adds
the last two.

---

## Pattern 4: monotonic stack (the "next greater" trick)

This one feels like magic the first time.

```python
result = [-1] * len(nums)
stack = []                       # holds INDICES still waiting for an answer
for i, n in enumerate(nums):
    while stack and nums[stack[-1]] < n:
        result[stack.pop()] = n  # n is the answer for everyone smaller
    stack.append(i)
```

**Picture it:** people standing in a queue, each holding up a sign asking "who is the next
person taller than me?" When a tall person walks in, they answer every waiting shorter
person at once, and those people leave the queue.

Each index is pushed once and popped once, so despite the inner `while`, it is **O(n)**, not
O(n²). Store **indices**, not values, when you need to write into a result array.

---

## Gotchas

**1. Popping an empty stack crashes.** Always guard:
```python
if stack and stack[-1] == c:      # check `stack` FIRST
```
Python's `and` short-circuits, so `stack[-1]` never runs on an empty list.

**2. Operand order.** When you pop two values for an operation, the **first** pop is the
**right-hand** operand:
```python
b = stack.pop()      # right
a = stack.pop()      # left
a - b                # NOT b - a
```
This bites everyone once on Reverse Polish Notation.

**3. `pop()` vs `pop(0)`.** `pop()` removes from the end (fast, O(1)). `pop(0)` removes from
the front and is O(n). If you need front removal, that is a **queue**, use
`collections.deque`.

---

## Now practice

Six problems in `problems/`. Start with Valid Parentheses, it is the canonical one and
shows up in real interviews constantly.

```bash
python 04_stack/problems/01_valid_parentheses.py
```
