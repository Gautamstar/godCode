"""
PROBLEM : Baseball Game
TOPIC   : Stack
LEVEL   : Easy

    Process a list of string operations on a score record:
      a number -> record that score
      "+"      -> record the sum of the previous two scores
      "D"      -> record double the previous score
      "C"      -> remove the previous score
    Return the sum of all recorded scores.

Examples:
    baseball_game(["5","2","C","D","+"])  ->  30

Hint (only peek if you are stuck):
    Keep a list as the record. Each op pushes or pops. Sum it at the end.

HOW TO RUN:  python 04_stack\problems\03_baseball_game.py
"""


def baseball_game(ops):
    # YOUR CODE HERE
    pass


# --------------------------- tests: do not edit ---------------------------
TESTS = [
    ((['5', '2', 'C', 'D', '+'],), 30),
    ((['5', '-2', '4', 'C', 'D', '9', '+', '+'],), 27),
    ((['1'],), 1),
    (([],), 0),

]

if __name__ == "__main__":
    passed = 0
    for args, expected in TESTS:
        try:
            got = baseball_game(*args)
        except Exception as e:
            got = "ERROR: " + str(e)
        ok = got == expected
        passed += ok
        print(("PASS  " if ok else "FAIL  ") + "baseball_game" + repr(args) +
              " -> " + repr(got) + "   expected " + repr(expected))
    print()
    print(str(passed) + "/" + str(len(TESTS)) + " passed")
