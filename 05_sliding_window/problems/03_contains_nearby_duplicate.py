"""
PROBLEM : Contains Nearby Duplicate
TOPIC   : Sliding Window + Hash
LEVEL   : Easy

    Return True if there are two EQUAL values whose indices are at most k apart.

Examples:
    contains_nearby_duplicate([1,2,3,1], 3)     ->  True
    contains_nearby_duplicate([1,2,3,1,2,3], 2) ->  False

Hint (only peek if you are stuck):
    Store value -> most recent index in a dict. When you see a repeat, check the index gap.

HOW TO RUN:  python 05_sliding_window\problems\03_contains_nearby_duplicate.py
"""


def contains_nearby_duplicate(nums, k):
    # YOUR CODE HERE
    pass


# --------------------------- tests: do not edit ---------------------------
TESTS = [
    (([1, 2, 3, 1], 3), True),
    (([1, 0, 1, 1], 1), True),
    (([1, 2, 3, 1, 2, 3], 2), False),
    (([], 1), False),
    (([1, 1], 0), False),

]

if __name__ == "__main__":
    passed = 0
    for args, expected in TESTS:
        try:
            got = contains_nearby_duplicate(*args)
        except Exception as e:
            got = "ERROR: " + str(e)
        ok = got == expected
        passed += ok
        print(("PASS  " if ok else "FAIL  ") + "contains_nearby_duplicate" + repr(args) +
              " -> " + repr(got) + "   expected " + repr(expected))
    print()
    print(str(passed) + "/" + str(len(TESTS)) + " passed")
