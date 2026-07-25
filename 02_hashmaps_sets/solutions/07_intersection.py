"""SOLUTION - Intersection of Two Arrays

Convert both to sets, intersect with &, then sort for a deterministic result.
O(n + m).
"""


def intersection(a, b):
    return sorted(set(a) & set(b))


TESTS = [
    (([1, 2, 2, 1], [2, 2]), [2]),
    (([4, 9, 5], [9, 4, 9, 8, 4]), [4, 9]),
    (([1, 2], [3, 4]), []),
    (([], [1]), []),

]

if __name__ == "__main__":
    passed = 0
    for args, expected in TESTS:
        got = intersection(*args)
        ok = got == expected
        passed += ok
        print(("PASS  " if ok else "FAIL  ") + repr(args) + " -> " + repr(got))
    print()
    print(str(passed) + "/" + str(len(TESTS)) + " passed")
