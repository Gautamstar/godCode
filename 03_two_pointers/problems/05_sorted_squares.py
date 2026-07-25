"""
PROBLEM : Squares of a Sorted Array
TOPIC   : Two Pointers
LEVEL   : Easy

    The list is SORTED ascending and may contain negatives. Return a SORTED list of
    the squares of each number.

Examples:
    sorted_squares([-4, -1, 0, 3, 10])  ->  [0, 1, 9, 16, 100]

Hint (only peek if you are stuck):
    The biggest square is at one END or the other (most negative or most positive). Fill the answer from the BACK.

HOW TO RUN:  python 03_two_pointers\problems\05_sorted_squares.py
"""


def sorted_squares(nums):
    # YOUR CODE HERE
    pass


# --------------------------- tests: do not edit ---------------------------
TESTS = [
    (([-4, -1, 0, 3, 10],), [0, 1, 9, 16, 100]),
    (([-7, -3, 2, 3, 11],), [4, 9, 9, 49, 121]),
    (([1, 2],), [1, 4]),
    (([],), []),
    (([-2],), [4]),

]

if __name__ == "__main__":
    passed = 0
    for args, expected in TESTS:
        try:
            got = sorted_squares(*args)
        except Exception as e:
            got = "ERROR: " + str(e)
        ok = got == expected
        passed += ok
        print(("PASS  " if ok else "FAIL  ") + "sorted_squares" + repr(args) +
              " -> " + repr(got) + "   expected " + repr(expected))
    print()
    print(str(passed) + "/" + str(len(TESTS)) + " passed")
