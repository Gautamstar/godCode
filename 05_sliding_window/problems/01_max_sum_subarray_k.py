"""
PROBLEM : Max Sum of Subarray of Size K
TOPIC   : Sliding Window (fixed)
LEVEL   : Easy

    Return the largest sum of any CONTIGUOUS subarray of exactly length k.
    If k is bigger than the list, return 0.

Examples:
    max_sum_subarray_k([1,2,3,4,5], 2)     ->  9    (4+5)
    max_sum_subarray_k([2,1,5,1,3,2], 3)  ->  9    (5+1+3)

Hint (only peek if you are stuck):
    Sum the first k. Then slide: add the entering element, subtract the leaving one. Do NOT re-sum each window.

HOW TO RUN:  python 05_sliding_window\problems\01_max_sum_subarray_k.py
"""


def max_sum_subarray_k(nums, k):
    # YOUR CODE HERE
    pass


# --------------------------- tests: do not edit ---------------------------
TESTS = [
    (([1, 2, 3, 4, 5], 2), 9),
    (([2, 1, 5, 1, 3, 2], 3), 9),
    (([1], 1), 1),
    (([1, 2], 3), 0),
    (([-1, -2, -3], 2), -3),

]

if __name__ == "__main__":
    passed = 0
    for args, expected in TESTS:
        try:
            got = max_sum_subarray_k(*args)
        except Exception as e:
            got = "ERROR: " + str(e)
        ok = got == expected
        passed += ok
        print(("PASS  " if ok else "FAIL  ") + "max_sum_subarray_k" + repr(args) +
              " -> " + repr(got) + "   expected " + repr(expected))
    print()
    print(str(passed) + "/" + str(len(TESTS)) + " passed")
