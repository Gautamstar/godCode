"""SOLUTION - Two Sum

One pass with a dict of values already seen. For each number, the partner we
need is target - n; if it is already in the dict we are done. O(n) time.
"""


def two_sum(nums, target):
    seen = {}
    for i, n in enumerate(nums):
        if target - n in seen:
            return [seen[target - n], i]
        seen[n] = i
    return []


TESTS = [
    (([2, 7, 11, 15], 9), [0, 1]),
    (([3, 2, 4], 6), [1, 2]),
    (([3, 3], 6), [0, 1]),
    (([1, 5, 3], 8), [1, 2]),

]

if __name__ == "__main__":
    passed = 0
    for args, expected in TESTS:
        got = two_sum(*args)
        ok = got == expected
        passed += ok
        print(("PASS  " if ok else "FAIL  ") + repr(args) + " -> " + repr(got))
    print()
    print(str(passed) + "/" + str(len(TESTS)) + " passed")
