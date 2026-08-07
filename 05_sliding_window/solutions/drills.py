"""Reference answers for module 05 drills."""

VOWELS = "aeiou"


# A. FIXED WIDTH


def window_sums(nums, k):
    if k > len(nums):
        return []
    total = sum(nums[:k])
    out = [total]
    for i in range(k, len(nums)):
        total += nums[i] - nums[i - k]     # add what entered, drop what left
        out.append(total)
    return out


def max_sum_k(nums, k):
    return max(window_sums(nums, k))


def min_sum_k(nums, k):
    return min(window_sums(nums, k))


def max_avg_k(nums, k):
    return max(window_sums(nums, k)) / k


def count_windows_above(nums, k, t):
    return len([s for s in window_sums(nums, k) if s > t])


def first_window_index(nums, k, target):
    for i, s in enumerate(window_sums(nums, k)):
        if s == target:
            return i
    return -1


def max_vowels_k(s, k):
    if k > len(s):
        return 0
    count = sum(1 for c in s[:k] if c in VOWELS)
    best = count
    for i in range(k, len(s)):
        if s[i] in VOWELS:
            count += 1
        if s[i - k] in VOWELS:
            count -= 1
        best = max(best, count)
    return best


def window_maxes(nums, k):
    return [max(nums[i:i + k]) for i in range(len(nums) - k + 1)]


# B. VARIABLE WIDTH


def longest_no_repeat(s):
    inside = set()
    left = 0
    best = 0
    for right, c in enumerate(s):
        while c in inside:            # shrink until the new char is allowed
            inside.remove(s[left])
            left += 1
        inside.add(c)
        best = max(best, right - left + 1)
    return best


def min_len_at_least(nums, target):
    left = 0
    total = 0
    best = None
    for right, n in enumerate(nums):
        total += n
        while total >= target:        # valid, so try to shrink it further
            width = right - left + 1
            best = width if best is None else min(best, width)
            total -= nums[left]
            left += 1
    return best if best is not None else 0


def longest_ones(nums, k):
    left = 0
    zeros = 0
    best = 0
    for right, n in enumerate(nums):
        if n == 0:
            zeros += 1
        while zeros > k:
            if nums[left] == 0:
                zeros -= 1
            left += 1
        best = max(best, right - left + 1)
    return best


def count_subarrays_sum(nums, target):
    left = 0
    total = 0
    found = 0
    for right, n in enumerate(nums):
        total += n
        while total > target and left <= right:
            total -= nums[left]
            left += 1
        if total == target:
            found += 1
    return found


def longest_k_distinct(s, k):
    counts = {}
    left = 0
    best = 0
    for right, c in enumerate(s):
        counts[c] = counts.get(c, 0) + 1
        while len(counts) > k:
            counts[s[left]] -= 1
            if counts[s[left]] == 0:
                del counts[s[left]]   # delete, or len() keeps counting it
            left += 1
        best = max(best, right - left + 1)
    return best


def max_two_types(nums):
    counts = {}
    left = 0
    best = 0
    for right, n in enumerate(nums):
        counts[n] = counts.get(n, 0) + 1
        while len(counts) > 2:
            counts[nums[left]] -= 1
            if counts[nums[left]] == 0:
                del counts[nums[left]]
            left += 1
        best = max(best, right - left + 1)
    return best


def smallest_window(s, needed):
    if not needed:
        return 0
    want = {}
    for c in needed:
        want[c] = want.get(c, 0) + 1
    missing = len(needed)
    left = 0
    best = None
    for right, c in enumerate(s):
        if want.get(c, 0) > 0:
            missing -= 1              # only counts while we still need it
        want[c] = want.get(c, 0) - 1
        while missing == 0:
            width = right - left + 1
            best = width if best is None else min(best, width)
            want[s[left]] += 1
            if want[s[left]] > 0:
                missing += 1
            left += 1
    return best if best is not None else 0


def longest_after_replace(s, k):
    counts = {}
    left = 0
    best = 0
    most = 0
    for right, c in enumerate(s):
        counts[c] = counts.get(c, 0) + 1
        most = max(most, counts[c])
        # everything that is not the most common character must be replaced
        while (right - left + 1) - most > k:
            counts[s[left]] -= 1
            left += 1
            most = max(counts.values())
        best = max(best, right - left + 1)
    return best


def longest_k_odds(nums, k):
    left = 0
    odds = 0
    best = 0
    for right, n in enumerate(nums):
        if n % 2 != 0:
            odds += 1
        while odds > k:
            if nums[left] % 2 != 0:
                odds -= 1
            left += 1
        best = max(best, right - left + 1)
    return best


def longest_sum_at_most(nums, t):
    left = 0
    total = 0
    best = 0
    for right, n in enumerate(nums):
        total += n
        while total > t and left <= right:
            total -= nums[left]
            left += 1
        best = max(best, right - left + 1)
    return best


# C. STRING WINDOWS


def _counts(text):
    out = {}
    for c in text:
        out[c] = out.get(c, 0) + 1
    return out


def anagram_indices(s, p):
    k = len(p)
    if k > len(s):
        return []
    target = _counts(p)
    window = _counts(s[:k])
    out = []
    if window == target:
        out.append(0)
    for i in range(k, len(s)):
        window[s[i]] = window.get(s[i], 0) + 1
        window[s[i - k]] -= 1
        if window[s[i - k]] == 0:
            del window[s[i - k]]      # so the dicts compare equal
        if window == target:
            out.append(i - k + 1)
    return out


def contains_permutation(s, p):
    return len(anagram_indices(s, p)) > 0


def distinct_windows(s, k):
    if k > len(s):
        return 0
    return len({s[i:i + k] for i in range(len(s) - k + 1)})


def all_windows(s, k):
    if k > len(s):
        return []
    return [s[i:i + k] for i in range(len(s) - k + 1)]


def max_distinct_window(s, k):
    best = 0
    for w in all_windows(s, k):
        best = max(best, len(set(w)))
    return best


def count_all_distinct_windows(s, k):
    return len([w for w in all_windows(s, k) if len(set(w)) == k])
