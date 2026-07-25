"""SOLUTION - Contains Nearby Duplicate

Remember where you last saw each value. On a repeat, the closest possible pair uses
the most recent sighting, so only the latest index matters. O(n).
"""


def contains_nearby_duplicate(nums, k):
    seen = {}
    for i, n in enumerate(nums):
        if n in seen and i - seen[n] <= k:
            return True
        seen[n] = i
    return False


TESTS = [
    (([1, 2, 3, 1], 3), True),
    (([1, 0, 1, 1], 1), True),
    (([1, 2, 3, 1, 2, 3], 2), False),
    (([], 1), False),
    (([1, 1], 0), False),

]

if __name__ == "__main__":
    passed = 0
    for args, expected in TESTS:
        got = contains_nearby_duplicate(*args)
        passed += (got == expected)
        print(("PASS  " if got == expected else "FAIL  ") + repr(args) + " -> " + repr(got))
    print()
    print(str(passed) + "/" + str(len(TESTS)) + " passed")
