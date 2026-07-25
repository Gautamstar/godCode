"""SOLUTION - Valid Palindrome

Filter to alphanumeric, lowercase it, then compare against the reversed copy.
O(n) time and space.
"""


def is_palindrome(s):
    cleaned = [c.lower() for c in s if c.isalnum()]
    return cleaned == cleaned[::-1]


TESTS = [
    (('A man, a plan, a canal: Panama',), True),
    (('race a car',), False),
    (('',), True),
    (('ab',), False),
    (('Aa',), True),

]

if __name__ == "__main__":
    passed = 0
    for args, expected in TESTS:
        got = is_palindrome(*args)
        ok = got == expected
        passed += ok
        print(("PASS  " if ok else "FAIL  ") + repr(args) + " -> " + repr(got))
    print()
    print(str(passed) + "/" + str(len(TESTS)) + " passed")
