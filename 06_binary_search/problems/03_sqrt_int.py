"""
PROBLEM : Integer Square Root
TOPIC   : Binary Search on Answer
LEVEL   : Easy

    Return the FLOOR of the square root of a non-negative integer x
    (the largest integer whose square is <= x). Do not use x ** 0.5.

Examples:
    sqrt_int(8)   ->  2
    sqrt_int(16)  ->  4

Hint (only peek if you are stuck):
    Binary search the ANSWER between 1 and x//2. Keep the last mid whose square fits.

HOW TO RUN:  python 06_binary_search\problems\03_sqrt_int.py
"""


def sqrt_int(x):
    # YOUR CODE HERE
    pass


# --------------------------- tests: do not edit ---------------------------
TESTS = [
    ((4,), 2),
    ((8,), 2),
    ((0,), 0),
    ((1,), 1),
    ((16,), 4),
    ((15,), 3),

]

if __name__ == "__main__":
    passed = 0
    for args, expected in TESTS:
        try:
            got = sqrt_int(*args)
        except Exception as e:
            got = "ERROR: " + str(e)
        ok = got == expected
        passed += ok
        print(("PASS  " if ok else "FAIL  ") + "sqrt_int" + repr(args) +
              " -> " + repr(got) + "   expected " + repr(expected))
    print()
    print(str(passed) + "/" + str(len(TESTS)) + " passed")
