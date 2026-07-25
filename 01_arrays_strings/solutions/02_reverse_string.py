"""SOLUTION - Reverse a String

Slicing with a step of -1 walks the string backwards. O(n).
"""


def reverse_string(s):
    return s[::-1]


TESTS = [
    (('hello',), 'olleh'),
    (('a',), 'a'),
    (('',), ''),
    (('abcd',), 'dcba'),

]

if __name__ == "__main__":
    passed = 0
    for args, expected in TESTS:
        got = reverse_string(*args)
        ok = got == expected
        passed += ok
        print(("PASS  " if ok else "FAIL  ") + repr(args) + " -> " + repr(got))
    print()
    print(str(passed) + "/" + str(len(TESTS)) + " passed")
