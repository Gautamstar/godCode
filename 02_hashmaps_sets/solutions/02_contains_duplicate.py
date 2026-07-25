"""SOLUTION - Contains Duplicate

If turning the list into a set shrinks it, there was a duplicate. O(n).
"""


def contains_duplicate(nums):
    return len(set(nums)) != len(nums)


TESTS = [
    (([1, 2, 3, 1],), True),
    (([1, 2, 3],), False),
    (([],), False),
    (([1, 1],), True),

]

if __name__ == "__main__":
    passed = 0
    for args, expected in TESTS:
        got = contains_duplicate(*args)
        ok = got == expected
        passed += ok
        print(("PASS  " if ok else "FAIL  ") + repr(args) + " -> " + repr(got))
    print()
    print(str(passed) + "/" + str(len(TESTS)) + " passed")
