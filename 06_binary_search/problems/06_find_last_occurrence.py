"""
PROBLEM : Last Occurrence of a Target
TOPIC   : Binary Search (boundary)
LEVEL   : Easy

    The SORTED list may contain duplicates. Return the RIGHTMOST index of target,
    or -1 if it is absent.

Examples:
    find_last_occurrence([5,7,7,8,8,10], 8)  ->  4
    find_last_occurrence([1,1,1], 1)         ->  2

Hint (only peek if you are stuck):
    Mirror of the previous one: on a match, record it and search the RIGHT half.

HOW TO RUN:  python 06_binary_search\problems\06_find_last_occurrence.py
"""


def find_last_occurrence(nums, target):
    # YOUR CODE HERE
    pass


# --------------------------- tests: do not edit ---------------------------
TESTS = [
    (([5, 7, 7, 8, 8, 10], 8), 4),
    (([1, 1, 1], 1), 2),
    (([], 1), -1),
    (([5, 7, 7, 8, 8, 10], 6), -1),
    (([1, 2, 3], 1), 0),

]

if __name__ == "__main__":
    passed = 0
    for args, expected in TESTS:
        try:
            got = find_last_occurrence(*args)
        except Exception as e:
            got = "ERROR: " + str(e)
        ok = got == expected
        passed += ok
        print(("PASS  " if ok else "FAIL  ") + "find_last_occurrence" + repr(args) +
              " -> " + repr(got) + "   expected " + repr(expected))
    print()
    print(str(passed) + "/" + str(len(TESTS)) + " passed")
