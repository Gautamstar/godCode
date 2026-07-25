"""SOLUTION - Count Vowels

Normalize case once, then count membership in a vowel set. O(n).
"""


def count_vowels(s):
    count = 0
    for ch in s.lower():
        if ch in "aeiou":
            count += 1
    return count


TESTS = [
    (('hello',), 2),
    (('XYZ',), 0),
    (('AEIOU',), 5),
    (('',), 0),
    (('Programming',), 3),

]

if __name__ == "__main__":
    passed = 0
    for args, expected in TESTS:
        got = count_vowels(*args)
        ok = got == expected
        passed += ok
        print(("PASS  " if ok else "FAIL  ") + repr(args) + " -> " + repr(got))
    print()
    print(str(passed) + "/" + str(len(TESTS)) + " passed")
