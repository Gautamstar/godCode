"""SOLUTION - Max Sum of Subarray of Size K

The fixed-size window. Recomputing every window is O(n*k); sliding makes it O(n)
because each step is one addition and one subtraction. The element leaving is at
index i - k.
"""


def max_sum_subarray_k(nums, k):
    if k <= 0 or k > len(nums):
        return 0
    window = sum(nums[:k])
    best = window
    for i in range(k, len(nums)):
        window += nums[i] - nums[i - k]
        best = max(best, window)
    return best


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
        got = max_sum_subarray_k(*args)
        passed += (got == expected)
        print(("PASS  " if got == expected else "FAIL  ") + repr(args) + " -> " + repr(got))
    print()
    print(str(passed) + "/" + str(len(TESTS)) + " passed")
