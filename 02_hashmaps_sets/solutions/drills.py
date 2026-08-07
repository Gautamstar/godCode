"""Reference answers for module 02 drills."""

# A. COUNTING


def freq(items):
    out = {}
    for x in items:
        out[x] = out.get(x, 0) + 1
    return out


def most_common(items):
    counts = freq(items)
    best = None
    # scan the ORIGINAL order so the first-seen wins a tie
    for x in items:
        if best is None or counts[x] > counts[best]:
            best = x
    return best


def count_unique(items):
    return len(set(items))


def appears_once(items):
    counts = freq(items)
    return sorted(x for x in counts if counts[x] == 1)


def same_letters(a, b):
    return freq(a) == freq(b)      # two dicts compare by content


def majority(nums):
    counts = freq(nums)
    return max(counts, key=counts.get)


def parity_counts(nums):
    out = {"even": 0, "odd": 0}    # both keys must exist even at zero
    for n in nums:
        if n % 2 == 0:
            out["even"] += 1
        else:
            out["odd"] += 1
    return out


def rarest_count(items):
    counts = freq(items)
    return min(counts.values())


# B. COMPLEMENT AND LOOKUP


def two_sum(nums, target):
    seen = {}                      # value -> index
    for i, n in enumerate(nums):
        want = target - n
        if want in seen:           # check BEFORE inserting, or n matches itself
            return [seen[want], i]
        seen[n] = i
    return []


def has_pair_summing(nums, target):
    seen = set()
    for n in nums:
        if target - n in seen:
            return True
        seen.add(n)
    return False


def has_duplicate(nums):
    return len(set(nums)) != len(nums)


def nearby_duplicate(nums, k):
    last = {}                      # value -> most recent index
    for i, n in enumerate(nums):
        if n in last and i - last[n] <= k:
            return True
        last[n] = i
    return False


def pairs_with_diff(nums, d):
    values = set(nums)
    return len([x for x in values if x + d in values])


def zero_subarray(nums):
    seen = {0}                     # seed with 0: a prefix can itself be zero
    total = 0
    for n in nums:
        total += n
        if total in seen:          # same running total twice means zero between
            return True
        seen.add(total)
    return False


def first_unique(s):
    counts = freq(s)
    for i, c in enumerate(s):      # second pass, in order
        if counts[c] == 1:
            return i
    return -1


# C. GROUPING


def group_anagrams(words):
    out = {}
    for w in words:
        key = "".join(sorted(w))   # identical for every anagram
        if key not in out:
            out[key] = []
        out[key].append(w)
    return out


def group_by_length(words):
    out = {}
    for w in words:
        out.setdefault(len(w), []).append(w)   # setdefault creates on first use
    return out


def group_by_parity(nums):
    out = {"even": [], "odd": []}
    for n in nums:
        out["even" if n % 2 == 0 else "odd"].append(n)
    return out


def index_map(items):
    out = {}
    for i, x in enumerate(items):
        if x not in out:           # only the FIRST index
            out[x] = i
    return out


def invert_multi(d):
    out = {}
    for key, value in d.items():
        out.setdefault(value, []).append(key)
    for value in out:
        out[value].sort()
    return out


def count_by_first_letter(words):
    out = {}
    for w in words:
        out[w[0]] = out.get(w[0], 0) + 1
    return out


def bucket(rows):
    out = {}
    for name, score in rows:       # unpacking the tuple in the for line
        out.setdefault(name, []).append(score)
    return out


# D. SETS


def intersect(a, b):
    return sorted(set(a) & set(b))


def subtract(a, b):
    return sorted(set(a) - set(b))


def either_not_both(a, b):
    return sorted(set(a) ^ set(b))


def is_subset(a, b):
    return set(a) <= set(b)


def all_distinct(s):
    return len(set(s)) == len(s)


def missing(nums):
    present = set(nums)
    for i in range(len(nums) + 1):
        if i not in present:
            return i
    return -1


def common_to_all(lists):
    if not lists:
        return []
    shared = set(lists[0])
    for rest in lists[1:]:
        shared &= set(rest)
    return sorted(shared)


def longest_run(nums):
    values = set(nums)
    best = 0
    for n in values:
        if n - 1 in values:
            continue               # not a run start, someone else will walk it
        length = 1
        while n + length in values:
            length += 1
        best = max(best, length)
    return best
