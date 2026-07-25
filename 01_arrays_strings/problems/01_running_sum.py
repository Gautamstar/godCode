"""
PROBLEM : Running Sum of 1d Array
TOPIC   : Arrays
LEVEL   : Easy

    Return a list where each element is the sum of all elements up to that
    index in nums (a running / prefix sum).

Examples:
    running_sum([1, 2, 3, 4])  ->  [1, 3, 6, 10]
    running_sum([1, 1, 1])     ->  [1, 2, 3]

Hint (only peek if you are stuck):
    Keep one variable `total`, add each number to it, append total to a result list.

HOW TO RUN:  python 01_arrays_strings\problems\01_running_sum.py
"""


def running_sum(nums):
    # YOUR CODE HERE
    pass


# --------------------------- tests: do not edit ---------------------------
TESTS = [
    (([1, 2, 3, 4],), [1, 3, 6, 10]),
    (([1, 1, 1],), [1, 2, 3]),
    (([3],), [3]),
    (([],), []),
    (([-1, 2, -3],), [-1, 1, -2]),

]

if __name__ == "__main__":
    passed = 0
    for args, expected in TESTS:
        try:
            got = running_sum(*args)
        except Exception as e:
            got = "ERROR: " + str(e)
        ok = got == expected
        passed += ok
        print(("PASS  " if ok else "FAIL  ") + "running_sum" + repr(args) +
              " -> " + repr(got) + "   expected " + repr(expected))
    print()
    print(str(passed) + "/" + str(len(TESTS)) + " passed")
