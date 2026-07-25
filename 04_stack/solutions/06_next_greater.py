"""SOLUTION - Next Greater Element

A monotonic stack. Hold indices whose answer is still unknown. When a new number
arrives, it is the answer for every waiting index smaller than it, so pop them and
fill them in. Each index is pushed and popped once, so O(n).
"""


def next_greater(nums):
    result = [-1] * len(nums)
    stack = []
    for i, n in enumerate(nums):
        while stack and nums[stack[-1]] < n:
            result[stack.pop()] = n
        stack.append(i)
    return result


TESTS = [
    (([2, 1, 3],), [3, 3, -1]),
    (([1, 2, 3],), [2, 3, -1]),
    (([3, 2, 1],), [-1, -1, -1]),
    (([],), []),
    (([1],), [-1]),

]

if __name__ == "__main__":
    passed = 0
    for args, expected in TESTS:
        got = next_greater(*args)
        passed += (got == expected)
        print(("PASS  " if got == expected else "FAIL  ") + repr(args) + " -> " + repr(got))
    print()
    print(str(passed) + "/" + str(len(TESTS)) + " passed")
