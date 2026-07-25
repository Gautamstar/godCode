"""SOLUTION - Evaluate Reverse Polish Notation

RPN is what a stack was made for. Careful with order: b = stack.pop() is the right
operand and a = stack.pop() is the left, so it is a - b, not b - a. Use int(a / b)
for truncation toward zero (// floors toward negative infinity, which differs for
negative results).
"""


def eval_rpn(tokens):
    stack = []
    for t in tokens:
        if t in ("+", "-", "*", "/"):
            b = stack.pop()
            a = stack.pop()
            if t == "+":
                stack.append(a + b)
            elif t == "-":
                stack.append(a - b)
            elif t == "*":
                stack.append(a * b)
            else:
                stack.append(int(a / b))
        else:
            stack.append(int(t))
    return stack[0]


TESTS = [
    ((['2', '1', '+', '3', '*'],), 9),
    ((['4', '13', '5', '/', '+'],), 6),
    ((['5'],), 5),
    ((['3', '-4', '+'],), -1),

]

if __name__ == "__main__":
    passed = 0
    for args, expected in TESTS:
        got = eval_rpn(*args)
        passed += (got == expected)
        print(("PASS  " if got == expected else "FAIL  ") + repr(args) + " -> " + repr(got))
    print()
    print(str(passed) + "/" + str(len(TESTS)) + " passed")
