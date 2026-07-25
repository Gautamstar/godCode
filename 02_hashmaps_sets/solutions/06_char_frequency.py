"""SOLUTION - Character Frequency

The classic counting idiom. dict.get(key, default) avoids a KeyError on the
first sighting of a character. O(n).
"""


def char_frequency(s):
    freq = {}
    for c in s:
        freq[c] = freq.get(c, 0) + 1
    return freq


TESTS = [
    (('aab',), {'a': 2, 'b': 1}),
    (('',), {}),
    (('abc',), {'a': 1, 'b': 1, 'c': 1}),
    (('aaa',), {'a': 3}),

]

if __name__ == "__main__":
    passed = 0
    for args, expected in TESTS:
        got = char_frequency(*args)
        ok = got == expected
        passed += ok
        print(("PASS  " if ok else "FAIL  ") + repr(args) + " -> " + repr(got))
    print()
    print(str(passed) + "/" + str(len(TESTS)) + " passed")
