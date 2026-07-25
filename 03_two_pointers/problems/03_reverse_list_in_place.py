"""
PROBLEM : Reverse a List In Place
TOPIC   : Two Pointers
LEVEL   : Easy

    Reverse the list IN PLACE using two pointers (do not use slicing or reversed()).
    Return the list.

Examples:
    reverse_list_in_place([1, 2, 3])  ->  [3, 2, 1]

Hint (only peek if you are stuck):
    left at 0, right at the end. Swap them, then move both inward until they meet.

HOW TO RUN:  python 03_two_pointers\problems\03_reverse_list_in_place.py
"""


def reverse_list_in_place(nums):
    # YOUR CODE HERE
    pass


# --------------------------- tests: do not edit ---------------------------
TESTS = [
    (([1, 2, 3],), [3, 2, 1]),
    (([],), []),
    (([1],), [1]),
    (([1, 2],), [2, 1]),
    (([1, 2, 3, 4],), [4, 3, 2, 1]),

]

if __name__ == "__main__":
    passed = 0
    for args, expected in TESTS:
        try:
            got = reverse_list_in_place(*args)
        except Exception as e:
            got = "ERROR: " + str(e)
        ok = got == expected
        passed += ok
        print(("PASS  " if ok else "FAIL  ") + "reverse_list_in_place" + repr(args) +
              " -> " + repr(got) + "   expected " + repr(expected))
    print()
    print(str(passed) + "/" + str(len(TESTS)) + " passed")
