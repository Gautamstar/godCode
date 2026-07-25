"""SOLUTION - Remove Duplicates from Sorted List

Since equal values are adjacent in a sorted list, compare each element to the last
one you kept. If it is new, write it forward. O(n) time, O(1) extra space.
"""


def remove_duplicates(nums):
    if not nums:
        return []
    write = 1
    for read in range(1, len(nums)):
        if nums[read] != nums[write - 1]:
            nums[write] = nums[read]
            write += 1
    return nums[:write]


TESTS = [
    (([1, 1, 2],), [1, 2]),
    (([0, 0, 1, 1, 1, 2, 2, 3, 3, 4],), [0, 1, 2, 3, 4]),
    (([],), []),
    (([1],), [1]),
    (([1, 1, 1],), [1]),

]

if __name__ == "__main__":
    passed = 0
    for args, expected in TESTS:
        got = remove_duplicates(*args)
        passed += (got == expected)
        print(("PASS  " if got == expected else "FAIL  ") + repr(args) + " -> " + repr(got))
    print()
    print(str(passed) + "/" + str(len(TESTS)) + " passed")
