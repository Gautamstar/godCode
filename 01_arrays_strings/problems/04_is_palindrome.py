"""
PROBLEM : Valid Palindrome
TOPIC   : Strings / Two Pointers
LEVEL   : Easy

    Return True if the string reads the same forwards and backwards,
    ignoring case and any character that is not a letter or digit.

Examples:
    is_palindrome("A man, a plan, a canal: Panama")  ->  True
    is_palindrome("race a car")                     ->  False

Hint (only peek if you are stuck):
    Build a cleaned list of lowercase alphanumeric chars, then compare it to its reverse.

HOW TO RUN:  python 01_arrays_strings\problems\04_is_palindrome.py
"""


def is_palindrome(s):
    # YOUR CODE HERE
    pass


# --------------------------- tests: do not edit ---------------------------
TESTS = [
    (('A man, a plan, a canal: Panama',), True),
    (('race a car',), False),
    (('',), True),
    (('ab',), False),
    (('Aa',), True),

]

if __name__ == "__main__":
    passed = 0
    for args, expected in TESTS:
        try:
            got = is_palindrome(*args)
        except Exception as e:
            got = "ERROR: " + str(e)
        ok = got == expected
        passed += ok
        print(("PASS  " if ok else "FAIL  ") + "is_palindrome" + repr(args) +
              " -> " + repr(got) + "   expected " + repr(expected))
    print()
    print(str(passed) + "/" + str(len(TESTS)) + " passed")
