"""SOLUTION - Remove Adjacent Duplicates

The stack holds the result so far. A new character that matches the top cancels it
out. One pass, O(n), and the stack IS the answer at the end.
"""


def remove_adjacent_duplicates(s):
    stack = []
    for c in s:
        if stack and stack[-1] == c:
            stack.pop()
        else:
            stack.append(c)
    return "".join(stack)


TESTS = [
    (('abbaca',), 'ca'),
    (('azxxzy',), 'ay'),
    (('',), ''),
    (('aa',), ''),
    (('abc',), 'abc'),

]

if __name__ == "__main__":
    passed = 0
    for args, expected in TESTS:
        got = remove_adjacent_duplicates(*args)
        passed += (got == expected)
        print(("PASS  " if got == expected else "FAIL  ") + repr(args) + " -> " + repr(got))
    print()
    print(str(passed) + "/" + str(len(TESTS)) + " passed")
