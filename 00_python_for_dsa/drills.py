"""
MODULE 00 DRILLS - pure Python reps, no algorithms yet.

80 drills, eight sections, difficulty climbing slowly. These are the syntax
reflexes every later module depends on. Volume is the point: do them, then do
them again next week from a blank file.

RUN
    python 00_python_for_dsa/drills.py          everything
    python 00_python_for_dsa/drills.py 34       just drill 34
    python 00_python_for_dsa/drills.py 30-40    a range
    python 00_python_for_dsa/drills.py dict     name contains "dict"
    python 00_python_for_dsa/drills.py -v       list passing drills too

Finished drills are counted, not printed, so the ones you are working on stay
visible. The footer tells you which drill to do next.

Drills marked ALREADY DONE are yours from the first pass. Left in place.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from drill_harness import run  # noqa: E402


# ===========================================================================
# A. NUMBERS AND OPERATORS
# ===========================================================================

# 1. Return a + b.
def add(a, b):
    return a + b


# 2. Return how many whole times b fits into a.  whole_divide(7, 2) -> 3
#    Use // (floor division). Plain / gives 3.5, a float.
def whole_divide(a, b):
    return a // b


# 3. Return the remainder of a divided by b.  remainder(7, 2) -> 1
#    The % operator. This is how you test divisibility and wrap around.
def remainder(a, b):
    return a % b


# 4. Return a raised to the power b.  power(2, 3) -> 8
def power(a, b):
    return a ** b


# 5. Return True when n is even.
#    n % 2 == 0 is already True or False, so no if statement is needed.
def is_even(n):
    return n % 2 == 0

# 6. Return the distance of n from zero.  distance(-4) -> 4
def distance(n):
    return abs(n)


# 7. Return n as a whole number, throwing away the decimal part.
#    to_int(3.9) -> 3      int() truncates toward zero, it does not round.
def to_int(n):
    return int(n)


# 8. Return the smaller of a and b WITHOUT using min().
#    An if/else with two returns is the clearest way.
def smaller(a, b):
    if a > b:
        return b
    else:
        return a

# ===========================================================================
# B. STRINGS
# ===========================================================================

# 9. Return the string in uppercase.
def shout(s):
    raise NotImplementedError


# 10. Return the string in lowercase.
def whisper(s):
    raise NotImplementedError


# 11. Return the first character.  Strings index exactly like lists.
def first_char(s):
    raise NotImplementedError


# 12. Return the last character. Use a negative index, not len(s) - 1.
def last_char(s):
    raise NotImplementedError


# 13. Return how many characters the string has.
def char_count(s):
    raise NotImplementedError


# 14. Return the string reversed.  reverse_string("abc") -> "cba"
#     Slice with a step of -1.
def reverse_string(s):
    raise NotImplementedError


# 15. Return True when `part` appears anywhere inside s.
#     The `in` operator works on strings, not just lists.
def contains(s, part):
    raise NotImplementedError


# 16. Return True when s begins with `part`.  There is a string method for this.
def starts_with(s, part):
    raise NotImplementedError


# 17. Return s with leading and trailing whitespace removed.
#     strip() only touches the ends, never the middle.
def trim(s):
    raise NotImplementedError


# 18. Split a sentence into a list of words.  split_words("a b") -> ["a", "b"]
#     .split() with no argument splits on any run of whitespace.
def split_words(s):
    raise NotImplementedError


# 19. ALREADY DONE. Join the words with a dash:  ["a","b"] -> "a-b"
def join_words(words):
    new_woreds = "-".join(words)
    return new_woreds


# 20. ALREADY DONE. Return only the digit characters from s.  "a1b2" -> "12"
def only_digits(s):
    strs = "".join([i for i in s if i.isdigit()])
    return strs


# 21. Return how many times `ch` appears in s. There is a string method for it.
def count_char(s, ch):
    raise NotImplementedError


# 22. Return s with every occurrence of `old` swapped for `new`.
def replace_all(s, old, new):
    raise NotImplementedError


# ===========================================================================
# C. LISTS: INDEXING AND SLICING
# ===========================================================================

# 23. ALREADY DONE. Return the LAST element.
def last_element(nums):
    return nums[-1]


# 24. ALREADY DONE. Return the first three items.
def first_three(nums):
    return nums[0:3]


# 25. ALREADY DONE. Return the list reversed.
def reverse_list(items):
    return items[::-1]


# 26. Return the last TWO items.  last_two([1,2,3,4]) -> [3, 4]
#     A negative start with no end: nums[-2:]
def last_two(nums):
    raise NotImplementedError


# 27. Return everything EXCEPT the first item.  drop_first([1,2,3]) -> [2, 3]
def drop_first(nums):
    raise NotImplementedError


# 28. Return every other item, starting from the first.
#     every_other([1,2,3,4,5]) -> [1, 3, 5]        slice with a step of 2
def every_other(nums):
    raise NotImplementedError


# 29. Return the middle item of an odd-length list.  middle([1,2,3]) -> 2
#     Index len // 2.
def middle(nums):
    raise NotImplementedError


# 30. Return how many items the list holds.
def size(nums):
    raise NotImplementedError


# 31. Return a NEW list with `item` added on the end. Do not modify the input.
#     nums + [item] builds a new list. nums.append(item) mutates and returns None.
def with_added(nums, item):
    raise NotImplementedError


# 32. Return the two lists joined end to end.
def concat(a, b):
    raise NotImplementedError


# 33. Return True when `target` is somewhere in the list.
def has(nums, target):
    raise NotImplementedError


# 34. Return the position of `target`, or -1 when it is absent.
#     .index() raises when it is missing, so check with `in` first.
def position_of(nums, target):
    raise NotImplementedError


# ===========================================================================
# D. LOOPS AND CONDITIONALS
# ===========================================================================

# 35. Return the total of every number, using a loop rather than sum().
#     Start an accumulator at 0, add each item, return it. This is the shape
#     of nearly every counting algorithm you will write.
def total(nums):
    raise NotImplementedError


# 36. Return how many numbers are greater than zero.
def count_positive(nums):
    raise NotImplementedError


# 37. ALREADY DONE. Return the INDEX of the largest number.
def index_of_max(nums):
    max_num = max(enumerate(nums), key=lambda x: x[1])
    return max_num[0]


# 38. Return the first negative number, or None when there is none.
#     Return as soon as you find it. Do not scan the rest.
def first_negative(nums):
    raise NotImplementedError


# 39. Return True when EVERY number is even.  An empty list counts as True.
#     Write the loop first. Once it works, try the one-liner with all().
def all_even(nums):
    raise NotImplementedError


# 40. Return True when AT LEAST ONE number is negative.
def any_negative(nums):
    raise NotImplementedError


# 41. Return the largest number WITHOUT using max().
#     Track a best-so-far. Assume the list is not empty.
def largest(nums):
    raise NotImplementedError


# 42. Return a running total at each position.
#     running([1,2,3]) -> [1, 3, 6]        keep a total, append after each add
def running(nums):
    raise NotImplementedError


# 43. Return "fizz" when n divides by 3, "buzz" when by 5, "fizzbuzz" when by
#     both, otherwise the number as a string. Check both FIRST.
def fizz(n):
    raise NotImplementedError


# 44. Return "negative", "zero", or "positive" for n.
def sign_word(n):
    raise NotImplementedError


# ===========================================================================
# E. DICTS AND SETS
# ===========================================================================

# 45. ALREADY DONE. Map each item to how many times it appears.
def count_items(items):
    freq = {}
    for i in items:
        freq[i] = freq.get(i, 0) + 1
    return freq


# 46. ALREADY DONE. Return the sorted unique values.
def unique_sorted(items):
    seen = sorted(set(items))
    return seen


# 47. Return the value for `key`, or `fallback` when the key is absent.
#     d.get(key, fallback) does this in one call and never raises.
def lookup(d, key, fallback):
    raise NotImplementedError


# 48. Return True when `key` exists in the dict.
#     `in` on a dict checks the KEYS, not the values.
def has_key(d, key):
    raise NotImplementedError


# 49. Return the dict's keys as a sorted list.
def sorted_keys(d):
    raise NotImplementedError


# 50. Return the sum of the dict's values.
def sum_values(d):
    raise NotImplementedError


# 51. Flip a dict so values become keys.  {"a": 1} -> {1: "a"}
#     Loop over d.items().
def invert(d):
    raise NotImplementedError


# 52. Return the key with the largest value.  {"a":1,"b":9} -> "b"
#     max(d, key=d.get) is the idiom. A loop is fine too.
def top_key(d):
    raise NotImplementedError


# 53. Return the values present in BOTH lists, sorted, no repeats.
#     Convert both to sets and use & (intersection).
def in_both(a, b):
    raise NotImplementedError


# 54. Return the values in `a` that are NOT in `b`, sorted, no repeats.
#     Sets support - (difference).
def only_in_first(a, b):
    raise NotImplementedError


# 55. Return every distinct value across both lists, sorted.  Sets support |.
def in_either(a, b):
    raise NotImplementedError


# 56. Return the first value that appears twice, or None.
#     Keep a `seen` set. Check membership BEFORE adding. This one pattern
#     solves a surprising number of Easy problems.
def first_repeat(nums):
    raise NotImplementedError


# 57. Return the indices [i, j] of the two numbers summing to target.
#     Exactly one answer exists.  two_sum([2,7,11,15], 9) -> [0, 1]
#     Store value -> index as you go, and look for target - n before inserting.
#     This is the single most important pattern in the whole course.
def two_sum(nums, target):
    raise NotImplementedError


# 58. Group words by their first letter.
#     group(["ant","ape","bee"]) -> {"a": ["ant","ape"], "b": ["bee"]}
#     Create the bucket on first sighting: if key not in out: out[key] = []
def group_by_first(words):
    raise NotImplementedError


# ===========================================================================
# F. COMPREHENSIONS
# ===========================================================================

# 59. ALREADY DONE. Every EVEN number doubled, odds dropped.
def doubled_evens(nums):
    return [i * 2 for i in nums if i % 2 == 0]


# 60. Return each number squared.
def squares(nums):
    raise NotImplementedError


# 61. Return only the words longer than 3 characters.
def long_words(words):
    raise NotImplementedError


# 62. Return the length of each word.  lengths(["ab","c"]) -> [2, 1]
def lengths(words):
    raise NotImplementedError


# 63. Flatten a list of lists.  flatten([[1,2],[3]]) -> [1, 2, 3]
#     Two `for` clauses in one comprehension, outer first.
def flatten(rows):
    raise NotImplementedError


# 64. Map each word to its length as a DICT.  {"ab": 2, "c": 1}
#     A dict comprehension uses braces and a key: value pair.
def length_map(words):
    raise NotImplementedError


# 65. Return the distinct first letters as a SET.
#     A set comprehension uses braces with no colon.
def first_letters(words):
    raise NotImplementedError


# 66. ALREADY DONE. Pairwise sums of two equal-length lists.
def sum_two_lists(a, b):
    sums = [x + y for x, y in zip(a, b)]
    return sums


# 67. Return each word uppercased.
def upper_all(words):
    raise NotImplementedError


# 68. Return (index, value) pairs as a list of tuples.
#     pairs(["a","b"]) -> [(0, "a"), (1, "b")]       enumerate gives you both
def pairs(items):
    raise NotImplementedError


# ===========================================================================
# G. TUPLES, UNPACKING, FUNCTIONS
# ===========================================================================

# 69. ALREADY DONE. Return the two values swapped, as a tuple.
def swap(a, b):
    swapped = (b, a)
    return swapped


# 70. Return (smallest, largest) as a tuple.
def min_and_max(nums):
    raise NotImplementedError


# 71. Return a - b, where `pair` is a two-slot tuple.  Unpack it first:
#     a, b = pair
def difference(pair):
    raise NotImplementedError


# 72. Add up any number of arguments.  add_all(1, 2, 3) -> 6
#     A *args parameter collects them into a tuple.
def add_all(*nums):
    raise NotImplementedError


# 73. Return a repeated `times` times, joined by spaces. `times` DEFAULTS to 2.
#     repeat("hi") -> "hi hi"      A default is written in the signature.
def repeat(word, times=2):
    raise NotImplementedError


# 74. Build a dict from two equal-length lists of keys and values.
#     zip_dict(["a"], [1]) -> {"a": 1}        dict(zip(...)) does it in one call
def zip_dict(keys, values):
    raise NotImplementedError


# ===========================================================================
# H. SORTING
# ===========================================================================

# 75. ALREADY DONE. Sort largest to smallest.
def sort_desc(nums):
    return sorted(nums, reverse=True)


# 76. Sort the words by LENGTH, shortest first.
#     sorted(words, key=len). The key function decides what to compare by.
def by_length(words):
    raise NotImplementedError


# 77. Sort a list of (name, score) tuples by score, highest first.
#     key=lambda pair: pair[1], and reverse=True.
def by_score(rows):
    raise NotImplementedError


# 78. Sort words alphabetically, ignoring case.
#     by_alpha(["b","A"]) -> ["A", "b"]        key=str.lower
def by_alpha(words):
    raise NotImplementedError


# 79. Return the k largest numbers, largest first.
def top_k(nums, k):
    raise NotImplementedError


# 80. Sort a dict's keys by their value, smallest value first.
#     sort_keys_by_value({"a": 3, "b": 1}) -> ["b", "a"]
def sort_keys_by_value(d):
    raise NotImplementedError


# --------------------------- tests: do not edit ---------------------------
DRILLS = [
    ("A. NUMBERS AND OPERATORS", [
        ("add", add, [((2, 3), 5), ((-1, 1), 0)]),
        ("whole_divide", whole_divide, [((7, 2), 3), ((9, 3), 3)]),
        ("remainder", remainder, [((7, 2), 1), ((8, 4), 0)]),
        ("power", power, [((2, 3), 8), ((5, 0), 1)]),
        ("is_even", is_even, [((4,), True), ((7,), False), ((0,), True)]),
        ("distance", distance, [((-4,), 4), ((4,), 4), ((0,), 0)]),
        ("to_int", to_int, [((3.9,), 3), ((-3.9,), -3)]),
        ("smaller", smaller, [((2, 5), 2), ((5, 2), 2), ((3, 3), 3)]),
    ]),
    ("B. STRINGS", [
        ("shout", shout, [(("hi",), "HI"), (("",), "")]),
        ("whisper", whisper, [(("HI",), "hi")]),
        ("first_char", first_char, [(("abc",), "a")]),
        ("last_char", last_char, [(("abc",), "c")]),
        ("char_count", char_count, [(("abc",), 3), (("",), 0)]),
        ("reverse_string", reverse_string, [(("abc",), "cba"), (("",), "")]),
        ("contains", contains, [(("hello", "ell"), True), (("hello", "z"), False)]),
        ("starts_with", starts_with, [(("hello", "he"), True), (("hello", "lo"), False)]),
        ("trim", trim, [(("  hi  ",), "hi"), (("a b",), "a b")]),
        ("split_words", split_words, [(("a b c",), ["a", "b", "c"]), (("",), [])]),
        ("join_words", join_words, [((["a", "b"],), "a-b"), ((["x"],), "x")]),
        ("only_digits", only_digits, [(("a1b2",), "12"), (("abc",), "")]),
        ("count_char", count_char, [(("banana", "a"), 3), (("abc", "z"), 0)]),
        ("replace_all", replace_all, [(("a-b-c", "-", "+"), "a+b+c")]),
    ]),
    ("C. LISTS: INDEXING AND SLICING", [
        ("last_element", last_element, [(([1, 2, 3],), 3), (([9],), 9)]),
        ("first_three", first_three, [(([1, 2, 3, 4, 5],), [1, 2, 3]), (([1],), [1])]),
        ("reverse_list", reverse_list, [(([1, 2, 3],), [3, 2, 1]), (([],), [])]),
        ("last_two", last_two, [(([1, 2, 3, 4],), [3, 4]), (([7],), [7])]),
        ("drop_first", drop_first, [(([1, 2, 3],), [2, 3]), (([1],), [])]),
        ("every_other", every_other, [(([1, 2, 3, 4, 5],), [1, 3, 5]), (([],), [])]),
        ("middle", middle, [(([1, 2, 3],), 2), (([5],), 5)]),
        ("size", size, [(([1, 2],), 2), (([],), 0)]),
        ("with_added", with_added, [(([1, 2], 3), [1, 2, 3]), (([], 1), [1])]),
        ("concat", concat, [(([1], [2, 3]), [1, 2, 3]), (([], []), [])]),
        ("has", has, [(([1, 2], 2), True), (([1], 9), False)]),
        ("position_of", position_of, [(([1, 2, 3], 2), 1), (([1], 9), -1)]),
    ]),
    ("D. LOOPS AND CONDITIONALS", [
        ("total", total, [(([1, 2, 3],), 6), (([],), 0)]),
        ("count_positive", count_positive, [(([-1, 2, 3],), 2), (([],), 0)]),
        ("index_of_max", index_of_max, [(([1, 9, 3],), 1), (([5],), 0), (([2, 2, 7],), 2)]),
        ("first_negative", first_negative, [(([1, -2, -3],), -2), (([1, 2],), None)]),
        ("all_even", all_even, [(([2, 4],), True), (([2, 3],), False), (([],), True)]),
        ("any_negative", any_negative, [(([1, -2],), True), (([1, 2],), False)]),
        ("largest", largest, [(([1, 9, 3],), 9), (([5],), 5), (([-3, -1],), -1)]),
        ("running", running, [(([1, 2, 3],), [1, 3, 6]), (([],), [])]),
        ("fizz", fizz, [((3,), "fizz"), ((5,), "buzz"), ((15,), "fizzbuzz"), ((7,), "7")]),
        ("sign_word", sign_word, [((-2,), "negative"), ((0,), "zero"), ((4,), "positive")]),
    ]),
    ("E. DICTS AND SETS", [
        ("count_items", count_items, [((["a", "a", "b"],), {"a": 2, "b": 1}), (([],), {})]),
        ("unique_sorted", unique_sorted, [(([3, 1, 3, 2],), [1, 2, 3]), (([],), [])]),
        ("lookup", lookup, [(({"a": 1}, "a", 0), 1), (({"a": 1}, "z", 0), 0)]),
        ("has_key", has_key, [(({"a": 1}, "a"), True), (({"a": 1}, "z"), False)]),
        ("sorted_keys", sorted_keys, [(({"b": 1, "a": 2},), ["a", "b"]), (({},), [])]),
        ("sum_values", sum_values, [(({"a": 1, "b": 2},), 3), (({},), 0)]),
        ("invert", invert, [(({"a": 1},), {1: "a"}), (({},), {})]),
        ("top_key", top_key, [(({"a": 1, "b": 9},), "b"), (({"z": 5},), "z")]),
        ("in_both", in_both, [(([1, 2, 3], [2, 3, 4]), [2, 3]), (([1], [9]), [])]),
        ("only_in_first", only_in_first, [(([1, 2, 3], [2]), [1, 3]), (([1], [1]), [])]),
        ("in_either", in_either, [(([1, 2], [2, 3]), [1, 2, 3]), (([], []), [])]),
        ("first_repeat", first_repeat, [(([1, 2, 1],), 1), (([1, 2],), None)]),
        ("two_sum", two_sum, [(([2, 7, 11, 15], 9), [0, 1]), (([3, 2, 4], 6), [1, 2]),
                              (([3, 3], 6), [0, 1])]),
        ("group_by_first", group_by_first,
         [((["ant", "ape", "bee"],), {"a": ["ant", "ape"], "b": ["bee"]}), (([],), {})]),
    ]),
    ("F. COMPREHENSIONS", [
        ("doubled_evens", doubled_evens, [(([1, 2, 3, 4],), [4, 8]), (([1, 3],), [])]),
        ("squares", squares, [(([1, 2, 3],), [1, 4, 9]), (([],), [])]),
        ("long_words", long_words, [((["hi", "tree", "a"],), ["tree"]), (([],), [])]),
        ("lengths", lengths, [((["ab", "c"],), [2, 1]), (([],), [])]),
        ("flatten", flatten, [(([[1, 2], [3]],), [1, 2, 3]), (([],), [])]),
        ("length_map", length_map, [((["ab", "c"],), {"ab": 2, "c": 1}), (([],), {})]),
        ("first_letters", first_letters, [((["ant", "ape", "bee"],), {"a", "b"}), (([],), set())]),
        ("sum_two_lists", sum_two_lists, [(([1, 2], [10, 20]), [11, 22]), (([], []), [])]),
        ("upper_all", upper_all, [((["a", "b"],), ["A", "B"]), (([],), [])]),
        ("pairs", pairs, [((["a", "b"],), [(0, "a"), (1, "b")]), (([],), [])]),
    ]),
    ("G. TUPLES, UNPACKING, FUNCTIONS", [
        ("swap", swap, [((1, 2), (2, 1)), (("a", "b"), ("b", "a"))]),
        ("min_and_max", min_and_max, [(([3, 1, 2],), (1, 3)), (([5],), (5, 5))]),
        ("difference", difference, [(((10, 4),), 6), (((1, 1),), 0)]),
        ("add_all", add_all, [((1, 2, 3), 6), ((), 0), ((5,), 5)]),
        ("repeat", repeat, [(("hi",), "hi hi"), (("a", 3), "a a a")]),
        ("zip_dict", zip_dict, [((["a", "b"], [1, 2]), {"a": 1, "b": 2}), (([], []), {})]),
    ]),
    ("H. SORTING", [
        ("sort_desc", sort_desc, [(([1, 3, 2],), [3, 2, 1]), (([],), [])]),
        ("by_length", by_length, [((["tree", "a", "bc"],), ["a", "bc", "tree"])]),
        ("by_score", by_score, [(([("a", 1), ("b", 9)],), [("b", 9), ("a", 1)])]),
        ("by_alpha", by_alpha, [((["b", "A"],), ["A", "b"]), (([],), [])]),
        ("top_k", top_k, [(([4, 9, 1, 7], 2), [9, 7]), (([1], 3), [1])]),
        ("sort_keys_by_value", sort_keys_by_value,
         [(({"a": 3, "b": 1},), ["b", "a"]), (({},), [])]),
    ]),
]

if __name__ == "__main__":
    run(DRILLS)
