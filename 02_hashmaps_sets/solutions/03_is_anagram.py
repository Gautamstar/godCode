"""SOLUTION - Valid Anagram

Two strings are anagrams exactly when their character counts match.
sorted() is the simplest way; Counter is the same idea. O(n log n) with sorting.
"""


def is_anagram(s, t):
    return sorted(s) == sorted(t)


TESTS = [
    (('anagram', 'nagaram'), True),
    (('rat', 'car'), False),
    (('', ''), True),
    (('a', 'ab'), False),
    (('aabb', 'bbaa'), True),

]

if __name__ == "__main__":
    passed = 0
    for args, expected in TESTS:
        got = is_anagram(*args)
        ok = got == expected
        passed += ok
        print(("PASS  " if ok else "FAIL  ") + repr(args) + " -> " + repr(got))
    print()
    print(str(passed) + "/" + str(len(TESTS)) + " passed")
