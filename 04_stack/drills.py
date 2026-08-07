"""
MODULE 04 DRILLS - stacks, 26 reps.

A stack is just a Python list you only touch at the end: .append() to push,
.pop() to take the last one back, [-1] to look without removing.

The reason it matters is the shape of problem it solves: anything where the
thing you need next is the most RECENT thing you saw. Matching brackets, undo,
"what was the last unresolved item", and every monotonic-stack question.

RUN
    python 04_stack/drills.py                everything
    python 04_stack/drills.py 18             just drill 18
    python 04_stack/drills.py greater        name contains "greater"
    python 04_stack/drills.py -v             list passing drills too
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from drill_harness import run  # noqa: E402


# ===========================================================================
# A. STACK BASICS
# ===========================================================================

# 1. Run a list of operations and return the final stack.
#    Each op is ("push", value) or ("pop",). A pop on an empty stack does
#    nothing.  run_ops([("push",1),("push",2),("pop",)]) -> [1]
def run_ops(ops):
    raise NotImplementedError


# 2. Return the top of the stack WITHOUT removing it, or None when empty.
#    stack[-1] reads the last item. Guard the empty case first.
def peek(stack):
    raise NotImplementedError


# 3. Reverse a list by pushing everything then popping everything.
#    Slower than [::-1], but it is the drill: last in, first out.
def reverse_with_stack(items):
    raise NotImplementedError


# 4. Return True when the round brackets in s are balanced.
#    Push on "(", pop on ")". A pop with nothing to pop means unbalanced, and
#    anything left on the stack at the end means unbalanced too.
def is_balanced_simple(s):
    raise NotImplementedError


# 5. Same, but for ( ) [ ] and { }, which must also nest correctly.
#    "([)]" is invalid. On a closer, check the popped opener actually matches.
#    A dict from closer to opener makes this short.
def is_balanced_multi(s):
    raise NotImplementedError


# 6. Return the deepest nesting level of round brackets.
#    max_depth("((a))") -> 2,  max_depth("()()") -> 1,  max_depth("") -> 0
#    A counter is enough here; the stack is implicit.
def max_depth(s):
    raise NotImplementedError


# 7. Evaluate a postfix expression given as tokens.
#    evaluate_postfix(["2","3","+"]) -> 5
#    Push numbers. On an operator pop TWO, apply, push the result. Order
#    matters: the first pop is the right operand.
#    Only + - * are used, and integer division is not needed.
def evaluate_postfix(tokens):
    raise NotImplementedError


# ===========================================================================
# B. UNDO AND MATCHING
# ===========================================================================

# 8. Apply backspaces, where "#" deletes the character before it.
#    backspace("ab#c") -> "ac",  backspace("###") -> ""
def backspace(s):
    raise NotImplementedError


# 9. Repeatedly remove adjacent EQUAL characters until none are left.
#    squash("abbaca") -> "ca"
#    One pass with a stack does it: if the new character equals the top, pop
#    instead of pushing.
def squash(s):
    raise NotImplementedError


# 10. Score a baseball game.  Each op is a number, "C" (cancel the last score),
#     "D" (double the last score), or "+" (sum of the last two). Return the
#     total.  baseball(["5","2","C","D","+"]) -> 30
def baseball(ops):
    raise NotImplementedError


# 11. Return the smallest number of brackets to add to make s balanced.
#     count_unmatched("())") -> 1,  count_unmatched("(((") -> 3
#     Track unmatched openers on the stack and count closers that find nothing.
def count_unmatched(s):
    raise NotImplementedError


# 12. Simplify a Unix path.  "/a/./b/../c" -> "/a/c"
#     Split on "/". Ignore "" and ".". On ".." pop if you can. Join the rest
#     back with "/" and a leading slash.
def simplify_path(path):
    raise NotImplementedError


# 13. Expand a single level of repeats.  "3[ab]" -> "ababab",  "2[a]1[b]" -> "aab"
#     No nesting. The digit is always a single character.
def decode_repeat(s):
    raise NotImplementedError


# 14. Reverse the order of the words using a stack.
def reverse_words_with_stack(s):
    raise NotImplementedError


# 15. Return True when s is a palindrome, checked with a stack.
#     Push every character, then pop while walking forward.
def is_palindrome_stack(s):
    raise NotImplementedError


# 16. Could `popped` be the pop order of a stack that had `pushed` pushed in
#     order?  valid_pop_sequence([1,2,3],[3,2,1]) -> True
#                                 ([1,2,3],[3,1,2]) -> False
#     Simulate: push each value, then pop while the top matches the next
#     expected pop.
def valid_pop_sequence(pushed, popped):
    raise NotImplementedError


# 17. Remove the OUTERMOST brackets of every top-level group.
#     remove_outer("(()())(())") -> "()()()",  remove_outer("()()") -> ""
#     Track depth. Keep a character only when it is not the outermost layer.
def remove_outer(s):
    raise NotImplementedError


# ===========================================================================
# C. MONOTONIC STACK
# ===========================================================================
#
# The pattern: walk the list holding a stack of items still WAITING for an
# answer. When the current value resolves what is on top, pop and record.
# Each item is pushed once and popped once, so the whole thing is O(n) even
# though it looks like a nested loop.

# 18. For each value, the next value to its right that is larger, or -1.
#     next_greater([2,1,3]) -> [3, 3, -1]
#     Keep a stack of INDICES still waiting. While the current value beats the
#     value at the top index, that index's answer is the current value.
def next_greater(nums):
    raise NotImplementedError


# 19. For each value, the nearest value to its LEFT that is larger, or -1.
#     previous_greater([2,1,3]) -> [-1, 2, -1]
#     Same walk, but you read the answer off the stack before pushing.
def previous_greater(nums):
    raise NotImplementedError


# 20. For each value, the next value to its right that is smaller, or -1.
#     next_smaller([2,1,3]) -> [1, -1, -1]
def next_smaller(nums):
    raise NotImplementedError


# 21. For each value, the nearest value to its LEFT that is smaller, or -1.
#     previous_smaller([2,1,3]) -> [-1, -1, 1]
def previous_smaller(nums):
    raise NotImplementedError


# 22. How many days until a warmer temperature, 0 when it never comes.
#     warmer([73,74,75,71,69,72,76,73]) -> [1,1,4,2,1,1,0,0]
#     next_greater again, but recording the index GAP instead of the value.
def warmer(temps):
    raise NotImplementedError


# 23. Stock span: for each price, how many consecutive days up to and
#     including today had a price less than or equal to today's.
#     span([100,80,60,70,60,75,85]) -> [1,1,1,2,1,4,6]
def span(prices):
    raise NotImplementedError


# 24. Count the buildings visible from the left, meaning taller than every
#     building before them.  visible_from_left([3,1,4,2,5]) -> 3
def visible_from_left(heights):
    raise NotImplementedError


# 25. next_greater, but the list wraps around at the end.
#     next_greater_circular([1,2,1]) -> [2, -1, 2]
#     Walk the list twice, and only push indices on the first pass.
def next_greater_circular(nums):
    raise NotImplementedError


# 26. Remove k digits from the number string to leave the smallest possible
#     number, keeping the order of the rest.
#     remove_k_digits("1432219", 3) -> "1219"
#     Greedy with a stack: while the top digit is bigger than the current one
#     and you still have removals left, pop it. Strip leading zeros at the end,
#     and return "0" when nothing is left.
def remove_k_digits(digits, k):
    raise NotImplementedError


# --------------------------- tests: do not edit ---------------------------
DRILLS = [
    ("A. STACK BASICS", [
        ("run_ops", run_ops, [(([("push", 1), ("push", 2), ("pop",)],), [1]),
                              (([("pop",)],), []), (([],), [])]),
        ("peek", peek, [(([1, 2],), 2), (([],), None)]),
        ("reverse_with_stack", reverse_with_stack, [(([1, 2, 3],), [3, 2, 1]),
                                                    (([],), [])]),
        ("is_balanced_simple", is_balanced_simple, [(("(())",), True), (("(()",), False),
                                                    ((")(",), False), (("",), True)]),
        ("is_balanced_multi", is_balanced_multi, [(("([]{})",), True),
                                                  (("([)]",), False),
                                                  (("{[]}",), True), (("]",), False)]),
        ("max_depth", max_depth, [(("((a))",), 2), (("()()",), 1), (("",), 0)]),
        ("evaluate_postfix", evaluate_postfix,
         [((["2", "3", "+"],), 5), ((["4", "2", "-"],), 2),
          ((["2", "3", "*", "4", "+"],), 10)]),
    ]),
    ("B. UNDO AND MATCHING", [
        ("backspace", backspace, [(("ab#c",), "ac"), (("###",), ""), (("abc",), "abc")]),
        ("squash", squash, [(("abbaca",), "ca"), (("abc",), "abc"), (("aa",), "")]),
        ("baseball", baseball, [(((["5", "2", "C", "D", "+"]),), 30),
                                (((["1", "2"]),), 3)]),
        ("count_unmatched", count_unmatched, [(("())",), 1), (("(((",), 3),
                                              (("()",), 0), ((")(",), 2)]),
        ("simplify_path", simplify_path, [(("/a/./b/../c",), "/a/c"), (("/../",), "/"),
                                          (("/home//foo/",), "/home/foo")]),
        ("decode_repeat", decode_repeat, [(("3[ab]",), "ababab"), (("2[a]1[b]",), "aab"),
                                          (("",), "")]),
        ("reverse_words_with_stack", reverse_words_with_stack,
         [(("a b c",), "c b a"), (("hi",), "hi")]),
        ("is_palindrome_stack", is_palindrome_stack, [(("aba",), True), (("ab",), False),
                                                      (("",), True)]),
        ("valid_pop_sequence", valid_pop_sequence, [(([1, 2, 3], [3, 2, 1]), True),
                                                    (([1, 2, 3], [3, 1, 2]), False),
                                                    (([], []), True)]),
        ("remove_outer", remove_outer, [(("(()())(())",), "()()()"), (("()()",), ""),
                                        (("",), "")]),
    ]),
    ("C. MONOTONIC STACK", [
        ("next_greater", next_greater, [(([2, 1, 3],), [3, 3, -1]),
                                        (([3, 2, 1],), [-1, -1, -1]), (([],), [])]),
        ("previous_greater", previous_greater, [(([2, 1, 3],), [-1, 2, -1]),
                                                (([1, 2, 3],), [-1, -1, -1])]),
        ("next_smaller", next_smaller, [(([2, 1, 3],), [1, -1, -1]),
                                        (([1, 2, 3],), [-1, -1, -1])]),
        ("previous_smaller", previous_smaller, [(([2, 1, 3],), [-1, -1, 1]),
                                                (([3, 2, 1],), [-1, -1, -1])]),
        ("warmer", warmer, [(([73, 74, 75, 71, 69, 72, 76, 73],),
                             [1, 1, 4, 2, 1, 1, 0, 0]), (([5],), [0])]),
        ("span", span, [(([100, 80, 60, 70, 60, 75, 85],), [1, 1, 1, 2, 1, 4, 6]),
                        (([1],), [1])]),
        ("visible_from_left", visible_from_left, [(([3, 1, 4, 2, 5],), 3),
                                                  (([1, 2, 3],), 3), (([],), 0)]),
        ("next_greater_circular", next_greater_circular, [(([1, 2, 1],), [2, -1, 2]),
                                                          (([3, 2, 1],), [-1, 3, 3])]),
        ("remove_k_digits", remove_k_digits, [(("1432219", 3), "1219"),
                                              (("10200", 1), "200"),
                                              (("10", 2), "0")]),
    ]),
]

if __name__ == "__main__":
    run(DRILLS)
