"""
PROBLEM : Best Time to Buy and Sell Stock
TOPIC   : Sliding Window
LEVEL   : Easy

    You may buy on one day and sell on a LATER day. Return the maximum profit,
    or 0 if no profit is possible.

Examples:
    max_profit([7,1,5,3,6,4])  ->  5    (buy at 1, sell at 6)
    max_profit([7,6,4,3,1])    ->  0

Hint (only peek if you are stuck):
    Track the cheapest price seen so far, and the best profit if you sold today.

HOW TO RUN:  python 05_sliding_window\problems\02_max_profit.py
"""


def max_profit(prices):
    # YOUR CODE HERE
    pass


# --------------------------- tests: do not edit ---------------------------
TESTS = [
    (([7, 1, 5, 3, 6, 4],), 5),
    (([7, 6, 4, 3, 1],), 0),
    (([],), 0),
    (([1],), 0),
    (([1, 2],), 1),

]

if __name__ == "__main__":
    passed = 0
    for args, expected in TESTS:
        try:
            got = max_profit(*args)
        except Exception as e:
            got = "ERROR: " + str(e)
        ok = got == expected
        passed += ok
        print(("PASS  " if ok else "FAIL  ") + "max_profit" + repr(args) +
              " -> " + repr(got) + "   expected " + repr(expected))
    print()
    print(str(passed) + "/" + str(len(TESTS)) + " passed")
