"""SOLUTION - Merge Two Sorted Lists

Compare the fronts of both lists and take the smaller each time. When one runs out,
append the rest of the other. O(n + m). This is the merge step of merge sort.
"""


def merge_two_sorted(a, b):
    i = j = 0
    out = []
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            out.append(a[i])
            i += 1
        else:
            out.append(b[j])
            j += 1
    out.extend(a[i:])
    out.extend(b[j:])
    return out


TESTS = [
    (([1, 3], [2, 4]), [1, 2, 3, 4]),
    (([], [1]), [1]),
    (([1], []), [1]),
    (([], []), []),
    (([1, 2, 3], [1, 2]), [1, 1, 2, 2, 3]),

]

if __name__ == "__main__":
    passed = 0
    for args, expected in TESTS:
        got = merge_two_sorted(*args)
        passed += (got == expected)
        print(("PASS  " if got == expected else "FAIL  ") + repr(args) + " -> " + repr(got))
    print()
    print(str(passed) + "/" + str(len(TESTS)) + " passed")
