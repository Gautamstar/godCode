"""SOLUTION - Binary Search

Halve the search space every step, so O(log n). Use lo <= hi with hi = len-1, and
mid = (lo + hi) // 2. The classic bug is an off-by-one in the bounds update: it must
be mid + 1 and mid - 1, or you loop forever.
"""


def binary_search(nums, target):
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1


TESTS = [
    (([-1, 0, 3, 5, 9, 12], 9), 4),
    (([-1, 0, 3, 5, 9, 12], 2), -1),
    (([], 1), -1),
    (([5], 5), 0),
    (([1, 2], 2), 1),

]

if __name__ == "__main__":
    passed = 0
    for args, expected in TESTS:
        got = binary_search(*args)
        passed += (got == expected)
        print(("PASS  " if got == expected else "FAIL  ") + repr(args) + " -> " + repr(got))
    print()
    print(str(passed) + "/" + str(len(TESTS)) + " passed")
