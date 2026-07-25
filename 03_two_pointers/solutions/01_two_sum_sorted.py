"""SOLUTION - Two Sum II (sorted input)

Because the list is sorted, the sum tells you which way to move. Too small means
you need a bigger number, so advance the left pointer. Too big, pull the right in.
O(n) time, O(1) space, and no dict needed.
"""


def two_sum_sorted(numbers, target):
    left, right = 0, len(numbers) - 1
    while left < right:
        total = numbers[left] + numbers[right]
        if total == target:
            return [left + 1, right + 1]
        elif total < target:
            left += 1
        else:
            right -= 1
    return []


TESTS = [
    (([2, 7, 11, 15], 9), [1, 2]),
    (([2, 3, 4], 6), [1, 3]),
    (([-1, 0], -1), [1, 2]),
    (([1, 2, 3, 4], 7), [3, 4]),

]

if __name__ == "__main__":
    passed = 0
    for args, expected in TESTS:
        got = two_sum_sorted(*args)
        passed += (got == expected)
        print(("PASS  " if got == expected else "FAIL  ") + repr(args) + " -> " + repr(got))
    print()
    print(str(passed) + "/" + str(len(TESTS)) + " passed")
