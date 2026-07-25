"""
PROBLEM : Character Frequency
TOPIC   : Hash Maps
LEVEL   : Easy

    Return a dict mapping each character to how many times it appears.

Examples:
    char_frequency("aab")  ->  {"a": 2, "b": 1}

Hint (only peek if you are stuck):
    Loop the string and use freq.get(c, 0) + 1 so missing keys start at 0.

HOW TO RUN:  python 02_hashmaps_sets\problems\06_char_frequency.py
"""


def char_frequency(s):
    # YOUR CODE HERE
    pass


# --------------------------- tests: do not edit ---------------------------
TESTS = [
    (('aab',), {'a': 2, 'b': 1}),
    (('',), {}),
    (('abc',), {'a': 1, 'b': 1, 'c': 1}),
    (('aaa',), {'a': 3}),

]

if __name__ == "__main__":
    passed = 0
    for args, expected in TESTS:
        try:
            got = char_frequency(*args)
        except Exception as e:
            got = "ERROR: " + str(e)
        ok = got == expected
        passed += ok
        print(("PASS  " if ok else "FAIL  ") + "char_frequency" + repr(args) +
              " -> " + repr(got) + "   expected " + repr(expected))
    print()
    print(str(passed) + "/" + str(len(TESTS)) + " passed")
