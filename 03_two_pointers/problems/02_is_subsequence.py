"""
PROBLEM : Is Subsequence
TOPIC   : Two Pointers
LEVEL   : Easy

    Return True if s is a subsequence of t, meaning you can delete some characters
    from t (without reordering) and get s.

Examples:
    is_subsequence("abc", "ahbgdc")  ->  True
    is_subsequence("axc", "ahbgdc")  ->  False

Hint (only peek if you are stuck):
    One pointer into s. Walk t; every time the characters match, advance the s pointer.

HOW TO RUN:  python 03_two_pointers\problems\02_is_subsequence.py
"""


def is_subsequence(s, t):
    # YOUR CODE HERE
    pass


# --------------------------- tests: do not edit ---------------------------
TESTS = [
    (('abc', 'ahbgdc'), True),
    (('axc', 'ahbgdc'), False),
    (('', 'abc'), True),
    (('abc', ''), False),
    (('b', 'abc'), True),

]

if __name__ == "__main__":
    passed = 0
    for args, expected in TESTS:
        try:
            got = is_subsequence(*args)
        except Exception as e:
            got = "ERROR: " + str(e)
        ok = got == expected
        passed += ok
        print(("PASS  " if ok else "FAIL  ") + "is_subsequence" + repr(args) +
              " -> " + repr(got) + "   expected " + repr(expected))
    print()
    print(str(passed) + "/" + str(len(TESTS)) + " passed")
