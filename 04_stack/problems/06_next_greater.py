"""
PROBLEM : Next Greater Element
TOPIC   : Stack (monotonic)
LEVEL   : Medium

    For each element, find the next element to its RIGHT that is strictly greater.
    If there is none, use -1. Return the list of answers.

Examples:
    next_greater([2, 1, 3])  ->  [3, 3, -1]
    next_greater([3, 2, 1])  ->  [-1, -1, -1]

Hint (only peek if you are stuck):
    Keep a stack of INDICES still waiting for their answer. When a bigger number arrives, it answers all of them.

HOW TO RUN:  python 04_stack\problems\06_next_greater.py
"""


def next_greater(nums):
    # YOUR CODE HERE
    pass


# --------------------------- tests: do not edit ---------------------------
TESTS = [
    (([2, 1, 3],), [3, 3, -1]),
    (([1, 2, 3],), [2, 3, -1]),
    (([3, 2, 1],), [-1, -1, -1]),
    (([],), []),
    (([1],), [-1]),

]

if __name__ == "__main__":
    passed = 0
    for args, expected in TESTS:
        try:
            got = next_greater(*args)
        except Exception as e:
            got = "ERROR: " + str(e)
        ok = got == expected
        passed += ok
        print(("PASS  " if ok else "FAIL  ") + "next_greater" + repr(args) +
              " -> " + repr(got) + "   expected " + repr(expected))
    print()
    print(str(passed) + "/" + str(len(TESTS)) + " passed")
