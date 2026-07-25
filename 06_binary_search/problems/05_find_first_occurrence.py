"""
PROBLEM : First Occurrence of a Target
TOPIC   : Binary Search (boundary)
LEVEL   : Easy

    The SORTED list may contain duplicates. Return the LEFTMOST index of target,
    or -1 if it is absent.

Examples:
    find_first_occurrence([5,7,7,8,8,10], 8)  ->  3
    find_first_occurrence([1,1,1], 1)         ->  0

Hint (only peek if you are stuck):
    When you find a match, do not return. Record it and keep searching the LEFT half.

HOW TO RUN:  python 06_binary_search\problems\05_find_first_occurrence.py
"""


def find_first_occurrence(nums, target):
    # YOUR CODE HERE
    pass


# --------------------------- tests: do not edit ---------------------------
TESTS = [
    (([5, 7, 7, 8, 8, 10], 8), 3),
    (([5, 7, 7, 8, 8, 10], 6), -1),
    (([1, 1, 1], 1), 0),
    (([], 1), -1),
    (([1, 2, 3], 3), 2),

]

if __name__ == "__main__":
    passed = 0
    for args, expected in TESTS:
        try:
            got = find_first_occurrence(*args)
        except Exception as e:
            got = "ERROR: " + str(e)
        ok = got == expected
        passed += ok
        print(("PASS  " if ok else "FAIL  ") + "find_first_occurrence" + repr(args) +
              " -> " + repr(got) + "   expected " + repr(expected))
    print()
    print(str(passed) + "/" + str(len(TESTS)) + " passed")
