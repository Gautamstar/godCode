"""
PROBLEM : Valid Anagram
TOPIC   : Hash Maps
LEVEL   : Easy

    Return True if t is an anagram of s (same letters, same counts, any order).

Examples:
    is_anagram("anagram", "nagaram")  ->  True
    is_anagram("rat", "car")          ->  False

Hint (only peek if you are stuck):
    Different lengths means False right away. Otherwise compare sorted(s) to sorted(t), or use Counter.

HOW TO RUN:  python 02_hashmaps_sets\problems\03_is_anagram.py
"""


def is_anagram(s, t):
    # YOUR CODE HERE
    pass


# --------------------------- tests: do not edit ---------------------------
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
        try:
            got = is_anagram(*args)
        except Exception as e:
            got = "ERROR: " + str(e)
        ok = got == expected
        passed += ok
        print(("PASS  " if ok else "FAIL  ") + "is_anagram" + repr(args) +
              " -> " + repr(got) + "   expected " + repr(expected))
    print()
    print(str(passed) + "/" + str(len(TESTS)) + " passed")
