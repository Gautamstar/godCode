"""SOLUTION - Best Time to Buy and Sell Stock

One pass. At every day, the best sale today is today's price minus the cheapest
price seen before it. Keep both running values. O(n) time, O(1) space.
"""


def max_profit(prices):
    if not prices:
        return 0
    cheapest = prices[0]
    best = 0
    for p in prices:
        cheapest = min(cheapest, p)
        best = max(best, p - cheapest)
    return best


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
        got = max_profit(*args)
        passed += (got == expected)
        print(("PASS  " if got == expected else "FAIL  ") + repr(args) + " -> " + repr(got))
    print()
    print(str(passed) + "/" + str(len(TESTS)) + " passed")
