"""SOLUTION - Longest Substring Without Repeating Characters

The variable-size window. Grow to the right always; when the new character was
already seen at or after `left`, jump `left` to just past that old position. The
check seen[c] >= left matters, otherwise stale positions shrink the window wrongly.
"""


def longest_substring_no_repeat(s):
    seen = {}
    left = 0
    best = 0
    for right, c in enumerate(s):
        if c in seen and seen[c] >= left:
            left = seen[c] + 1
        seen[c] = right
        best = max(best, right - left + 1)
    return best


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
        got = longest_substring_no_repeat(*args)
        passed += (got == expected)
        print(("PASS  " if got == expected else "FAIL  ") + repr(args) + " -> " + repr(got))
    print()
    print(str(passed) + "/" + str(len(TESTS)) + " passed")
