"""
PROBLEM : Move Zeroes
TOPIC   : Arrays / Two Pointers
LEVEL   : Easy

    Move every 0 to the end of the list while keeping the order of the
    non-zero elements. Return the resulting list.

Examples:
    move_zeroes([0, 1, 0, 3, 12])  ->  [1, 3, 12, 0, 0]
    move_zeroes([0])               ->  [0]

Hint (only peek if you are stuck):
    Use a `write` index. Copy each non-zero forward, then fill the rest with 0.

HOW TO RUN:  python 01_arrays_strings\problems\06_move_zeroes.py
"""


def move_zeroes(nums):
    # YOUR CODE HERE
    pass


# --------------------------- tests: do not edit ---------------------------
TESTS = [
    (([0, 1, 0, 3, 12],), [1, 3, 12, 0, 0]),
    (([0],), [0]),
    (([1, 2, 3],), [1, 2, 3]),
    (([0, 0, 0],), [0, 0, 0]),
    (([1, 0, 2, 0, 3],), [1, 2, 3, 0, 0]),

]

if __name__ == "__main__":
    passed = 0
    for args, expected in TESTS:
        try:
            got = move_zeroes(*args)
        except Exception as e:
            got = "ERROR: " + str(e)
        ok = got == expected
        passed += ok
        print(("PASS  " if ok else "FAIL  ") + "move_zeroes" + repr(args) +
              " -> " + repr(got) + "   expected " + repr(expected))
    print()
    print(str(passed) + "/" + str(len(TESTS)) + " passed")
