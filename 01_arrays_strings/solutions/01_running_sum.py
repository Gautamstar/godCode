"""SOLUTION - Running Sum of 1d Array

Walk the list once, keeping a running total. Append the total after each add.
O(n) time, O(n) space for the output.
"""


def running_sum(nums):
    total = 0
    out = []
    for n in nums:
        total += n
        out.append(total)
    return out


TESTS = [
    (([1, 2, 3, 4],), [1, 3, 6, 10]),
    (([1, 1, 1],), [1, 2, 3]),
    (([3],), [3]),
    (([],), []),
    (([-1, 2, -3],), [-1, 1, -2]),

]

if __name__ == "__main__":
    passed = 0
    for args, expected in TESTS:
        got = running_sum(*args)
        ok = got == expected
        passed += ok
        print(("PASS  " if ok else "FAIL  ") + repr(args) + " -> " + repr(got))
    print()
    print(str(passed) + "/" + str(len(TESTS)) + " passed")
