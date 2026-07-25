"""
PROBLEM : First Unique Character
TOPIC   : Hash Maps
LEVEL   : Easy

    Return the INDEX of the first character that appears exactly once.
    If there is none, return -1.

Examples:
    first_uniq_char("leetcode")  ->  0
    first_uniq_char("aabb")      ->  -1

Hint (only peek if you are stuck):
    First pass: count every character into a dict. Second pass: return the first index whose count is 1.

HOW TO RUN:  python 02_hashmaps_sets\problems\04_first_uniq_char.py
"""


def first_uniq_char(s):
    # YOUR CODE HERE
    pass


# --------------------------- tests: do not edit ---------------------------
TESTS = [
    (('leetcode',), 0),
    (('loveleetcode',), 2),
    (('aabb',), -1),
    (('',), -1),
    (('z',), 0),

]

if __name__ == "__main__":
    passed = 0
    for args, expected in TESTS:
        try:
            got = first_uniq_char(*args)
        except Exception as e:
            got = "ERROR: " + str(e)
        ok = got == expected
        passed += ok
        print(("PASS  " if ok else "FAIL  ") + "first_uniq_char" + repr(args) +
              " -> " + repr(got) + "   expected " + repr(expected))
    print()
    print(str(passed) + "/" + str(len(TESTS)) + " passed")
