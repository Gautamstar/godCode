"""
PROBLEM : Rotate List Left by K
TOPIC   : Arrays
LEVEL   : Easy

    Rotate the list to the LEFT by k positions and return the result.
    k can be larger than the length of the list.

Examples:
    rotate_left([1, 2, 3, 4, 5], 2)  ->  [3, 4, 5, 1, 2]
    rotate_left([1, 2, 3], 4)        ->  [2, 3, 1]

Hint (only peek if you are stuck):
    Use k = k % len(nums) to handle big k, then slice: nums[k:] + nums[:k].

HOW TO RUN:  python 01_arrays_strings\problems\08_rotate_left.py
"""


def rotate_left(nums, k):
    # YOUR CODE HERE
    pass


# --------------------------- tests: do not edit ---------------------------
TESTS = [
    (([1, 2, 3, 4, 5], 2), [3, 4, 5, 1, 2]),
    (([1, 2, 3], 4), [2, 3, 1]),
    (([1, 2, 3], 0), [1, 2, 3]),
    (([], 3), []),
    (([1, 2, 3], 3), [1, 2, 3]),

]

if __name__ == "__main__":
    passed = 0
    for args, expected in TESTS:
        try:
            got = rotate_left(*args)
        except Exception as e:
            got = "ERROR: " + str(e)
        ok = got == expected
        passed += ok
        print(("PASS  " if ok else "FAIL  ") + "rotate_left" + repr(args) +
              " -> " + repr(got) + "   expected " + repr(expected))
    print()
    print(str(passed) + "/" + str(len(TESTS)) + " passed")
