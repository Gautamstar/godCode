"""
MODULE 00 DRILLS - pure Python reps, no algorithms yet.

Fill in each function body. These are the exact syntax reflexes every later
problem depends on. Read LESSON.md first if a drill is unclear.

RUN:  python 00_python_for_dsa/drills.py
"""


# 1. Return the LAST element of the list. (negative indexing)
def last_element(nums):
    pass


# 2. Return the first three items of the list. (slicing)
def first_three(nums):
    pass


# 3. Return the list reversed. (slice with a step of -1)
def reverse_list(items):
    pass


# 4. Return the INDEX of the largest number. (enumerate)
def index_of_max(nums):
    pass


# 5. Return a dict mapping each item to how many times it appears.
#    (the freq.get(x, 0) + 1 idiom)
def count_items(items):
    pass


# 6. Return a sorted list of the UNIQUE values. (set, then sorted)
def unique_sorted(items):
    pass


# 7. Join the words with a dash between them:  ["a","b"] -> "a-b"
def join_words(words):
    pass


# 8. Return a string of only the digit characters from s.
#    "a1b2" -> "12"        (loop or comprehension + .isdigit())
def only_digits(s):
    pass


# 9. Return the numbers sorted from largest to smallest.
def sort_desc(nums):
    pass


# 10. Return a list with every EVEN number doubled, odds dropped.
#     [1,2,3,4] -> [4,8]        (comprehension with a condition)
def doubled_evens(nums):
    pass


# 11. Return the two values swapped, as a tuple:  (1,2) -> (2,1)
def swap(a, b):
    pass


# 12. Return the pairwise sums of two equal-length lists.
#     [1,2],[10,20] -> [11,22]        (zip)
def sum_two_lists(a, b):
    pass


# --------------------------- tests: do not edit ---------------------------
DRILLS = [
    ("last_element",  last_element,  [(([1, 2, 3],), 3), (([9],), 9)]),
    ("first_three",   first_three,   [(([1, 2, 3, 4, 5],), [1, 2, 3]), (([1],), [1])]),
    ("reverse_list",  reverse_list,  [(([1, 2, 3],), [3, 2, 1]), (([],), [])]),
    ("index_of_max",  index_of_max,  [(([1, 9, 3],), 1), (([5],), 0), (([2, 2, 7],), 2)]),
    ("count_items",   count_items,   [((["a", "a", "b"],), {"a": 2, "b": 1}), (([],), {})]),
    ("unique_sorted", unique_sorted, [(([3, 1, 3, 2],), [1, 2, 3]), (([],), [])]),
    ("join_words",    join_words,    [((["a", "b"],), "a-b"), ((["x"],), "x")]),
    ("only_digits",   only_digits,   [(("a1b2",), "12"), (("abc",), "")]),
    ("sort_desc",     sort_desc,     [(([1, 3, 2],), [3, 2, 1]), (([],), [])]),
    ("doubled_evens", doubled_evens, [(([1, 2, 3, 4],), [4, 8]), (([1, 3],), [])]),
    ("swap",          swap,          [((1, 2), (2, 1)), (("a", "b"), ("b", "a"))]),
    ("sum_two_lists", sum_two_lists, [(([1, 2], [10, 20]), [11, 22]), (([], []), [])]),
]

if __name__ == "__main__":
    total = 0
    solved = 0
    for name, fn, cases in DRILLS:
        ok_all = True
        for args, expected in cases:
            try:
                got = fn(*args)
            except Exception as e:
                got = "ERROR: " + str(e)
            if got != expected:
                ok_all = False
                print("FAIL  " + name + repr(args) + " -> " + repr(got) +
                      "   expected " + repr(expected))
        total += 1
        if ok_all:
            solved += 1
            print("PASS  " + name)
    print()
    print(str(solved) + "/" + str(total) + " drills complete")
