"""SOLUTION - Backspace String Compare

Build each string with a stack: normal characters push, '#' pops (if anything is
there). Then compare. Writing a helper keeps it clean instead of duplicating the loop.
"""


def backspace_compare(s, t):
    def build(x):
        st = []
        for c in x:
            if c == "#":
                if st:
                    st.pop()
            else:
                st.append(c)
        return st

    return build(s) == build(t)


TESTS = [
    (('ab#c', 'ad#c'), True),
    (('ab##', 'c#d#'), True),
    (('a#c', 'b'), False),
    (('', ''), True),
    (('#a', 'a'), True),

]

if __name__ == "__main__":
    passed = 0
    for args, expected in TESTS:
        got = backspace_compare(*args)
        passed += (got == expected)
        print(("PASS  " if got == expected else "FAIL  ") + repr(args) + " -> " + repr(got))
    print()
    print(str(passed) + "/" + str(len(TESTS)) + " passed")
