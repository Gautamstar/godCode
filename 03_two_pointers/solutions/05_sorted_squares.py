"""SOLUTION - Squares of a Sorted Array

Sorting the squares afterwards is O(n log n). The two-pointer trick is O(n): the
largest square must come from one of the two ends, so compare the ends and fill the
result array from the back forward.
"""


def sorted_squares(nums):
    result = [0] * len(nums)
    left, right = 0, len(nums) - 1
    for i in range(len(nums) - 1, -1, -1):
        if abs(nums[left]) > abs(nums[right]):
            result[i] = nums[left] ** 2
            left += 1
        else:
            result[i] = nums[right] ** 2
            right -= 1
    return result


TESTS = [
    (([-4, -1, 0, 3, 10],), [0, 1, 9, 16, 100]),
    (([-7, -3, 2, 3, 11],), [4, 9, 9, 49, 121]),
    (([1, 2],), [1, 4]),
    (([],), []),
    (([-2],), [4]),

]

if __name__ == "__main__":
    passed = 0
    for args, expected in TESTS:
        got = sorted_squares(*args)
        passed += (got == expected)
        print(("PASS  " if got == expected else "FAIL  ") + repr(args) + " -> " + repr(got))
    print()
    print(str(passed) + "/" + str(len(TESTS)) + " passed")
