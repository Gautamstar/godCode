"""SOLUTION - First Unique Character

Count first, then scan in order. Two passes but still O(n).
"""


def first_uniq_char(s):
    freq = {}
    for c in s:
        freq[c] = freq.get(c, 0) + 1
    for i, c in enumerate(s):
        if freq[c] == 1:
            return i
    return -1


TESTS = [
    (('leetcode',), 0),
    (('loveleetcode',), 2),
    (('aabb',), -1),
    (('',), -1),
    (('z',), 0),

]

if __name__ == "__main__":
    passed = 0
    for args, expected in TESTS:
        got = first_uniq_char(*args)
        ok = got == expected
        passed += ok
        print(("PASS  " if ok else "FAIL  ") + repr(args) + " -> " + repr(got))
    print()
    print(str(passed) + "/" + str(len(TESTS)) + " passed")
