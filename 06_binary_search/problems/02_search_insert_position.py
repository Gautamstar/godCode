"""
PROBLEM : Search Insert Position
TOPIC   : Binary Search
LEVEL   : Easy

    The list is SORTED. Return the index of target, or the index where it WOULD be
    inserted to keep the list sorted.

Examples:
    search_insert_position([1,3,5,6], 5)  ->  2
    search_insert_position([1,3,5,6], 2)  ->  1
    search_insert_position([1,3,5,6], 7)  ->  4

Hint (only peek if you are stuck):
    Use lo=0, hi=len(nums) (not len-1) and loop while lo < hi. At the end, lo is the answer.

HOW TO RUN:  python 06_binary_search\problems\02_search_insert_position.py
"""


def search_insert_position(nums, target):
    # YOUR CODE HERE
    pass


# --------------------------- tests: do not edit ---------------------------
TESTS = [
    (([1, 3, 5, 6], 5), 2),
    (([1, 3, 5, 6], 2), 1),
    (([1, 3, 5, 6], 7), 4),
    (([], 5), 0),
    (([1, 3, 5, 6], 0), 0),

]

if __name__ == "__main__":
    passed = 0
    for args, expected in TESTS:
        try:
            got = search_insert_position(*args)
        except Exception as e:
            got = "ERROR: " + str(e)
        ok = got == expected
        passed += ok
        print(("PASS  " if ok else "FAIL  ") + "search_insert_position" + repr(args) +
              " -> " + repr(got) + "   expected " + repr(expected))
    print()
    print(str(passed) + "/" + str(len(TESTS)) + " passed")
