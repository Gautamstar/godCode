"""
MODULE 02 DRILLS - hash maps and sets, 30 reps.

The highest-value module in the course. Most Easy problems that look like they
need a nested loop are really one pass plus a dict.

Some drills repeat things you did in module 00. That is deliberate. The
complement-lookup pattern in particular shows up here three times in three
disguises, because recognising it instantly is worth more than any single
solution.

RUN
    python 02_hashmaps_sets/drills.py           everything
    python 02_hashmaps_sets/drills.py 9         just drill 9
    python 02_hashmaps_sets/drills.py group     name contains "group"
    python 02_hashmaps_sets/drills.py -v        list passing drills too
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from drill_harness import run  # noqa: E402


# ===========================================================================
# A. COUNTING
# ===========================================================================

# 1. Map each item to how many times it appears.
#    The freq[x] = freq.get(x, 0) + 1 idiom. You will write this constantly.
def freq(items):
    raise NotImplementedError


# 2. Return the item that appears most often. On a tie return whichever was
#    seen first.  most_common(["a","b","a"]) -> "a"
#    Count first, then scan the ORIGINAL list to break ties by first sighting.
def most_common(items):
    raise NotImplementedError


# 3. Return how many distinct values the list holds.
def count_unique(items):
    raise NotImplementedError


# 4. Return the values appearing exactly once, sorted.
#    appears_once([1,2,2,3]) -> [1, 3]
def appears_once(items):
    raise NotImplementedError


# 5. Return True when both strings use the same letters the same number of
#    times. Build a count for each and compare. No sorting.
def same_letters(a, b):
    raise NotImplementedError


# 6. Return the value appearing more than half the time. Assume one exists.
#    majority([2,2,1]) -> 2
def majority(nums):
    raise NotImplementedError


# 7. Return {"even": count, "odd": count}.
def parity_counts(nums):
    raise NotImplementedError


# 8. Return the count of the rarest value. On a tie any of them gives the same
#    number, so just return the smallest count.
def rarest_count(items):
    raise NotImplementedError


# ===========================================================================
# B. COMPLEMENT AND LOOKUP
# ===========================================================================

# 9. Return the indices [i, j] of the two values summing to target.
#    Exactly one answer exists.  two_sum([2,7,11,15], 9) -> [0, 1]
#    Store value -> index as you go. Check for target - n BEFORE inserting n,
#    or a value can pair with itself.
def two_sum(nums, target):
    raise NotImplementedError


# 10. Return True when SOME pair sums to target. Same trick, simpler answer.
#     A set of seen values is enough here, no indices needed.
def has_pair_summing(nums, target):
    raise NotImplementedError


# 11. Return True when any value appears more than once.
def has_duplicate(nums):
    raise NotImplementedError


# 12. Return True when the same value appears twice within k indices of itself.
#     nearby_duplicate([1,2,1], 2) -> True     the two 1s are 2 apart
#     nearby_duplicate([1,2,1], 1) -> False
#     Keep value -> most recent index and compare the gap.
def nearby_duplicate(nums, k):
    raise NotImplementedError


# 13. Count the DISTINCT values x for which x + d also appears.
#     pairs_with_diff([1,2,3], 1) -> 2        (1 with 2, and 2 with 3)
#     Put everything in a set, then ask each value whether value + d is in it.
def pairs_with_diff(nums, d):
    raise NotImplementedError


# 14. Return True when some run of consecutive values sums to zero.
#     zero_subarray([1,-1,3]) -> True
#     Walk the running total. If the same total appears twice, everything
#     between those two points sums to zero. Seed the set with 0.
def zero_subarray(nums):
    raise NotImplementedError


# 15. Return the index of the first character appearing exactly once, or -1.
#     first_unique("aabc") -> 2
#     Count in one pass, then scan again in order and return the first with 1.
def first_unique(s):
    raise NotImplementedError


# ===========================================================================
# C. GROUPING
# ===========================================================================

# 16. Group words that are anagrams of each other.
#     Key each word by its sorted letters, which is identical for anagrams.
#     group_anagrams(["ant","tan","bee"]) -> {"ant": ["ant","tan"], "bee": ["bee"]}
#     Use the SORTED-LETTER STRING as the key: "".join(sorted(word)).
def group_anagrams(words):
    raise NotImplementedError


# 17. Group words by their length.  {2: ["ab"], 3: ["abc"]}
def group_by_length(words):
    raise NotImplementedError


# 18. Split into {"even": [...], "odd": [...]}, order preserved. Both keys must
#     exist even when one side is empty.
def group_by_parity(nums):
    raise NotImplementedError


# 19. Map each value to the FIRST index where it appears.
#     index_map(["a","b","a"]) -> {"a": 0, "b": 1}
def index_map(items):
    raise NotImplementedError


# 20. Flip a dict so each value maps to the sorted list of keys that had it.
#     invert_multi({"a": 1, "b": 1}) -> {1: ["a", "b"]}
def invert_multi(d):
    raise NotImplementedError


# 21. Count how many words start with each letter.  {"a": 2, "b": 1}
def count_by_first_letter(words):
    raise NotImplementedError


# 22. Collect scores per name from (name, score) rows, order preserved.
#     bucket([("a",1),("b",2),("a",3)]) -> {"a": [1, 3], "b": [2]}
def bucket(rows):
    raise NotImplementedError


# ===========================================================================
# D. SETS
# ===========================================================================

# 23. Values present in both lists, sorted, no repeats.
def intersect(a, b):
    raise NotImplementedError


# 24. Values in a but not in b, sorted, no repeats.
def subtract(a, b):
    raise NotImplementedError


# 25. Values in exactly one of the two lists, sorted.
#     Sets support ^ for symmetric difference.
def either_not_both(a, b):
    raise NotImplementedError


# 26. Return True when every value in a also appears in b.
#     Sets support <= for "is a subset of".
def is_subset(a, b):
    raise NotImplementedError


# 27. Return True when every character in s is distinct.
#     Compare the size of the set against the length of the string.
def all_distinct(s):
    raise NotImplementedError


# 28. One number from 0..n is missing from the list. Return it.
#     missing([0,1,3]) -> 2
#     A set lookup works. So does summing 0..n and subtracting.
def missing(nums):
    raise NotImplementedError


# 29. Values appearing in EVERY one of the given lists, sorted.
#     common_to_all([[1,2],[2,3]]) -> [2]        an empty input gives []
#     Start from the first list's set and intersect the rest into it.
def common_to_all(lists):
    raise NotImplementedError


# 30. Return the length of the longest run of CONSECUTIVE integers.
#     longest_run([100,4,200,1,3,2]) -> 4        (1,2,3,4)
#     Put everything in a set. Only start counting at a value whose value - 1
#     is absent, so each run is walked exactly once.
def longest_run(nums):
    raise NotImplementedError


# --------------------------- tests: do not edit ---------------------------
DRILLS = [
    ("A. COUNTING", [
        ("freq", freq, [((["a", "a", "b"],), {"a": 2, "b": 1}), (([],), {})]),
        ("most_common", most_common, [((["a", "b", "a"],), "a"),
                                      ((["x", "y"],), "x")]),
        ("count_unique", count_unique, [(([1, 1, 2],), 2), (([],), 0)]),
        ("appears_once", appears_once, [(([1, 2, 2, 3],), [1, 3]), (([1, 1],), [])]),
        ("same_letters", same_letters, [(("listen", "silent"), True),
                                        (("ab", "abb"), False)]),
        ("majority", majority, [(([2, 2, 1],), 2), (([5],), 5)]),
        ("parity_counts", parity_counts, [(([1, 2, 3],), {"even": 1, "odd": 2}),
                                          (([],), {"even": 0, "odd": 0})]),
        ("rarest_count", rarest_count, [((["a", "a", "b"],), 1), ((["a", "a"],), 2)]),
    ]),
    ("B. COMPLEMENT AND LOOKUP", [
        ("two_sum", two_sum, [(([2, 7, 11, 15], 9), [0, 1]), (([3, 2, 4], 6), [1, 2]),
                              (([3, 3], 6), [0, 1])]),
        ("has_pair_summing", has_pair_summing, [(([1, 2, 3], 5), True),
                                                (([1, 2], 9), False)]),
        ("has_duplicate", has_duplicate, [(([1, 2, 1],), True), (([1, 2],), False),
                                          (([],), False)]),
        ("nearby_duplicate", nearby_duplicate, [(([1, 2, 1], 2), True),
                                                (([1, 2, 1], 1), False),
                                                (([1, 2, 3], 3), False)]),
        ("pairs_with_diff", pairs_with_diff, [(([1, 2, 3], 1), 2), (([1, 5], 1), 0)]),
        ("zero_subarray", zero_subarray, [(([1, -1, 3],), True), (([1, 2],), False),
                                          (([3, -3],), True)]),
        ("first_unique", first_unique, [(("aabc",), 2), (("aa",), -1), (("abc",), 0)]),
    ]),
    ("C. GROUPING", [
        ("group_anagrams", group_anagrams,
         [((["ant", "tan", "bee"],), {"ant": ["ant", "tan"], "bee": ["bee"]}),
          (([],), {})]),
        ("group_by_length", group_by_length,
         [((["ab", "abc", "xy"],), {2: ["ab", "xy"], 3: ["abc"]}), (([],), {})]),
        ("group_by_parity", group_by_parity,
         [(([1, 2, 3],), {"even": [2], "odd": [1, 3]}),
          (([],), {"even": [], "odd": []})]),
        ("index_map", index_map, [((["a", "b", "a"],), {"a": 0, "b": 1}), (([],), {})]),
        ("invert_multi", invert_multi, [(({"a": 1, "b": 1},), {1: ["a", "b"]}),
                                        (({},), {})]),
        ("count_by_first_letter", count_by_first_letter,
         [((["ant", "ape", "bee"],), {"a": 2, "b": 1}), (([],), {})]),
        ("bucket", bucket, [(([("a", 1), ("b", 2), ("a", 3)],),
                             {"a": [1, 3], "b": [2]}), (([],), {})]),
    ]),
    ("D. SETS", [
        ("intersect", intersect, [(([1, 2, 3], [2, 3, 4]), [2, 3]), (([1], [9]), [])]),
        ("subtract", subtract, [(([1, 2, 3], [2]), [1, 3]), (([1], [1]), [])]),
        ("either_not_both", either_not_both, [(([1, 2], [2, 3]), [1, 3]),
                                              (([1], [1]), [])]),
        ("is_subset", is_subset, [(([1, 2], [1, 2, 3]), True), (([1, 9], [1, 2]), False),
                                  (([], [1]), True)]),
        ("all_distinct", all_distinct, [(("abc",), True), (("aba",), False),
                                        (("",), True)]),
        ("missing", missing, [(([0, 1, 3],), 2), (([1],), 0), (([0],), 1)]),
        ("common_to_all", common_to_all, [(([[1, 2], [2, 3]],), [2]),
                                          (([[1], [2]],), []), (([],), [])]),
        ("longest_run", longest_run, [(([100, 4, 200, 1, 3, 2],), 4), (([],), 0),
                                      (([5],), 1)]),
    ]),
]

if __name__ == "__main__":
    run(DRILLS)
