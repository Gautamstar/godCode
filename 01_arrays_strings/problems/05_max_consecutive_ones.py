"""
PROBLEM : Max Consecutive Ones
TOPIC   : Arrays
LEVEL   : Easy

    Given a list of 0s and 1s, return the length of the longest run of
    consecutive 1s.

Examples:
    max_consecutive_ones([1, 1, 0, 1, 1, 1])  ->  3
    max_consecutive_ones([0, 0])             ->  0

Hint (only peek if you are stuck):
    Track a `current` streak and a `best`. Reset current to 0 when you hit a 0.

HOW TO RUN:  python 01_arrays_strings\problems\05_max_consecutive_ones.py
"""


def max_consecutive_ones(nums):
    # YOUR CODE HERE
    pass


# --------------------------- tests: do not edit ---------------------------
TESTS = [
    (([1, 1, 0, 1, 1, 1],), 3),
    (([0, 0],), 0),
    (([1],), 1),
    (([],), 0),
    (([1, 0, 1, 1],), 2),

]

if __name__ == "__main__":
    passed = 0
    for args, expected in TESTS:
        try:
            got = max_consecutive_ones(*args)
        except Exception as e:
            got = "ERROR: " + str(e)
        ok = got == expected
        passed += ok
        print(("PASS  " if ok else "FAIL  ") + "max_consecutive_ones" + repr(args) +
              " -> " + repr(got) + "   expected " + repr(expected))
    print()
    print(str(passed) + "/" + str(len(TESTS)) + " passed")
