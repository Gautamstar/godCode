"""
PROBLEM : Valid Perfect Square
TOPIC   : Binary Search on Answer
LEVEL   : Easy

    Return True if num is a perfect square (some integer times itself).
    Do not use a square root function.

Examples:
    is_perfect_square(16)  ->  True
    is_perfect_square(14)  ->  False

Hint (only peek if you are stuck):
    Binary search between 0 and num for a mid where mid*mid == num.

HOW TO RUN:  python 06_binary_search\problems\04_is_perfect_square.py
"""


def is_perfect_square(num):
    # YOUR CODE HERE
    pass


# --------------------------- tests: do not edit ---------------------------
TESTS = [
    ((16,), True),
    ((14,), False),
    ((1,), True),
    ((0,), True),
    ((2,), False),
    ((25,), True),

]

if __name__ == "__main__":
    passed = 0
    for args, expected in TESTS:
        try:
            got = is_perfect_square(*args)
        except Exception as e:
            got = "ERROR: " + str(e)
        ok = got == expected
        passed += ok
        print(("PASS  " if ok else "FAIL  ") + "is_perfect_square" + repr(args) +
              " -> " + repr(got) + "   expected " + repr(expected))
    print()
    print(str(passed) + "/" + str(len(TESTS)) + " passed")
