"""Reference answers for module 04 drills."""

# A. STACK BASICS


def run_ops(ops):
    stack = []
    for op in ops:
        if op[0] == "push":
            stack.append(op[1])
        elif stack:            # a pop on empty does nothing
            stack.pop()
    return stack


def peek(stack):
    if not stack:
        return None
    return stack[-1]


def reverse_with_stack(items):
    stack = []
    for x in items:
        stack.append(x)
    out = []
    while stack:
        out.append(stack.pop())
    return out


def is_balanced_simple(s):
    depth = 0
    for c in s:
        if c == "(":
            depth += 1
        elif c == ")":
            depth -= 1
            if depth < 0:      # a closer with nothing open
                return False
    return depth == 0          # anything left open is unbalanced too


PAIRS = {")": "(", "]": "[", "}": "{"}


def is_balanced_multi(s):
    stack = []
    for c in s:
        if c in "([{":
            stack.append(c)
        elif c in PAIRS:
            if not stack or stack.pop() != PAIRS[c]:
                return False   # nothing to close, or the wrong opener
    return not stack


def max_depth(s):
    depth = 0
    best = 0
    for c in s:
        if c == "(":
            depth += 1
            best = max(best, depth)
        elif c == ")":
            depth -= 1
    return best


def evaluate_postfix(tokens):
    stack = []
    for t in tokens:
        if t in ("+", "-", "*"):
            right = stack.pop()    # first pop is the RIGHT operand
            left = stack.pop()
            if t == "+":
                stack.append(left + right)
            elif t == "-":
                stack.append(left - right)
            else:
                stack.append(left * right)
        else:
            stack.append(int(t))
    return stack[-1]


# B. UNDO AND MATCHING


def backspace(s):
    out = []
    for c in s:
        if c == "#":
            if out:
                out.pop()
        else:
            out.append(c)
    return "".join(out)


def squash(s):
    stack = []
    for c in s:
        if stack and stack[-1] == c:
            stack.pop()        # cancel instead of pushing
        else:
            stack.append(c)
    return "".join(stack)


def baseball(ops):
    stack = []
    for op in ops:
        if op == "C":
            stack.pop()
        elif op == "D":
            stack.append(stack[-1] * 2)
        elif op == "+":
            stack.append(stack[-1] + stack[-2])
        else:
            stack.append(int(op))
    return sum(stack)


def count_unmatched(s):
    open_count = 0
    unmatched_closers = 0
    for c in s:
        if c == "(":
            open_count += 1
        elif c == ")":
            if open_count:
                open_count -= 1
            else:
                unmatched_closers += 1
    return open_count + unmatched_closers


def simplify_path(path):
    stack = []
    for part in path.split("/"):
        if part == "" or part == ".":
            continue           # "//" produces empty pieces
        if part == "..":
            if stack:
                stack.pop()
        else:
            stack.append(part)
    return "/" + "/".join(stack)


def decode_repeat(s):
    out = []
    i = 0
    while i < len(s):
        if s[i].isdigit():
            times = int(s[i])
            close = s.index("]", i)
            out.append(s[i + 2:close] * times)   # skip the digit and the "["
            i = close + 1
        else:
            out.append(s[i])
            i += 1
    return "".join(out)


def reverse_words_with_stack(s):
    stack = []
    for w in s.split():
        stack.append(w)
    out = []
    while stack:
        out.append(stack.pop())
    return " ".join(out)


def is_palindrome_stack(s):
    stack = list(s)
    for c in s:
        if c != stack.pop():
            return False
    return True


def valid_pop_sequence(pushed, popped):
    stack = []
    i = 0
    for value in pushed:
        stack.append(value)
        # pop as long as the top is what we are next expecting
        while stack and i < len(popped) and stack[-1] == popped[i]:
            stack.pop()
            i += 1
    return not stack


def remove_outer(s):
    out = []
    depth = 0
    for c in s:
        if c == "(":
            if depth > 0:      # keep it only if it is not the outermost
                out.append(c)
            depth += 1
        else:
            depth -= 1
            if depth > 0:
                out.append(c)
    return "".join(out)


# C. MONOTONIC STACK


def next_greater(nums):
    out = [-1] * len(nums)
    waiting = []               # indices still without an answer
    for i, n in enumerate(nums):
        while waiting and nums[waiting[-1]] < n:
            out[waiting.pop()] = n
        waiting.append(i)
    return out


def previous_greater(nums):
    out = [-1] * len(nums)
    stack = []                 # values, decreasing from the bottom
    for i, n in enumerate(nums):
        while stack and stack[-1] <= n:
            stack.pop()
        if stack:
            out[i] = stack[-1]     # read the answer BEFORE pushing
        stack.append(n)
    return out


def next_smaller(nums):
    out = [-1] * len(nums)
    waiting = []
    for i, n in enumerate(nums):
        while waiting and nums[waiting[-1]] > n:
            out[waiting.pop()] = n
        waiting.append(i)
    return out


def previous_smaller(nums):
    out = [-1] * len(nums)
    stack = []
    for i, n in enumerate(nums):
        while stack and stack[-1] >= n:
            stack.pop()
        if stack:
            out[i] = stack[-1]
        stack.append(n)
    return out


def warmer(temps):
    out = [0] * len(temps)
    waiting = []
    for i, t in enumerate(temps):
        while waiting and temps[waiting[-1]] < t:
            j = waiting.pop()
            out[j] = i - j     # the GAP, not the temperature
        waiting.append(i)
    return out


def span(prices):
    out = []
    stack = []                 # indices of strictly greater prices
    for i, p in enumerate(prices):
        while stack and prices[stack[-1]] <= p:
            stack.pop()
        out.append(i + 1 if not stack else i - stack[-1])
        stack.append(i)
    return out


def visible_from_left(heights):
    seen = 0
    tallest = None
    for h in heights:
        if tallest is None or h > tallest:
            seen += 1
            tallest = h
    return seen


def next_greater_circular(nums):
    size = len(nums)
    out = [-1] * size
    waiting = []
    for pass_index in range(2 * size):     # walk it twice
        i = pass_index % size
        while waiting and nums[waiting[-1]] < nums[i]:
            out[waiting.pop()] = nums[i]
        if pass_index < size:              # only push on the first pass
            waiting.append(i)
    return out


def remove_k_digits(digits, k):
    stack = []
    for d in digits:
        while k and stack and stack[-1] > d:
            stack.pop()
            k -= 1
        stack.append(d)
    if k:
        stack = stack[:-k]     # still had removals left, drop from the end
    result = "".join(stack).lstrip("0")
    return result or "0"
