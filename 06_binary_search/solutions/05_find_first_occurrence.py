"""SOLUTION - First Occurrence of a Target

The boundary variant, and the real skill of binary search. Finding a match is not
the end: store it as the best answer so far, then move hi = mid - 1 to look for an
even earlier one. O(log n).
"""


def find_first_occurrence(nums, target):
    lo, hi = 0, len(nums) - 1
    ans = -1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            ans = mid
            hi = mid - 1
        elif nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return ans


TESTS = [
    (([5, 7, 7, 8, 8, 10], 8), 3),
    (([5, 7, 7, 8, 8, 10], 6), -1),
    (([1, 1, 1], 1), 0),
    (([], 1), -1),
    (([1, 2, 3], 3), 2),

]

if __name__ == "__main__":
    passed = 0
    for args, expected in TESTS:
        got = find_first_occurrence(*args)
        passed += (got == expected)
        print(("PASS  " if got == expected else "FAIL  ") + repr(args) + " -> " + repr(got))
    print()
    print(str(passed) + "/" + str(len(TESTS)) + " passed")
