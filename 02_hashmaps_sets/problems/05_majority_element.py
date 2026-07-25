"""
PROBLEM : Majority Element
TOPIC   : Hash Maps
LEVEL   : Easy

    Return the element that appears more than len(nums) // 2 times.
    You may assume it always exists.

Examples:
    majority_element([3, 2, 3])           ->  3
    majority_element([2, 2, 1, 1, 1, 2, 2]) ->  2

Hint (only peek if you are stuck):
    Count occurrences in a dict, then return the key with the biggest count.

HOW TO RUN:  python 02_hashmaps_sets\problems\05_majority_element.py
"""


def majority_element(nums):
    # YOUR CODE HERE
    pass


# --------------------------- tests: do not edit ---------------------------
TESTS = [
    (([3, 2, 3],), 3),
    (([2, 2, 1, 1, 1, 2, 2],), 2),
    (([1],), 1),
    (([5, 5, 4],), 5),

]

if __name__ == "__main__":
    passed = 0
    for args, expected in TESTS:
        try:
            got = majority_element(*args)
        except Exception as e:
            got = "ERROR: " + str(e)
        ok = got == expected
        passed += ok
        print(("PASS  " if ok else "FAIL  ") + "majority_element" + repr(args) +
              " -> " + repr(got) + "   expected " + repr(expected))
    print()
    print(str(passed) + "/" + str(len(TESTS)) + " passed")
