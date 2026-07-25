"""SOLUTION - Reverse a List In Place

Swap the outermost pair, then step both pointers inward. Stop when they meet.
O(n) time, O(1) space. Python swaps with a, b = b, a - no temp variable needed.
"""


def reverse_list_in_place(nums):
    left, right = 0, len(nums) - 1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1
    return nums


TESTS = [
    (([1, 2, 3],), [3, 2, 1]),
    (([],), []),
    (([1],), [1]),
    (([1, 2],), [2, 1]),
    (([1, 2, 3, 4],), [4, 3, 2, 1]),

]

if __name__ == "__main__":
    passed = 0
    for args, expected in TESTS:
        got = reverse_list_in_place(*args)
        passed += (got == expected)
        print(("PASS  " if got == expected else "FAIL  ") + repr(args) + " -> " + repr(got))
    print()
    print(str(passed) + "/" + str(len(TESTS)) + " passed")
