"""
PROBLEM : Longest Substring Without Repeating Characters
TOPIC   : Sliding Window (variable)
LEVEL   : Medium

    Return the LENGTH of the longest substring that has no repeated characters.

Examples:
    longest_substring_no_repeat("abcabcbb")  ->  3    ("abc")
    longest_substring_no_repeat("pwwkew")    ->  3    ("wke")

Hint (only peek if you are stuck):
    Keep a window [left..right]. Store each character's last index. On a repeat INSIDE the window, jump left past it.

HOW TO RUN:  python 05_sliding_window\problems\04_longest_substring_no_repeat.py
"""


def longest_substring_no_repeat(s):
    # YOUR CODE HERE
    pass


# --------------------------- tests: do not edit ---------------------------
TESTS = [
    (('abcabcbb',), 3),
    (('bbbbb',), 1),
    (('pwwkew',), 3),
    (('',), 0),
    (('abcdef',), 6),

]

if __name__ == "__main__":
    passed = 0
    for args, expected in TESTS:
        try:
            got = longest_substring_no_repeat(*args)
        except Exception as e:
            got = "ERROR: " + str(e)
        ok = got == expected
        passed += ok
        print(("PASS  " if ok else "FAIL  ") + "longest_substring_no_repeat" + repr(args) +
              " -> " + repr(got) + "   expected " + repr(expected))
    print()
    print(str(passed) + "/" + str(len(TESTS)) + " passed")
