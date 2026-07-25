"""
PROBLEM : Evaluate Reverse Polish Notation
TOPIC   : Stack
LEVEL   : Medium

    Evaluate an expression in Reverse Polish Notation (the operator comes AFTER its
    two operands). Division truncates toward zero.

Examples:
    eval_rpn(["2","1","+","3","*"])   ->  9      ((2+1)*3)
    eval_rpn(["4","13","5","/","+"]) ->  6      (4 + 13//5)

Hint (only peek if you are stuck):
    Push numbers. On an operator, pop TWO values. Order matters: the first pop is the RIGHT operand.

HOW TO RUN:  python 04_stack\problems\05_eval_rpn.py
"""


def eval_rpn(tokens):
    # YOUR CODE HERE
    pass


# --------------------------- tests: do not edit ---------------------------
TESTS = [
    ((['2', '1', '+', '3', '*'],), 9),
    ((['4', '13', '5', '/', '+'],), 6),
    ((['5'],), 5),
    ((['3', '-4', '+'],), -1),

]

if __name__ == "__main__":
    passed = 0
    for args, expected in TESTS:
        try:
            got = eval_rpn(*args)
        except Exception as e:
            got = "ERROR: " + str(e)
        ok = got == expected
        passed += ok
        print(("PASS  " if ok else "FAIL  ") + "eval_rpn" + repr(args) +
              " -> " + repr(got) + "   expected " + repr(expected))
    print()
    print(str(passed) + "/" + str(len(TESTS)) + " passed")
