"""
PROBLEM : Count Vowels
TOPIC   : Strings
LEVEL   : Easy

    Return how many vowels (a, e, i, o, u) are in the string.
    Treat uppercase and lowercase the same.

Examples:
    count_vowels("hello")   ->  2
    count_vowels("XYZ")     ->  0

Hint (only peek if you are stuck):
    Lowercase the string first, then loop and check `if ch in "aeiou"`.

HOW TO RUN:  python 01_arrays_strings\problems\03_count_vowels.py
"""


def count_vowels(s):
    # YOUR CODE HERE
    pass


# --------------------------- tests: do not edit ---------------------------
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
        try:
            got = count_vowels(*args)
        except Exception as e:
            got = "ERROR: " + str(e)
        ok = got == expected
        passed += ok
        print(("PASS  " if ok else "FAIL  ") + "count_vowels" + repr(args) +
              " -> " + repr(got) + "   expected " + repr(expected))
    print()
    print(str(passed) + "/" + str(len(TESTS)) + " passed")
