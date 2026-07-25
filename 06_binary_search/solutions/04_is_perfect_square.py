"""SOLUTION - Valid Perfect Square

Same idea as integer square root, but you only need an exact hit. O(log n).
"""


def is_perfect_square(num):
    if num < 0:
        return False
    lo, hi = 0, num
    while lo <= hi:
        mid = (lo + hi) // 2
        sq = mid * mid
        if sq == num:
            return True
        elif sq < num:
            lo = mid + 1
        else:
            hi = mid - 1
    return False


TESTS = [
    ((16,), True),
    ((14,), False),
    ((1,), True),
    ((0,), True),
    ((2,), False),
    ((25,), True),

]

if __name__ == "__main__":
    passed = 0
    for args, expected in TESTS:
        got = is_perfect_square(*args)
        passed += (got == expected)
        print(("PASS  " if got == expected else "FAIL  ") + repr(args) + " -> " + repr(got))
    print()
    print(str(passed) + "/" + str(len(TESTS)) + " passed")
