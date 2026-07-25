"""SOLUTION - Move Zeroes

Two pointers: `read` scans, `write` marks the next slot for a non-zero.
Afterwards, everything from `write` onward becomes 0. O(n) time, O(1) space.
"""


def move_zeroes(nums):
    write = 0
    for read in range(len(nums)):
        if nums[read] != 0:
            nums[write] = nums[read]
            write += 1
    for i in range(write, len(nums)):
        nums[i] = 0
    return nums


TESTS = [
    (([0, 1, 0, 3, 12],), [1, 3, 12, 0, 0]),
    (([0],), [0]),
    (([1, 2, 3],), [1, 2, 3]),
    (([0, 0, 0],), [0, 0, 0]),
    (([1, 0, 2, 0, 3],), [1, 2, 3, 0, 0]),

]

if __name__ == "__main__":
    passed = 0
    for args, expected in TESTS:
        got = move_zeroes(*args)
        ok = got == expected
        passed += ok
        print(("PASS  " if ok else "FAIL  ") + repr(args) + " -> " + repr(got))
    print()
    print(str(passed) + "/" + str(len(TESTS)) + " passed")
