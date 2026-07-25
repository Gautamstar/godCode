"""
PROBLEM : Backspace String Compare
TOPIC   : Stack
LEVEL   : Easy

    '#' means a backspace (delete the previous character). Return True if the two
    strings are equal after applying all backspaces.

Examples:
    backspace_compare("ab#c", "ad#c")  ->  True
    backspace_compare("a#c", "b")      ->  False

Hint (only peek if you are stuck):
    Write a small helper that builds the final string with a stack, then compare the two results.

HOW TO RUN:  python 04_stack\problems\04_backspace_compare.py
"""


def backspace_compare(s, t):
    # YOUR CODE HERE
    pass


# --------------------------- tests: do not edit ---------------------------
TESTS = [
    (('ab#c', 'ad#c'), True),
    (('ab##', 'c#d#'), True),
    (('a#c', 'b'), False),
    (('', ''), True),
    (('#a', 'a'), True),

]

if __name__ == "__main__":
    passed = 0
    for args, expected in TESTS:
        try:
            got = backspace_compare(*args)
        except Exception as e:
            got = "ERROR: " + str(e)
        ok = got == expected
        passed += ok
        print(("PASS  " if ok else "FAIL  ") + "backspace_compare" + repr(args) +
              " -> " + repr(got) + "   expected " + repr(expected))
    print()
    print(str(passed) + "/" + str(len(TESTS)) + " passed")
