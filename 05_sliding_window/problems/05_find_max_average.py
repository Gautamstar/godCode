"""
PROBLEM : Maximum Average Subarray
TOPIC   : Sliding Window (fixed)
LEVEL   : Easy

    Return the maximum AVERAGE of any contiguous subarray of length exactly k.
    Return it as a float.

Examples:
    find_max_average([1,12,-5,-6,50,3], 4)  ->  12.75

Hint (only peek if you are stuck):
    Same sliding sum as before, just divide the best sum by k at the very end.

HOW TO RUN:  python 05_sliding_window\problems\05_find_max_average.py
"""


def find_max_average(nums, k):
    # YOUR CODE HERE
    pass


# --------------------------- tests: do not edit ---------------------------
TESTS = [
    (([1, 12, -5, -6, 50, 3], 4), 12.75),
    (([5], 1), 5.0),
    (([0, 1, 1, 3, 3], 4), 2.0),

]

if __name__ == "__main__":
    passed = 0
    for args, expected in TESTS:
        try:
            got = find_max_average(*args)
        except Exception as e:
            got = "ERROR: " + str(e)
        ok = got == expected
        passed += ok
        print(("PASS  " if ok else "FAIL  ") + "find_max_average" + repr(args) +
              " -> " + repr(got) + "   expected " + repr(expected))
    print()
    print(str(passed) + "/" + str(len(TESTS)) + " passed")
