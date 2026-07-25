"""SOLUTION - Fizz Buzz

Check divisibility by 15 before 3 and 5, since 15 satisfies both.
O(n).
"""


def fizz_buzz(n):
    out = []
    for i in range(1, n + 1):
        if i % 15 == 0:
            out.append("FizzBuzz")
        elif i % 3 == 0:
            out.append("Fizz")
        elif i % 5 == 0:
            out.append("Buzz")
        else:
            out.append(str(i))
    return out


TESTS = [
    ((5,), ['1', '2', 'Fizz', '4', 'Buzz']),
    ((3,), ['1', '2', 'Fizz']),
    ((15,), ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', '14', 'FizzBuzz']),
    ((1,), ['1']),

]

if __name__ == "__main__":
    passed = 0
    for args, expected in TESTS:
        got = fizz_buzz(*args)
        ok = got == expected
        passed += ok
        print(("PASS  " if ok else "FAIL  ") + repr(args) + " -> " + repr(got))
    print()
    print(str(passed) + "/" + str(len(TESTS)) + " passed")
