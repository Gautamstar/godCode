"""SOLUTION - Is Subsequence

Walk the long string once. Each time it matches the current character of s, move
forward in s. If you reach the end of s, everything was found in order. O(len(t)).
"""


def is_subsequence(s, t):
    i = 0
    for c in t:
        if i < len(s) and s[i] == c:
            i += 1
    return i == len(s)


TESTS = [
    (('abc', 'ahbgdc'), True),
    (('axc', 'ahbgdc'), False),
    (('', 'abc'), True),
    (('abc', ''), False),
    (('b', 'abc'), True),

]

if __name__ == "__main__":
    passed = 0
    for args, expected in TESTS:
        got = is_subsequence(*args)
        passed += (got == expected)
        print(("PASS  " if got == expected else "FAIL  ") + repr(args) + " -> " + repr(got))
    print()
    print(str(passed) + "/" + str(len(TESTS)) + " passed")
