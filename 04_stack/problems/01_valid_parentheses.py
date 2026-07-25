"""
PROBLEM : Valid Parentheses
TOPIC   : Stack
LEVEL   : Easy

    Given a string of (), [] and {}, return True if every bracket is closed by the
    matching type in the correct order.

Examples:
    valid_parentheses("()[]{}")  ->  True
    valid_parentheses("([)]")    ->  False

Hint (only peek if you are stuck):
    Push opening brackets. On a closing bracket, the top of the stack must be its partner.

HOW TO RUN:  python 04_stack\problems\01_valid_parentheses.py
"""


def valid_parentheses(s):
    # YOUR CODE HERE
    pass


# --------------------------- tests: do not edit ---------------------------
TESTS = [
    (('()',), True),
    (('()[]{}',), True),
    (('(]',), False),
    (('([)]',), False),
    (('{[]}',), True),
    (('',), True),
    (('(',), False),
    ((')',), False),

]

if __name__ == "__main__":
    passed = 0
    for args, expected in TESTS:
        try:
            got = valid_parentheses(*args)
        except Exception as e:
            got = "ERROR: " + str(e)
        ok = got == expected
        passed += ok
        print(("PASS  " if ok else "FAIL  ") + "valid_parentheses" + repr(args) +
              " -> " + repr(got) + "   expected " + repr(expected))
    print()
    print(str(passed) + "/" + str(len(TESTS)) + " passed")
