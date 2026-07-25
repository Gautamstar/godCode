"""
PROBLEM : Contains Duplicate
TOPIC   : Sets
LEVEL   : Easy

    Return True if any value appears at least twice, otherwise False.

Examples:
    contains_duplicate([1, 2, 3, 1])  ->  True
    contains_duplicate([1, 2, 3])     ->  False

Hint (only peek if you are stuck):
    A set removes duplicates. Compare len(set(nums)) with len(nums).

HOW TO RUN:  python 02_hashmaps_sets\problems\02_contains_duplicate.py
"""


def contains_duplicate(nums):
    # YOUR CODE HERE
    pass


# --------------------------- tests: do not edit ---------------------------
TESTS = [
    (([1, 2, 3, 1],), True),
    (([1, 2, 3],), False),
    (([],), False),
    (([1, 1],), True),

]

if __name__ == "__main__":
    passed = 0
    for args, expected in TESTS:
        try:
            got = contains_duplicate(*args)
        except Exception as e:
            got = "ERROR: " + str(e)
        ok = got == expected
        passed += ok
        print(("PASS  " if ok else "FAIL  ") + "contains_duplicate" + repr(args) +
              " -> " + repr(got) + "   expected " + repr(expected))
    print()
    print(str(passed) + "/" + str(len(TESTS)) + " passed")
