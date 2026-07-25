"""
PROBLEM : Remove Adjacent Duplicates
TOPIC   : Stack
LEVEL   : Easy

    Repeatedly remove two ADJACENT equal characters until none remain.
    Return the final string.

Examples:
    remove_adjacent_duplicates("abbaca")  ->  "ca"
    remove_adjacent_duplicates("azxxzy")  ->  "ay"

Hint (only peek if you are stuck):
    Push characters. If the incoming character equals the top of the stack, pop instead of pushing.

HOW TO RUN:  python 04_stack\problems\02_remove_adjacent_duplicates.py
"""


def remove_adjacent_duplicates(s):
    # YOUR CODE HERE
    pass


# --------------------------- tests: do not edit ---------------------------
TESTS = [
    (('abbaca',), 'ca'),
    (('azxxzy',), 'ay'),
    (('',), ''),
    (('aa',), ''),
    (('abc',), 'abc'),

]

if __name__ == "__main__":
    passed = 0
    for args, expected in TESTS:
        try:
            got = remove_adjacent_duplicates(*args)
        except Exception as e:
            got = "ERROR: " + str(e)
        ok = got == expected
        passed += ok
        print(("PASS  " if ok else "FAIL  ") + "remove_adjacent_duplicates" + repr(args) +
              " -> " + repr(got) + "   expected " + repr(expected))
    print()
    print(str(passed) + "/" + str(len(TESTS)) + " passed")
