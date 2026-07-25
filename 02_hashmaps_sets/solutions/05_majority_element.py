"""SOLUTION - Majority Element

Count everything, then take the key with the max count. O(n).
(A slicker O(1)-space trick is Boyer-Moore voting, worth learning later.)
"""


def majority_element(nums):
    counts = {}
    for n in nums:
        counts[n] = counts.get(n, 0) + 1
    return max(counts, key=counts.get)


TESTS = [
    (([3, 2, 3],), 3),
    (([2, 2, 1, 1, 1, 2, 2],), 2),
    (([1],), 1),
    (([5, 5, 4],), 5),

]

if __name__ == "__main__":
    passed = 0
    for args, expected in TESTS:
        got = majority_element(*args)
        ok = got == expected
        passed += ok
        print(("PASS  " if ok else "FAIL  ") + repr(args) + " -> " + repr(got))
    print()
    print(str(passed) + "/" + str(len(TESTS)) + " passed")
