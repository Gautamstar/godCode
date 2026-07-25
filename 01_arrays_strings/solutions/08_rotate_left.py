"""SOLUTION - Rotate List Left by K

Modulo keeps k inside the list length (rotating by len is a no-op).
Then a slice split-and-swap does the rotation. O(n).
"""


def rotate_left(nums, k):
    if not nums:
        return []
    k = k % len(nums)
    return nums[k:] + nums[:k]


TESTS = [
    (([1, 2, 3, 4, 5], 2), [3, 4, 5, 1, 2]),
    (([1, 2, 3], 4), [2, 3, 1]),
    (([1, 2, 3], 0), [1, 2, 3]),
    (([], 3), []),
    (([1, 2, 3], 3), [1, 2, 3]),

]

if __name__ == "__main__":
    passed = 0
    for args, expected in TESTS:
        got = rotate_left(*args)
        ok = got == expected
        passed += ok
        print(("PASS  " if ok else "FAIL  ") + repr(args) + " -> " + repr(got))
    print()
    print(str(passed) + "/" + str(len(TESTS)) + " passed")
