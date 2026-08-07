"""
MODULE 01 DRILLS - arrays and strings, 30 reps.

Read LESSON.md first. These sit between the module 00 syntax drills and the
problems/ folder: still small, but now every one has an idea behind it.

RUN
    python 01_arrays_strings/drills.py          everything
    python 01_arrays_strings/drills.py 12       just drill 12
    python 01_arrays_strings/drills.py 1-10     a range
    python 01_arrays_strings/drills.py prefix   name contains "prefix"
    python 01_arrays_strings/drills.py -v       list passing drills too

Never modify a list you were handed unless the drill says to. Returning a new
list is the default.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from drill_harness import run  # noqa: E402


# ===========================================================================
# A. INDEX ARITHMETIC
# ===========================================================================

# 1. Sum the values from index i to index j INCLUSIVE.
#    sum_range([1,2,3,4], 1, 2) -> 5
#    Python slices exclude the end, so the slice you want ends at j + 1.
def sum_range(nums, i, j):
    raise NotImplementedError


# 2. Return a NEW list with positions i and j swapped.
#    Copy first with list(nums) or nums[:], then assign both.
def swapped(nums, i, j):
    raise NotImplementedError


# 3. Shift every item one place left, the first wrapping to the end.
#    rotate_left([1,2,3]) -> [2, 3, 1]        slicing does this in one line
def rotate_left(nums):
    raise NotImplementedError


# 4. Shift every item one place right, the last wrapping to the front.
#    rotate_right([1,2,3]) -> [3, 1, 2]
def rotate_right(nums):
    raise NotImplementedError


# 5. Rotate left by k places.  rotate_left_k([1,2,3,4], 2) -> [3, 4, 1, 2]
#    k can exceed the length, so reduce it with % len first. Guard the empty list.
def rotate_left_k(nums, k):
    raise NotImplementedError


# 6. Return the index of the LAST occurrence of target, or -1.
#    Walk backwards with range(len(nums) - 1, -1, -1).
def last_index_of(nums, target):
    raise NotImplementedError


# 7. Return the second largest DISTINCT value, or None when there isn't one.
#    [3, 1, 3] has only two distinct values, so the answer is 1.
def second_largest(nums):
    raise NotImplementedError


# 8. Return True when the list reads the same forwards and backwards.
def is_palindrome_list(nums):
    raise NotImplementedError


# ===========================================================================
# B. BUILDING NEW LISTS
# ===========================================================================

# 9. Return a new list with every occurrence of `value` removed.
def without(nums, value):
    raise NotImplementedError


# 10. Return a new list where every negative becomes 0.
#     A conditional expression inside a comprehension: n if n > 0 else 0
def clamp_negatives(nums):
    raise NotImplementedError


# 11. Move every zero to the end, keeping the order of everything else.
#     move_zeros([0,1,0,2]) -> [1, 2, 0, 0]
#     Collect the non-zeros, then pad with the zeros you counted.
def move_zeros(nums):
    raise NotImplementedError


# 12. Remove duplicates but KEEP the original order.
#     dedupe([3,1,3,2]) -> [3, 1, 2]        sorted(set(...)) would lose the order
def dedupe(nums):
    raise NotImplementedError


# 13. Interleave two equal-length lists.
#     interleave([1,3],[2,4]) -> [1, 2, 3, 4]
def interleave(a, b):
    raise NotImplementedError


# 14. Split into consecutive chunks of `size`. The last chunk may be short.
#     chunk([1,2,3,4,5], 2) -> [[1,2],[3,4],[5]]
#     range(0, len(nums), size) walks the start of each chunk.
def chunk(nums, size):
    raise NotImplementedError


# 15. Reverse the list IN PLACE and return it. The caller's list must change.
#     Swap from both ends inward, or use .reverse(). Do not use [::-1], which
#     builds a copy and leaves the original alone.
def reverse_in_place(nums):
    raise NotImplementedError


# 16. Return the list with each item repeated twice, in order.
#     doubled([1,2]) -> [1, 1, 2, 2]
def doubled(nums):
    raise NotImplementedError


# ===========================================================================
# C. PREFIX SUMS AND RUNNING VALUES
# ===========================================================================

# 17. Return the running total at each position.
#     prefix_sums([1,2,3]) -> [1, 3, 6]
#     This is the setup for answering "sum between i and j" instantly.
def prefix_sums(nums):
    raise NotImplementedError


# 18. Answer a range-sum query USING a prefix-sum list you build first.
#     range_sum([1,2,3,4], 1, 2) -> 5
#     With prefix p, the sum from i to j is p[j] - p[i-1], and just p[j] when
#     i is 0. That is the whole trick: O(1) per query after one pass.
def range_sum(nums, i, j):
    raise NotImplementedError


# 19. Return the largest value seen so far at each position.
#     running_max([1,3,2,5]) -> [1, 3, 3, 5]
def running_max(nums):
    raise NotImplementedError


# 20. Return the average as a float. An empty list gives 0.0.
def average(nums):
    raise NotImplementedError


# 21. Return how many values are strictly less than k.
def count_below(nums, k):
    raise NotImplementedError


# 22. Return the index where the sum to the left equals the sum to the right,
#     or -1. The pivot itself belongs to neither side.
#     pivot_index([1,7,3,6,5,6]) -> 3
#     Keep a left total and derive the right from the grand total.
def pivot_index(nums):
    raise NotImplementedError


# ===========================================================================
# D. STRINGS
# ===========================================================================

# 23. Reverse the ORDER of the words, not the letters.
#     reverse_words("a b c") -> "c b a"
def reverse_words(s):
    raise NotImplementedError


# 24. Uppercase the first letter of every word, lowercase the rest.
#     title_case("hi there") -> "Hi There"
def title_case(s):
    raise NotImplementedError


# 25. Return True when s reads the same both ways, ignoring case.
def is_palindrome(s):
    raise NotImplementedError


# 26. Return the longest word. On a tie return the one that appears first.
def longest_word(s):
    raise NotImplementedError


# 27. Return the string with every vowel removed. Treat aeiou, lowercase only.
def strip_vowels(s):
    raise NotImplementedError


# 28. Map each character to a list of the positions where it appears.
#     positions("aba") -> {"a": [0, 2], "b": [1]}
def positions(s):
    raise NotImplementedError


# 29. Compress runs of repeats into character + count.
#     compress("aaabb") -> "a3b2",  compress("abc") -> "a1b1c1"
#     Walk once, comparing each character to the previous one.
def compress(s):
    raise NotImplementedError


# 30. Return True when the two strings use exactly the same letters.
#     is_anagram("listen","silent") -> True
#     Sorting both is the one-liner. Counting both is the O(n) version.
def is_anagram(a, b):
    raise NotImplementedError


# --------------------------- tests: do not edit ---------------------------
DRILLS = [
    ("A. INDEX ARITHMETIC", [
        ("sum_range", sum_range, [(([1, 2, 3, 4], 1, 2), 5), (([5], 0, 0), 5)]),
        ("swapped", swapped, [(([1, 2, 3], 0, 2), [3, 2, 1]), (([1, 2], 0, 1), [2, 1])]),
        ("rotate_left", rotate_left, [(([1, 2, 3],), [2, 3, 1]), (([1],), [1])]),
        ("rotate_right", rotate_right, [(([1, 2, 3],), [3, 1, 2]), (([1],), [1])]),
        ("rotate_left_k", rotate_left_k, [(([1, 2, 3, 4], 2), [3, 4, 1, 2]),
                                          (([1, 2, 3], 4), [2, 3, 1]), (([], 2), [])]),
        ("last_index_of", last_index_of, [(([1, 2, 1], 1), 2), (([1], 9), -1)]),
        ("second_largest", second_largest, [(([3, 1, 3],), 1), (([5],), None),
                                            (([1, 2, 3],), 2)]),
        ("is_palindrome_list", is_palindrome_list, [(([1, 2, 1],), True),
                                                    (([1, 2],), False), (([],), True)]),
    ]),
    ("B. BUILDING NEW LISTS", [
        ("without", without, [(([1, 2, 1], 1), [2]), (([1], 9), [1])]),
        ("clamp_negatives", clamp_negatives, [(([-1, 2, -3],), [0, 2, 0]), (([],), [])]),
        ("move_zeros", move_zeros, [(([0, 1, 0, 2],), [1, 2, 0, 0]), (([1, 2],), [1, 2])]),
        ("dedupe", dedupe, [(([3, 1, 3, 2],), [3, 1, 2]), (([],), [])]),
        ("interleave", interleave, [(([1, 3], [2, 4]), [1, 2, 3, 4]), (([], []), [])]),
        ("chunk", chunk, [(([1, 2, 3, 4, 5], 2), [[1, 2], [3, 4], [5]]),
                          (([1, 2], 5), [[1, 2]]), (([], 2), [])]),
        ("reverse_in_place", reverse_in_place, [(([1, 2, 3],), [3, 2, 1]), (([],), [])]),
        ("doubled", doubled, [(([1, 2],), [1, 1, 2, 2]), (([],), [])]),
    ]),
    ("C. PREFIX SUMS AND RUNNING VALUES", [
        ("prefix_sums", prefix_sums, [(([1, 2, 3],), [1, 3, 6]), (([],), [])]),
        ("range_sum", range_sum, [(([1, 2, 3, 4], 1, 2), 5), (([1, 2, 3], 0, 2), 6),
                                  (([4], 0, 0), 4)]),
        ("running_max", running_max, [(([1, 3, 2, 5],), [1, 3, 3, 5]), (([],), [])]),
        ("average", average, [(([1, 2, 3],), 2.0), (([],), 0.0)]),
        ("count_below", count_below, [(([1, 5, 3], 4), 2), (([], 1), 0)]),
        ("pivot_index", pivot_index, [(([1, 7, 3, 6, 5, 6],), 3), (([1, 2, 3],), -1),
                                      (([2, 1, -1],), 0)]),
    ]),
    ("D. STRINGS", [
        ("reverse_words", reverse_words, [(("a b c",), "c b a"), (("hi",), "hi")]),
        ("title_case", title_case, [(("hi there",), "Hi There"), (("aB",), "Ab")]),
        ("is_palindrome", is_palindrome, [(("Racecar",), True), (("abc",), False)]),
        ("longest_word", longest_word, [(("a bbb cc",), "bbb"), (("aa bb",), "aa")]),
        ("strip_vowels", strip_vowels, [(("hello",), "hll"), (("xyz",), "xyz")]),
        ("positions", positions, [(("aba",), {"a": [0, 2], "b": [1]}), (("",), {})]),
        ("compress", compress, [(("aaabb",), "a3b2"), (("abc",), "a1b1c1"), (("",), "")]),
        ("is_anagram", is_anagram, [(("listen", "silent"), True), (("ab", "abc"), False)]),
    ]),
]

if __name__ == "__main__":
    run(DRILLS)
