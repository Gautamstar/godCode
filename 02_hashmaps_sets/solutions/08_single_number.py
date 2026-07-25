"""SOLUTION - Single Number

Counting is the straightforward way. The elegant trick is XOR: a ^ a == 0, so
all the pairs cancel and only the lone value survives. O(n) time, O(1) space.
"""


def single_number(nums):
    result = 0
    for n in nums:
        result ^= n
    return result


TESTS = [
    (([2, 2, 1],), 1),
    (([4, 1, 2, 1, 2],), 4),
    (([1],), 1),
    (([7, 3, 3],), 7),

]

if __name__ == "__main__":
    passed = 0
    for args, expected in TESTS:
        got = single_number(*args)
        ok = got == expected
        passed += ok
        print(("PASS  " if ok else "FAIL  ") + repr(args) + " -> " + repr(got))
    print()
    print(str(passed) + "/" + str(len(TESTS)) + " passed")
