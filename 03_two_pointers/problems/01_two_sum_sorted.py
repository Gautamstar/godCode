"""
PROBLEM : Two Sum II (sorted input)
TOPIC   : Two Pointers
LEVEL   : Easy

    The list is SORTED ascending. Return the 1-INDEXED positions of the two
    numbers that add up to target. Exactly one answer exists.

Examples:
    two_sum_sorted([2, 7, 11, 15], 9)  ->  [1, 2]
    two_sum_sorted([2, 3, 4], 6)       ->  [1, 3]

Hint (only peek if you are stuck):
    One pointer at each end. Sum too small -> move left up. Too big -> move right down.

HOW TO RUN:  python 03_two_pointers\problems\01_two_sum_sorted.py
"""


def two_sum_sorted(numbers, target):
    # YOUR CODE HERE
    pass


# --------------------------- tests: do not edit ---------------------------
TESTS = [
    (([2, 7, 11, 15], 9), [1, 2]),
    (([2, 3, 4], 6), [1, 3]),
    (([-1, 0], -1), [1, 2]),
    (([1, 2, 3, 4], 7), [3, 4]),

]

if __name__ == "__main__":
    passed = 0
    for args, expected in TESTS:
        try:
            got = two_sum_sorted(*args)
        except Exception as e:
            got = "ERROR: " + str(e)
        ok = got == expected
        passed += ok
        print(("PASS  " if ok else "FAIL  ") + "two_sum_sorted" + repr(args) +
              " -> " + repr(got) + "   expected " + repr(expected))
    print()
    print(str(passed) + "/" + str(len(TESTS)) + " passed")
