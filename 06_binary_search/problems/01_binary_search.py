"""
PROBLEM : Binary Search
TOPIC   : Binary Search
LEVEL   : Easy

    The list is SORTED ascending. Return the INDEX of target, or -1 if it is absent.

Examples:
    binary_search([-1,0,3,5,9,12], 9)  ->  4
    binary_search([-1,0,3,5,9,12], 2)  ->  -1

Hint (only peek if you are stuck):
    lo=0, hi=len-1. Look at the middle. Too small -> search the right half. Too big -> the left half.

HOW TO RUN:  python 06_binary_search\problems\01_binary_search.py
"""


def binary_search(nums, target):
    # YOUR CODE HERE
    pass


# --------------------------- tests: do not edit ---------------------------
TESTS = [
    (([-1, 0, 3, 5, 9, 12], 9), 4),
    (([-1, 0, 3, 5, 9, 12], 2), -1),
    (([], 1), -1),
    (([5], 5), 0),
    (([1, 2], 2), 1),

]

if __name__ == "__main__":
    passed = 0
    for args, expected in TESTS:
        try:
            got = binary_search(*args)
        except Exception as e:
            got = "ERROR: " + str(e)
        ok = got == expected
        passed += ok
        print(("PASS  " if ok else "FAIL  ") + "binary_search" + repr(args) +
              " -> " + repr(got) + "   expected " + repr(expected))
    print()
    print(str(passed) + "/" + str(len(TESTS)) + " passed")
