"""SOLUTION - Baseball Game

A direct stack simulation. Read the op, mutate the stack, sum at the end.
Remember int(op) to convert the numeric strings.
"""


def baseball_game(ops):
    stack = []
    for op in ops:
        if op == "+":
            stack.append(stack[-1] + stack[-2])
        elif op == "D":
            stack.append(2 * stack[-1])
        elif op == "C":
            stack.pop()
        else:
            stack.append(int(op))
    return sum(stack)


TESTS = [
    ((['5', '2', 'C', 'D', '+'],), 30),
    ((['5', '-2', '4', 'C', 'D', '9', '+', '+'],), 27),
    ((['1'],), 1),
    (([],), 0),

]

if __name__ == "__main__":
    passed = 0
    for args, expected in TESTS:
        got = baseball_game(*args)
        passed += (got == expected)
        print(("PASS  " if got == expected else "FAIL  ") + repr(args) + " -> " + repr(got))
    print()
    print(str(passed) + "/" + str(len(TESTS)) + " passed")
