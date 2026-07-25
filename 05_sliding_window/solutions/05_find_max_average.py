"""SOLUTION - Maximum Average Subarray

Identical to the fixed window sum. Track the best SUM while sliding and divide once
at the end, dividing inside the loop just adds float noise. O(n).
"""


def find_max_average(nums, k):
    window = sum(nums[:k])
    best = window
    for i in range(k, len(nums)):
        window += nums[i] - nums[i - k]
        best = max(best, window)
    return best / k


TESTS = [
    (([1, 12, -5, -6, 50, 3], 4), 12.75),
    (([5], 1), 5.0),
    (([0, 1, 1, 3, 3], 4), 2.0),

]

if __name__ == "__main__":
    passed = 0
    for args, expected in TESTS:
        got = find_max_average(*args)
        passed += (got == expected)
        print(("PASS  " if got == expected else "FAIL  ") + repr(args) + " -> " + repr(got))
    print()
    print(str(passed) + "/" + str(len(TESTS)) + " passed")
