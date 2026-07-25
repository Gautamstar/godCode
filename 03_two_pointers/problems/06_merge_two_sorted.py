"""
PROBLEM : Merge Two Sorted Lists
TOPIC   : Two Pointers
LEVEL   : Easy

    Both lists are SORTED. Return one merged sorted list containing all elements.

Examples:
    merge_two_sorted([1, 3], [2, 4])  ->  [1, 2, 3, 4]

Hint (only peek if you are stuck):
    One pointer per list. Repeatedly take the smaller front element. Do not forget the leftovers.

HOW TO RUN:  python 03_two_pointers\problems\06_merge_two_sorted.py
"""


def merge_two_sorted(a, b):
    # YOUR CODE HERE
    pass


# --------------------------- tests: do not edit ---------------------------
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
        try:
            got = merge_two_sorted(*args)
        except Exception as e:
            got = "ERROR: " + str(e)
        ok = got == expected
        passed += ok
        print(("PASS  " if ok else "FAIL  ") + "merge_two_sorted" + repr(args) +
              " -> " + repr(got) + "   expected " + repr(expected))
    print()
    print(str(passed) + "/" + str(len(TESTS)) + " passed")
