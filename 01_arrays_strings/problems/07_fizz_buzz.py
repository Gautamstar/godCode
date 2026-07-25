"""
PROBLEM : Fizz Buzz
TOPIC   : Arrays / Logic
LEVEL   : Easy

    Return a list of strings for the numbers 1 through n where:
      - multiples of 3 and 5  -> "FizzBuzz"
      - multiples of 3        -> "Fizz"
      - multiples of 5        -> "Buzz"
      - everything else       -> the number as a string

Examples:
    fizz_buzz(5)  ->  ["1", "2", "Fizz", "4", "Buzz"]

Hint (only peek if you are stuck):
    Check the 15 case FIRST, otherwise 3 and 5 will steal it. Use str(i) to convert.

HOW TO RUN:  python 01_arrays_strings\problems\07_fizz_buzz.py
"""


def fizz_buzz(n):
    # YOUR CODE HERE
    pass


# --------------------------- tests: do not edit ---------------------------
TESTS = [
    ((5,), ['1', '2', 'Fizz', '4', 'Buzz']),
    ((3,), ['1', '2', 'Fizz']),
    ((15,), ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', '14', 'FizzBuzz']),
    ((1,), ['1']),

]

if __name__ == "__main__":
    passed = 0
    for args, expected in TESTS:
        try:
            got = fizz_buzz(*args)
        except Exception as e:
            got = "ERROR: " + str(e)
        ok = got == expected
        passed += ok
        print(("PASS  " if ok else "FAIL  ") + "fizz_buzz" + repr(args) +
              " -> " + repr(got) + "   expected " + repr(expected))
    print()
    print(str(passed) + "/" + str(len(TESTS)) + " passed")
