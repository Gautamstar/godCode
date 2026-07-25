"""SOLUTION - Integer Square Root

You can binary search over the answer space, not just over a list. Any mid whose
square is <= x is a valid candidate, so record it and try bigger. O(log x).
"""


def sqrt_int(x):
    if x < 2:
        return x
    lo, hi = 1, x // 2
    ans = 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if mid * mid <= x:
            ans = mid
            lo = mid + 1
        else:
            hi = mid - 1
    return ans


TESTS = [
    ((4,), 2),
    ((8,), 2),
    ((0,), 0),
    ((1,), 1),
    ((16,), 4),
    ((15,), 3),

]

if __name__ == "__main__":
    passed = 0
    for args, expected in TESTS:
        got = sqrt_int(*args)
        passed += (got == expected)
        print(("PASS  " if got == expected else "FAIL  ") + repr(args) + " -> " + repr(got))
    print()
    print(str(passed) + "/" + str(len(TESTS)) + " passed")
