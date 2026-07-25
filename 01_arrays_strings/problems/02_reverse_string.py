"""
PROBLEM : Reverse a String
TOPIC   : Strings
LEVEL   : Easy

    Return the string reversed.

Examples:
    reverse_string("hello")  ->  "olleh"
    reverse_string("a")      ->  "a"

Hint (only peek if you are stuck):
    Python slicing: s[::-1] reverses any sequence.

HOW TO RUN:  python 01_arrays_strings\problems\02_reverse_string.py
"""


def reverse_string(s):
    # YOUR CODE HERE
    pass


# --------------------------- tests: do not edit ---------------------------
TESTS = [
    (('hello',), 'olleh'),
    (('a',), 'a'),
    (('',), ''),
    (('abcd',), 'dcba'),

]

if __name__ == "__main__":
    passed = 0
    for args, expected in TESTS:
        try:
            got = reverse_string(*args)
        except Exception as e:
            got = "ERROR: " + str(e)
        ok = got == expected
        passed += ok
        print(("PASS  " if ok else "FAIL  ") + "reverse_string" + repr(args) +
              " -> " + repr(got) + "   expected " + repr(expected))
    print()
    print(str(passed) + "/" + str(len(TESTS)) + " passed")
