"""
MODULE 06 DRILLS - binary search, 24 reps.

The point of this module is repetition of ONE loop until you can type it
without thinking. Almost every drill here is that loop with a different thing
recorded, so if a drill feels like the previous one, it is, and that is the
design.

The shape:

    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            lo = mid + 1        # answer is strictly right of mid
        else:
            hi = mid - 1        # answer is strictly left of mid

The two things that cause infinite loops: forgetting the +1 or -1, and using
`while lo < hi` with the wrong update. Get the plain version right first.

RUN
    python 06_binary_search/drills.py            everything
    python 06_binary_search/drills.py 3          just drill 3
    python 06_binary_search/drills.py index      name contains "index"
    python 06_binary_search/drills.py -v         list passing drills too
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from drill_harness import run  # noqa: E402


# ===========================================================================
# A. THE INVARIANT
# ===========================================================================

# 1. Return the index of target in a sorted list, or -1.
#    Write the loop above from memory. Then delete it and write it again.
def binary_search(nums, target):
    raise NotImplementedError


# 2. The same thing, recursively, with lo and hi as parameters.
#    The base case is lo > hi, which means the range is empty.
def binary_search_rec(nums, target, lo=0, hi=None):
    raise NotImplementedError


# 3. Return the LEFTMOST index of target, or -1.
#    On a match, do not return. Record it and keep searching left by setting
#    hi = mid - 1. That one change is the whole difference.
def first_index(nums, target):
    raise NotImplementedError


# 4. Return the RIGHTMOST index of target, or -1.
#    Same, but keep searching right.
def last_index(nums, target):
    raise NotImplementedError


# 5. Count how many times target appears. Two searches, no scanning.
def count_of(nums, target):
    raise NotImplementedError


# 6. Return the index where target should be inserted to keep the list sorted.
#    insert_position([1,3,5], 4) -> 2,  insert_position([1,3], 0) -> 0
#    When the loop ends without a match, `lo` is already the answer.
def insert_position(nums, target):
    raise NotImplementedError


# 7. Return True when target is present.
def exists(nums, target):
    raise NotImplementedError


# 8. Return the VALUE closest to target. On a tie return the smaller one.
#    closest([1,4,6], 5) -> 4
#    Find the insertion point, then compare the neighbours either side of it.
def closest(nums, target):
    raise NotImplementedError


# ===========================================================================
# B. BOUNDS AND PREDICATES
# ===========================================================================

# 9. Return the largest value that is <= x, or None.
#    floor_value([1,3,5], 4) -> 3
def floor_value(nums, x):
    raise NotImplementedError


# 10. Return the smallest value that is >= x, or None.
#     ceil_value([1,3,5], 4) -> 5
def ceil_value(nums, x):
    raise NotImplementedError


# 11. Count the values that are <= x. This is an insertion point in disguise.
def count_at_most(nums, x):
    raise NotImplementedError


# 12. `flags` is a list of booleans that is all False then all True.
#     Return the index of the first True, or -1.
#     first_true([False,False,True,True]) -> 2
#     This is the general form: you are searching for the boundary where a
#     condition flips, not for a value.
def first_true(flags):
    raise NotImplementedError


# 13. Same list. Return the index of the last False, or -1.
def last_false(flags):
    raise NotImplementedError


# 14. Return the whole-number part of the square root of n, without math.sqrt.
#     sqrt_floor(8) -> 2,  sqrt_floor(9) -> 3
#     Binary search the answer between 0 and n.
def sqrt_floor(n):
    raise NotImplementedError


# 15. The list rises then falls with no plateau. Return the index of the peak.
#     peak_index([1,3,5,4,2]) -> 2
#     Compare mid with mid + 1 to decide which half the peak is in.
def peak_index(nums):
    raise NotImplementedError


# 16. A sorted list was rotated some number of places. Return its minimum.
#     min_rotated([4,5,6,1,2,3]) -> 1
#     Compare nums[mid] with nums[hi] to work out which half is sorted.
def min_rotated(nums):
    raise NotImplementedError


# ===========================================================================
# C. ROTATION, AND SEARCHING THE ANSWER
# ===========================================================================

# 17. Return how many places a sorted list was rotated, which is the index of
#     its minimum.  rotation_count([4,5,1,2,3]) -> 2
def rotation_count(nums):
    raise NotImplementedError


# 18. Find target in a rotated sorted list, or -1.
#     search_rotated([4,5,6,1,2,3], 2) -> 4
#     One half of the list either side of mid is always properly sorted.
#     Work out which, then check whether target falls inside it.
def search_rotated(nums, target):
    raise NotImplementedError


# 19. Versions 1..n, everything from `bad` onward is broken. Return `bad`,
#     using as few checks as possible. Signature takes bad so it is testable.
#     first_bad(5, 4) -> 4
def first_bad(n, bad):
    raise NotImplementedError


# 20. The list is sorted DESCENDING. Count the negatives.
#     count_negatives([5,1,-2,-9]) -> 2
#     The boundary between non-negative and negative is what you search for.
def count_negatives(nums):
    raise NotImplementedError


# 21. Return the smallest whole x with x * x >= n.
#     smallest_square_at_least(10) -> 4
def smallest_square_at_least(n):
    raise NotImplementedError


# 22. Sorted list. Return the indices [i, j] of the pair summing to target, or
#     [], by binary-searching for each complement.
#     Slower than two pointers, and the point is the search, not the speed.
def two_sum_bs(nums, target):
    raise NotImplementedError


# ---------------------------------------------------------------------------
# SEARCHING THE ANSWER
#
# The last two are the pattern that makes binary search feel powerful. The
# list is not what you search. You search the ANSWER SPACE: pick a candidate
# answer, ask a yes/no question about it, and throw away half the candidates.
# The question is always monotonic, meaning if x works then everything bigger
# works too.
# ---------------------------------------------------------------------------

# 23. Ship all the weights in order within `days`. Each day you load a prefix
#     of what is left, up to the ship's capacity. Return the smallest capacity
#     that finishes in time.
#     min_capacity([1,2,3,4,5,6,7,8,9,10], 5) -> 15
#     Capacity must be at least max(weights) and never needs to exceed their
#     sum. Write a helper that counts the days a given capacity needs.
def min_capacity(weights, days):
    raise NotImplementedError


# 24. Piles of bananas, `hours` available. At speed k per hour you finish a
#     pile of size p in ceil(p / k) hours. Return the smallest whole k that
#     clears every pile in time.
#     min_speed([3,6,7,11], 8) -> 4
#     Speed is between 1 and max(piles). Same shape as drill 23.
def min_speed(piles, hours):
    raise NotImplementedError


# --------------------------- tests: do not edit ---------------------------
DRILLS = [
    ("A. THE INVARIANT", [
        ("binary_search", binary_search, [(([1, 3, 5, 7], 5), 2), (([1, 3], 9), -1),
                                          (([], 1), -1), (([4], 4), 0)]),
        ("binary_search_rec", binary_search_rec, [(([1, 3, 5, 7], 5), 2),
                                                  (([1, 3], 9), -1), (([], 1), -1)]),
        ("first_index", first_index, [(([1, 2, 2, 2, 3], 2), 1), (([1, 2], 9), -1),
                                      (([2, 2], 2), 0)]),
        ("last_index", last_index, [(([1, 2, 2, 2, 3], 2), 3), (([1, 2], 9), -1),
                                    (([2, 2], 2), 1)]),
        ("count_of", count_of, [(([1, 2, 2, 2, 3], 2), 3), (([1, 2], 9), 0),
                                (([], 1), 0)]),
        ("insert_position", insert_position, [(([1, 3, 5], 4), 2), (([1, 3], 0), 0),
                                              (([1, 3], 9), 2), (([], 1), 0)]),
        ("exists", exists, [(([1, 3, 5], 3), True), (([1, 3], 2), False)]),
        ("closest", closest, [(([1, 4, 6], 5), 4), (([1, 4, 6], 6), 6),
                              (([5], 100), 5)]),
    ]),
    ("B. BOUNDS AND PREDICATES", [
        ("floor_value", floor_value, [(([1, 3, 5], 4), 3), (([1, 3, 5], 5), 5),
                                      (([1, 3], 0), None)]),
        ("ceil_value", ceil_value, [(([1, 3, 5], 4), 5), (([1, 3, 5], 1), 1),
                                    (([1, 3], 9), None)]),
        ("count_at_most", count_at_most, [(([1, 3, 5], 3), 2), (([1, 3], 0), 0),
                                          (([1, 3], 9), 2)]),
        ("first_true", first_true, [(([False, False, True, True],), 2),
                                    (([True],), 0), (([False, False],), -1)]),
        ("last_false", last_false, [(([False, False, True, True],), 1),
                                    (([True],), -1), (([False],), 0)]),
        ("sqrt_floor", sqrt_floor, [((8,), 2), ((9,), 3), ((0,), 0), ((1,), 1)]),
        ("peak_index", peak_index, [(([1, 3, 5, 4, 2],), 2), (([1, 2],), 1),
                                    (([5, 4],), 0)]),
        ("min_rotated", min_rotated, [(([4, 5, 6, 1, 2, 3],), 1), (([1, 2, 3],), 1),
                                      (([2, 1],), 1)]),
    ]),
    ("C. ROTATION, AND SEARCHING THE ANSWER", [
        ("rotation_count", rotation_count, [(([4, 5, 1, 2, 3],), 2), (([1, 2, 3],), 0)]),
        ("search_rotated", search_rotated, [(([4, 5, 6, 1, 2, 3], 2), 4),
                                            (([4, 5, 6, 1, 2, 3], 5), 1),
                                            (([4, 5, 6, 1, 2, 3], 9), -1)]),
        ("first_bad", first_bad, [((5, 4), 4), ((1, 1), 1), ((10, 1), 1)]),
        ("count_negatives", count_negatives, [(([5, 1, -2, -9],), 2), (([1, 2],), 0),
                                              (([-1, -2],), 2), (([],), 0)]),
        ("smallest_square_at_least", smallest_square_at_least,
         [((10,), 4), ((9,), 3), ((1,), 1), ((0,), 0)]),
        ("two_sum_bs", two_sum_bs, [(([1, 2, 4], 6), [1, 2]), (([1, 2], 9), []),
                                    (([1, 3], 4), [0, 1])]),
        ("min_capacity", min_capacity, [(([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5), 15),
                                        (([3, 2, 2, 4, 1, 4], 3), 6),
                                        (([1, 2, 3], 3), 3)]),
        ("min_speed", min_speed, [(([3, 6, 7, 11], 8), 4), (([30, 11, 23, 4, 20], 5), 30),
                                  (([1], 1), 1)]),
    ]),
]

if __name__ == "__main__":
    run(DRILLS)
