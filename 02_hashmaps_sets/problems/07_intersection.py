"""
PROBLEM : Intersection of Two Arrays
TOPIC   : Sets
LEVEL   : Easy

    Return a sorted list of the values that appear in BOTH lists.
    Each value should appear only once in the result.

Examples:
    intersection([1, 2, 2, 1], [2, 2])     ->  [2]
    intersection([4, 9, 5], [9, 4, 9, 8, 4]) ->  [4, 9]

Hint (only peek if you are stuck):
    Sets support the & operator for intersection. Then wrap in sorted().

HOW TO RUN:  python 02_hashmaps_sets\problems\07_intersection.py
"""


def intersection(a, b):
    # YOUR CODE HERE
    pass


# --------------------------- tests: do not edit ---------------------------
TESTS = [
    (([1, 2, 2, 1], [2, 2]), [2]),
    (([4, 9, 5], [9, 4, 9, 8, 4]), [4, 9]),
    (([1, 2], [3, 4]), []),
    (([], [1]), []),

]

if __name__ == "__main__":
    passed = 0
    for args, expected in TESTS:
        try:
            got = intersection(*args)
        except Exception as e:
            got = "ERROR: " + str(e)
        ok = got == expected
        passed += ok
        print(("PASS  " if ok else "FAIL  ") + "intersection" + repr(args) +
              " -> " + repr(got) + "   expected " + repr(expected))
    print()
    print(str(passed) + "/" + str(len(TESTS)) + " passed")
