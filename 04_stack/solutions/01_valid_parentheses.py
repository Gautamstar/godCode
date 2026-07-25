"""SOLUTION - Valid Parentheses

THE classic stack problem. A stack naturally models nesting: the most recently
opened bracket must be the first one closed. Empty stack at the end means balanced.
"""


def valid_parentheses(s):
    pairs = {")": "(", "]": "[", "}": "{"}
    stack = []
    for c in s:
        if c in "([{":
            stack.append(c)
        elif c in pairs:
            if not stack or stack.pop() != pairs[c]:
                return False
    return not stack


TESTS = [
    (('()',), True),
    (('()[]{}',), True),
    (('(]',), False),
    (('([)]',), False),
    (('{[]}',), True),
    (('',), True),
    (('(',), False),
    ((')',), False),

]

if __name__ == "__main__":
    passed = 0
    for args, expected in TESTS:
        got = valid_parentheses(*args)
        passed += (got == expected)
        print(("PASS  " if got == expected else "FAIL  ") + repr(args) + " -> " + repr(got))
    print()
    print(str(passed) + "/" + str(len(TESTS)) + " passed")
