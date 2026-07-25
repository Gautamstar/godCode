"""SOLUTION - Last Occurrence of a Target

Identical to find_first_occurrence with one line flipped: after recording a match,
move lo = mid + 1 to hunt for a later one. Learn these two together, they are the
basis of counting occurrences in O(log n).
"""


def find_last_occurrence(nums, target):
    lo, hi = 0, len(nums) - 1
    ans = -1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            ans = mid
            lo = mid + 1
        elif nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return ans


TESTS = [
    (([5, 7, 7, 8, 8, 10], 8), 4),
    (([1, 1, 1], 1), 2),
    (([], 1), -1),
    (([5, 7, 7, 8, 8, 10], 6), -1),
    (([1, 2, 3], 1), 0),

]

if __name__ == "__main__":
    passed = 0
    for args, expected in TESTS:
        got = find_last_occurrence(*args)
        passed += (got == expected)
        print(("PASS  " if got == expected else "FAIL  ") + repr(args) + " -> " + repr(got))
    print()
    print(str(passed) + "/" + str(len(TESTS)) + " passed")
