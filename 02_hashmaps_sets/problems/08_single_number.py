"""
PROBLEM : Single Number
TOPIC   : Hash Maps / Sets
LEVEL   : Easy

    Every element appears twice except for one. Return the one that appears once.

Examples:
    single_number([2, 2, 1])        ->  1
    single_number([4, 1, 2, 1, 2])  ->  4

Hint (only peek if you are stuck):
    Count with a dict and return the key with count 1. (A clever trick: XOR everything together.)

HOW TO RUN:  python 02_hashmaps_sets\problems\08_single_number.py
"""


def single_number(nums):
    # YOUR CODE HERE
    pass


# --------------------------- tests: do not edit ---------------------------
TESTS = [
    (([2, 2, 1],), 1),
    (([4, 1, 2, 1, 2],), 4),
    (([1],), 1),
    (([7, 3, 3],), 7),

]

if __name__ == "__main__":
    passed = 0
    for args, expected in TESTS:
        try:
            got = single_number(*args)
        except Exception as e:
            got = "ERROR: " + str(e)
        ok = got == expected
        passed += ok
        print(("PASS  " if ok else "FAIL  ") + "single_number" + repr(args) +
              " -> " + repr(got) + "   expected " + repr(expected))
    print()
    print(str(passed) + "/" + str(len(TESTS)) + " passed")
