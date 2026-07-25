"""SOLUTION - Search Insert Position

The lower-bound form of binary search. Note the different template: hi starts at
len(nums) and the loop is lo < hi. It converges on the first index whose value is
>= target, which is exactly the insert position.
"""


def search_insert_position(nums, target):
    lo, hi = 0, len(nums)
    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid
    return lo


TESTS = [
    (([1, 3, 5, 6], 5), 2),
    (([1, 3, 5, 6], 2), 1),
    (([1, 3, 5, 6], 7), 4),
    (([], 5), 0),
    (([1, 3, 5, 6], 0), 0),

]

if __name__ == "__main__":
    passed = 0
    for args, expected in TESTS:
        got = search_insert_position(*args)
        passed += (got == expected)
        print(("PASS  " if got == expected else "FAIL  ") + repr(args) + " -> " + repr(got))
    print()
    print(str(passed) + "/" + str(len(TESTS)) + " passed")
