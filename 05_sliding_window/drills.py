"""
MODULE 05 DRILLS - sliding window, 24 reps.

A window is a run of CONSECUTIVE items. The whole idea is that when the window
moves one step you do not recompute it, you adjust: add what entered, subtract
what left. That is what turns O(n*k) into O(n).

Two kinds:

  FIXED     the width never changes. Add the entering item, remove the leaving
            one, every step.

  VARIABLE  the right edge always advances. The left edge advances only while
            the window is INVALID. The loop is: expand, then shrink while bad,
            then record.

RUN
    python 05_sliding_window/drills.py           everything
    python 05_sliding_window/drills.py 9         just drill 9
    python 05_sliding_window/drills.py longest   name contains "longest"
    python 05_sliding_window/drills.py -v        list passing drills too
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from drill_harness import run  # noqa: E402

VOWELS = "aeiou"


# ===========================================================================
# A. FIXED WIDTH
# ===========================================================================

# 1. Return the sum of every window of width k.
#    window_sums([1,2,3,4], 2) -> [3, 5, 7]
#    Build the first window with sum(). After that, each step is
#    total += nums[i] - nums[i - k]. Do not re-sum.
def window_sums(nums, k):
    raise NotImplementedError


# 2. Return the largest sum of any window of width k.
def max_sum_k(nums, k):
    raise NotImplementedError


# 3. Return the smallest sum of any window of width k.
def min_sum_k(nums, k):
    raise NotImplementedError


# 4. Return the largest AVERAGE of any window of width k, as a float.
#    max_avg_k([1,12,-5,-6,50,3], 4) -> 12.75
def max_avg_k(nums, k):
    raise NotImplementedError


# 5. Count the windows of width k whose sum is strictly greater than t.
def count_windows_above(nums, k, t):
    raise NotImplementedError


# 6. Return the start index of the first window of width k summing to target,
#    or -1.
def first_window_index(nums, k, target):
    raise NotImplementedError


# 7. Return the most vowels in any window of k characters.
#    max_vowels_k("abciiidef", 3) -> 3
#    Count vowels as they enter and uncount as they leave.
def max_vowels_k(s, k):
    raise NotImplementedError


# 8. Return the maximum of every window of width k.
#    window_maxes([1,3,2,5], 2) -> [3, 3, 5]
#    max() on each slice is fine here. The O(n) version needs a deque.
def window_maxes(nums, k):
    raise NotImplementedError


# ===========================================================================
# B. VARIABLE WIDTH
# ===========================================================================
#
# The shape of every one of these:
#
#     left = 0
#     for right in range(len(items)):
#         ...add items[right]...
#         while <window is invalid>:
#             ...remove items[left]...
#             left += 1
#         ...record the answer...

# 9. Length of the longest run with no repeated character.
#    longest_no_repeat("abcabcbb") -> 3
#    Keep a set of what is in the window. While the new character is already
#    inside, drop from the left.
def longest_no_repeat(s):
    raise NotImplementedError


# 10. Shortest run whose sum is at least target, 0 when impossible.
#     min_len_at_least([2,3,1,2,4,3], 7) -> 2       ([4,3])
#     All values are positive, which is what makes shrinking safe.
def min_len_at_least(nums, target):
    raise NotImplementedError


# 11. The list is 0s and 1s. Longest run of 1s if you may flip up to k zeros.
#     longest_ones([1,1,0,0,1,1,1,0], 2) -> 7
#     Count zeros in the window. Shrink while there are more than k.
def longest_ones(nums, k):
    raise NotImplementedError


# 12. Count the runs summing to exactly target. All values are positive.
#     count_subarrays_sum([1,2,3], 3) -> 2        ([1,2] and [3])
def count_subarrays_sum(nums, target):
    raise NotImplementedError


# 13. Length of the longest run with at most k distinct characters.
#     longest_k_distinct("eceba", 2) -> 3        ("ece")
#     Keep a count per character. Shrink while the dict has more than k keys,
#     and delete a key when its count hits zero.
def longest_k_distinct(s, k):
    raise NotImplementedError


# 14. Longest run containing at most TWO distinct values.
#     max_two_types([1,2,1,2,3]) -> 4
#     Drill 13 with k fixed at 2. Write it again anyway.
def max_two_types(nums):
    raise NotImplementedError


# 15. Length of the shortest window of s containing every character of
#     `needed` (counts matter), or 0 when there is none.
#     smallest_window("adobecodebanc", "abc") -> 4        ("banc")
def smallest_window(s, needed):
    raise NotImplementedError


# 16. Longest run of a single repeated character if you may change up to k
#     characters.  longest_after_replace("AABABBA", 1) -> 4
#     A window is valid while (width - count of its most common character) <= k.
def longest_after_replace(s, k):
    raise NotImplementedError


# 17. Longest run containing at most k odd numbers.
#     longest_k_odds([1,2,3,4,5], 2) -> 4
def longest_k_odds(nums, k):
    raise NotImplementedError


# 18. Longest run whose sum is at most t. All values are positive.
#     longest_sum_at_most([1,2,3], 3) -> 2
def longest_sum_at_most(nums, t):
    raise NotImplementedError


# ===========================================================================
# C. STRING WINDOWS
# ===========================================================================

# 19. Return every start index where an anagram of p begins in s.
#     anagram_indices("cbaebabacd", "abc") -> [0, 6]
#     A fixed window the width of p. Compare character counts each step.
def anagram_indices(s, p):
    raise NotImplementedError


# 20. Return True when some permutation of p appears as a run inside s.
def contains_permutation(s, p):
    raise NotImplementedError


# 21. Count the DISTINCT substrings of length k.
#     distinct_windows("abcabc", 3) -> 3        (abc, bca, cab)
def distinct_windows(s, k):
    raise NotImplementedError


# 22. Return every substring of length k, in order, duplicates included.
#     all_windows("abcd", 2) -> ["ab", "bc", "cd"]
def all_windows(s, k):
    raise NotImplementedError


# 23. Return the most distinct characters in any window of length k.
#     max_distinct_window("abcba", 3) -> 3
def max_distinct_window(s, k):
    raise NotImplementedError


# 24. Count the windows of length k whose characters are all different.
#     count_all_distinct_windows("abcabc", 3) -> 4
#     A string of length n has n - k + 1 windows of width k, so "abcabc" has
#     four: abc, bca, cab, abc. All four happen to qualify.
def count_all_distinct_windows(s, k):
    raise NotImplementedError


# --------------------------- tests: do not edit ---------------------------
DRILLS = [
    ("A. FIXED WIDTH", [
        ("window_sums", window_sums, [(([1, 2, 3, 4], 2), [3, 5, 7]),
                                      (([5], 1), [5]), (([1, 2], 3), [])]),
        ("max_sum_k", max_sum_k, [(([1, 2, 3, 4], 2), 7), (([5], 1), 5)]),
        ("min_sum_k", min_sum_k, [(([1, 2, 3, 4], 2), 3), (([5], 1), 5)]),
        ("max_avg_k", max_avg_k, [(([1, 12, -5, -6, 50, 3], 4), 12.75),
                                  (([1, 2], 2), 1.5)]),
        ("count_windows_above", count_windows_above, [(([1, 2, 3], 2, 3), 1),
                                                      (([1, 1], 2, 9), 0)]),
        ("first_window_index", first_window_index, [(([1, 2, 3, 4], 2, 5), 1),
                                                    (([1, 2], 2, 99), -1)]),
        ("max_vowels_k", max_vowels_k, [(("abciiidef", 3), 3), (("bcd", 2), 0)]),
        ("window_maxes", window_maxes, [(([1, 3, 2, 5], 2), [3, 3, 5]),
                                        (([4], 1), [4])]),
    ]),
    ("B. VARIABLE WIDTH", [
        ("longest_no_repeat", longest_no_repeat, [(("abcabcbb",), 3), (("bbb",), 1),
                                                  (("",), 0), (("pwwkew",), 3)]),
        ("min_len_at_least", min_len_at_least, [(([2, 3, 1, 2, 4, 3], 7), 2),
                                                (([1, 1], 9), 0), (([5], 5), 1)]),
        ("longest_ones", longest_ones, [(([1, 1, 0, 0, 1, 1, 1, 0], 2), 7),
                                        (([0, 0], 0), 0), (([1, 1], 0), 2)]),
        ("count_subarrays_sum", count_subarrays_sum, [(([1, 2, 3], 3), 2),
                                                      (([1, 1, 1], 2), 2),
                                                      (([5], 9), 0)]),
        ("longest_k_distinct", longest_k_distinct, [(("eceba", 2), 3),
                                                    (("aa", 1), 2), (("abc", 0), 0)]),
        ("max_two_types", max_two_types, [(([1, 2, 1, 2, 3],), 4), (([1],), 1),
                                          (([],), 0)]),
        ("smallest_window", smallest_window, [(("adobecodebanc", "abc"), 4),
                                              (("a", "aa"), 0), (("ab", "b"), 1)]),
        ("longest_after_replace", longest_after_replace, [(("AABABBA", 1), 4),
                                                          (("ABAB", 2), 4),
                                                          (("", 1), 0)]),
        ("longest_k_odds", longest_k_odds, [(([1, 2, 3, 4, 5], 2), 4),
                                            (([2, 4], 0), 2), (([1], 0), 0)]),
        ("longest_sum_at_most", longest_sum_at_most, [(([1, 2, 3], 3), 2),
                                                      (([5], 1), 0),
                                                      (([1, 1, 1], 9), 3)]),
    ]),
    ("C. STRING WINDOWS", [
        ("anagram_indices", anagram_indices, [(("cbaebabacd", "abc"), [0, 6]),
                                              (("abab", "ab"), [0, 1, 2]),
                                              (("a", "ab"), [])]),
        ("contains_permutation", contains_permutation, [(("eidbaooo", "ab"), True),
                                                        (("eidboaoo", "ab"), False)]),
        ("distinct_windows", distinct_windows, [(("abcabc", 3), 3), (("aaa", 2), 1),
                                                (("a", 5), 0)]),
        ("all_windows", all_windows, [(("abcd", 2), ["ab", "bc", "cd"]),
                                      (("a", 2), [])]),
        ("max_distinct_window", max_distinct_window, [(("abcba", 3), 3),
                                                      (("aaaa", 2), 1)]),
        ("count_all_distinct_windows", count_all_distinct_windows,
         [(("abcabc", 3), 4), (("aaa", 2), 0), (("ab", 1), 2)]),
    ]),
]

if __name__ == "__main__":
    run(DRILLS)
