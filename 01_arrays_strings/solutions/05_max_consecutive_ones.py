"""SOLUTION - Max Consecutive Ones

Single pass. Grow `current` on a 1, reset on a 0, and keep the best seen.
O(n) time, O(1) space.
"""


def max_consecutive_ones(nums):
    best = 0
    current = 0
    for n in nums:
        if n == 1:
            current += 1
            best = max(best, current)
        else:
            current = 0
    return best


TESTS = [
    (([1, 1, 0, 1, 1, 1],), 3),
    (([0, 0],), 0),
    (([1],), 1),
    (([],), 0),
    (([1, 0, 1, 1],), 2),

]

if __name__ == "__main__":
    passed = 0
    for args, expected in TESTS:
        got = max_consecutive_ones(*args)
        ok = got == expected
        passed += ok
        print(("PASS  " if ok else "FAIL  ") + repr(args) + " -> " + repr(got))
    print()
    print(str(passed) + "/" + str(len(TESTS)) + " passed")
