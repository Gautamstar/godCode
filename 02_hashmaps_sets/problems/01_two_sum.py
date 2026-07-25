"""
PROBLEM : Two Sum
TOPIC   : Hash Maps
LEVEL   : Easy

    Return the indices of the two numbers in nums that add up to target.
    Exactly one solution exists. Return them as a list [i, j] with i < j.

Examples:
    two_sum([2, 7, 11, 15], 9)  ->  [0, 1]
    two_sum([3, 2, 4], 6)       ->  [1, 2]

Hint (only peek if you are stuck):
    Store value -> index in a dict as you go. For each n, look for (target - n).

HOW TO RUN:  python 02_hashmaps_sets\problems\01_two_sum.py
"""


def two_sum(nums, target):
    # YOUR CODE HERE
    pass


# --------------------------- tests: do not edit ---------------------------
TESTS = [
    (([2, 7, 11, 15], 9), [0, 1]),
    (([3, 2, 4], 6), [1, 2]),
    (([3, 3], 6), [0, 1]),
    (([1, 5, 3], 8), [1, 2]),

]

if __name__ == "__main__":
    passed = 0
    for args, expected in TESTS:
        try:
            got = two_sum(*args)
        except Exception as e:
            got = "ERROR: " + str(e)
        ok = got == expected
        passed += ok
        print(("PASS  " if ok else "FAIL  ") + "two_sum" + repr(args) +
              " -> " + repr(got) + "   expected " + repr(expected))
    print()
    print(str(passed) + "/" + str(len(TESTS)) + " passed")
