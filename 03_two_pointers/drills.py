"""
MODULE 03 DRILLS - two pointers, 26 reps.

Two shapes, and almost everything is one of them:

  CONVERGING    left starts at 0, right at the end, they move toward each
                other. Needs a SORTED list or a symmetric question.

  SAME DIRECTION  both start at 0. A `read` pointer scans, a `write` pointer
                marks where the next kept item goes. This is how you filter a
                list in place without building a new one.

RUN
    python 03_two_pointers/drills.py            everything
    python 03_two_pointers/drills.py 14         just drill 14
    python 03_two_pointers/drills.py sorted     name contains "sorted"
    python 03_two_pointers/drills.py -v         list passing drills too
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from drill_harness import run  # noqa: E402


# ===========================================================================
# A. CONVERGING FROM BOTH ENDS
# ===========================================================================

# 1. Reverse the list IN PLACE using two pointers. Return it.
#    left at 0, right at the end. Swap, step both inward, stop when they meet.
#    Do not use [::-1] or .reverse(); the loop is the drill.
def reverse_in_place(nums):
    raise NotImplementedError


# 2. Return True when s reads the same both ways, using two pointers.
#    Compare the ends and walk inward. No slicing.
def is_palindrome(s):
    raise NotImplementedError


# 3. The list is SORTED. Return the indices [i, j] of the pair summing to
#    target, or [] when there is none.  two_sum_sorted([1,2,4], 6) -> [1, 2]
#    Sum too small means the left pointer must rise. Too big means the right
#    must fall. That decision is the whole pattern.
def two_sum_sorted(nums, target):
    raise NotImplementedError


# 4. The list is SORTED. Return True when SOME pair sums to target.
def has_pair_sorted(nums, target):
    raise NotImplementedError


# 5. The list is SORTED and all values are DISTINCT. Count how many pairs sum
#    to target.  count_pairs_sorted([1,2,3,4], 5) -> 2      (1+4 and 2+3)
#    On a hit, move BOTH pointers inward. Moving only one would find the same
#    pair again from the other side.
def count_pairs_sorted(nums, target):
    raise NotImplementedError


# 6. Return True when s is a palindrome, ignoring case and anything that is
#    not a letter or digit.  "A man, a plan" is not, "aba!" is.
#    Skip bad characters by advancing the pointer without comparing.
def is_clean_palindrome(s):
    raise NotImplementedError


# 7. Reverse only the vowels, leaving everything else in place.
#    reverse_vowels("hello") -> "holle"
#    Convert to a list, walk both ends, swap only when BOTH sides are vowels.
def reverse_vowels(s):
    raise NotImplementedError


# 8. Two vertical lines at index i and j hold water of height min(h[i], h[j])
#    and width j - i. Return the largest area.
#    max_water([1,8,6,2,5,4,8,3,7]) -> 49
#    Start wide. Moving the taller line inward can never help, so always move
#    the shorter one.
def max_water(heights):
    raise NotImplementedError


# 9. The list is SORTED. Return the sum of the pair closest to target.
#    closest_sum([1,3,6], 7) -> 7        (1 + 6)
def closest_sum(nums, target):
    raise NotImplementedError


# ===========================================================================
# B. SAME DIRECTION: READ AND WRITE POINTERS
# ===========================================================================

# 10. Remove every occurrence of `value` IN PLACE. Return the new length, and
#     leave the first `length` slots holding the kept items.
#     A read pointer scans; a write pointer only advances when you keep one.
def remove_value(nums, value):
    raise NotImplementedError


# 11. The list is SORTED. Remove duplicates IN PLACE, return the new length.
#     Compare each item to the last one you WROTE, not to its neighbour.
def dedupe_sorted(nums):
    raise NotImplementedError


# 12. Move every zero to the end IN PLACE, keeping the order of the rest.
#     Return the list. Write the non-zeros forward, then fill the tail.
def move_zeros(nums):
    raise NotImplementedError


# 13. Merge two SORTED lists into one sorted list.
#     One pointer per list. Take the smaller head, advance that pointer, and
#     when one runs out append whatever is left of the other.
def merge_sorted(a, b):
    raise NotImplementedError


# 14. Reorder so every even number comes before every odd one. Within each
#     group keep the original order.  partition([1,2,3,4]) -> [2, 4, 1, 3]
def partition_even_first(nums):
    raise NotImplementedError


# 15. The list is SORTED and may contain negatives. Return the SQUARES in
#     sorted order.  sorted_squares([-4,-1,0,3]) -> [0, 1, 9, 16]
#     The largest square is always at one end. Fill the answer back to front.
def sorted_squares(nums):
    raise NotImplementedError


# 16. Both lists are SORTED. Return the values present in both, sorted, with
#     duplicates collapsed.  Walk both with one pointer each.
def intersect_sorted(a, b):
    raise NotImplementedError


# 17. Return True when every character of `small` appears in `big` in order,
#     not necessarily adjacent.  is_subsequence("ace","abcde") -> True
#     One pointer per string. Advance the small one only on a match.
def is_subsequence(small, big):
    raise NotImplementedError


# 18. Collapse runs of the same adjacent value down to one.
#     compact([1,1,2,2,1]) -> [1, 2, 1]        note the final 1 survives
def compact(nums):
    raise NotImplementedError


# ===========================================================================
# C. SCANNING WITH TWO CURSORS
# ===========================================================================

# 19. Return the middle item using a slow and a fast pointer. The fast one
#     moves two steps for every one of the slow one, so when fast reaches the
#     end slow is halfway. Odd lengths only.
def middle_slow_fast(nums):
    raise NotImplementedError


# 20. Return the nth item counting from the END, 1-based.
#     nth_from_end([1,2,3], 1) -> 3
#     Advance one pointer n steps first, then move both until it hits the end.
def nth_from_end(nums, n):
    raise NotImplementedError


# 21. Return the length of the longest run of the same repeated value.
#     longest_run([1,1,2,2,2]) -> 3
def longest_run(nums):
    raise NotImplementedError


# 22. The list is SORTED. Return the smallest gap between any two values.
#     Adjacent values in a sorted list are always the closest pair.
def min_gap_sorted(nums):
    raise NotImplementedError


# 23. The list is SORTED. Count the distinct values without using set().
def count_distinct_sorted(nums):
    raise NotImplementedError


# 24. Merge overlapping (start, end) intervals. The input is sorted by start.
#     merge_intervals([(1,3),(2,6),(8,10)]) -> [(1, 6), (8, 10)]
#     Keep the last interval you produced and extend it when the next overlaps.
def merge_intervals(intervals):
    raise NotImplementedError


# 25. Return True when the two lists become equal after applying backspaces,
#     where "#" deletes the character before it.
#     backspace_equal("ab#c", "ad#c") -> True
#     Build each result with a write pointer, stepping it BACK on a "#".
def backspace_equal(a, b):
    raise NotImplementedError


# 26. Return the values from `nums` that appear strictly more than once,
#     sorted, using a sorted copy and two pointers rather than a dict.
def repeats_sorted(nums):
    raise NotImplementedError


# --------------------------- tests: do not edit ---------------------------
DRILLS = [
    ("A. CONVERGING FROM BOTH ENDS", [
        ("reverse_in_place", reverse_in_place, [(([1, 2, 3],), [3, 2, 1]), (([],), [])]),
        ("is_palindrome", is_palindrome, [(("aba",), True), (("ab",), False),
                                          (("",), True)]),
        ("two_sum_sorted", two_sum_sorted, [(([1, 2, 4], 6), [1, 2]),
                                            (([1, 2], 9), []), (([1, 3], 4), [0, 1])]),
        ("has_pair_sorted", has_pair_sorted, [(([1, 2, 4], 6), True),
                                              (([1, 2], 9), False)]),
        ("count_pairs_sorted", count_pairs_sorted, [(([1, 2, 3, 4], 5), 2),
                                                    (([1, 2, 3], 4), 1),
                                                    (([1, 2], 9), 0)]),
        ("is_clean_palindrome", is_clean_palindrome, [(("aba!",), True),
                                                      (("A man, a plan",), False),
                                                      (("Ab, ba",), True)]),
        ("reverse_vowels", reverse_vowels, [(("hello",), "holle"), (("xyz",), "xyz")]),
        ("max_water", max_water, [(([1, 8, 6, 2, 5, 4, 8, 3, 7],), 49),
                                  (([1, 1],), 1)]),
        ("closest_sum", closest_sum, [(([1, 3, 6], 7), 7), (([1, 2], 100), 3)]),
    ]),
    ("B. SAME DIRECTION: READ AND WRITE POINTERS", [
        ("remove_value", remove_value, [(([3, 2, 3], 3), 1), (([1, 2], 9), 2),
                                        (([], 1), 0)]),
        ("dedupe_sorted", dedupe_sorted, [(([1, 1, 2],), 2), (([1, 2, 3],), 3),
                                          (([],), 0)]),
        ("move_zeros", move_zeros, [(([0, 1, 0, 2],), [1, 2, 0, 0]),
                                    (([1, 2],), [1, 2])]),
        ("merge_sorted", merge_sorted, [(([1, 3], [2, 4]), [1, 2, 3, 4]),
                                        (([], [1]), [1]), (([], []), [])]),
        ("partition_even_first", partition_even_first,
         [(([1, 2, 3, 4],), [2, 4, 1, 3]), (([1, 3],), [1, 3])]),
        ("sorted_squares", sorted_squares, [(([-4, -1, 0, 3],), [0, 1, 9, 16]),
                                            (([1, 2],), [1, 4]), (([],), [])]),
        ("intersect_sorted", intersect_sorted, [(([1, 2, 3], [2, 3, 4]), [2, 3]),
                                                (([1], [9]), []),
                                                (([1, 1, 2], [1, 2]), [1, 2])]),
        ("is_subsequence", is_subsequence, [(("ace", "abcde"), True),
                                            (("aec", "abcde"), False),
                                            (("", "abc"), True)]),
        ("compact", compact, [(([1, 1, 2, 2, 1],), [1, 2, 1]), (([],), [])]),
    ]),
    ("C. SCANNING WITH TWO CURSORS", [
        ("middle_slow_fast", middle_slow_fast, [(([1, 2, 3],), 2), (([5],), 5),
                                                (([1, 2, 3, 4, 5],), 3)]),
        ("nth_from_end", nth_from_end, [(([1, 2, 3], 1), 3), (([1, 2, 3], 3), 1)]),
        ("longest_run", longest_run, [(([1, 1, 2, 2, 2],), 3), (([1],), 1),
                                      (([],), 0)]),
        ("min_gap_sorted", min_gap_sorted, [(([1, 5, 6],), 1), (([1, 10],), 9)]),
        ("count_distinct_sorted", count_distinct_sorted, [(([1, 1, 2, 3],), 3),
                                                          (([],), 0)]),
        ("merge_intervals", merge_intervals,
         [(([(1, 3), (2, 6), (8, 10)],), [(1, 6), (8, 10)]),
          (([(1, 2)],), [(1, 2)]), (([],), [])]),
        ("backspace_equal", backspace_equal, [(("ab#c", "ad#c"), True),
                                              (("a#c", "b"), False),
                                              (("###", ""), True)]),
        ("repeats_sorted", repeats_sorted, [(([1, 2, 1, 3, 2],), [1, 2]),
                                            (([1, 2],), [])]),
    ]),
]

if __name__ == "__main__":
    run(DRILLS)
