"""
PROBLEM : Remove Duplicates from Sorted List
TOPIC   : Two Pointers
LEVEL   : Easy

    The list is SORTED. Remove duplicates so each value appears once, keeping order.
    Return the resulting list.

Examples:
    remove_duplicates([1, 1, 2])                 ->  [1, 2]
    remove_duplicates([0,0,1,1,1,2,2,3,3,4])    ->  [0, 1, 2, 3, 4]

Hint (only peek if you are stuck):
    A read pointer scans; a write pointer marks the next slot. Because it is sorted, duplicates sit next to each other.

HOW TO RUN:  python 03_two_pointers\problems\04_remove_duplicates.py
"""


def remove_duplicates(nums):
    # YOUR CODE HERE
    pass


# --------------------------- tests: do not edit ---------------------------
TESTS = [
    (([1, 1, 2],), [1, 2]),
    (([0, 0, 1, 1, 1, 2, 2, 3, 3, 4],), [0, 1, 2, 3, 4]),
    (([],), []),
    (([1],), [1]),
    (([1, 1, 1],), [1]),

]

if __name__ == "__main__":
    passed = 0
    for args, expected in TESTS:
        try:
            got = remove_duplicates(*args)
        except Exception as e:
            got = "ERROR: " + str(e)
        ok = got == expected
        passed += ok
        print(("PASS  " if ok else "FAIL  ") + "remove_duplicates" + repr(args) +
              " -> " + repr(got) + "   expected " + repr(expected))
    print()
    print(str(passed) + "/" + str(len(TESTS)) + " passed")
