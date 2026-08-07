"""Reference answers for module 01 drills."""

# A. INDEX ARITHMETIC


def sum_range(nums, i, j):
    return sum(nums[i:j + 1])      # +1 because slices exclude the end


def swapped(nums, i, j):
    out = list(nums)               # copy first, never touch the caller's list
    out[i], out[j] = out[j], out[i]
    return out


def rotate_left(nums):
    return nums[1:] + nums[:1]


def rotate_right(nums):
    return nums[-1:] + nums[:-1]


def rotate_left_k(nums, k):
    if not nums:
        return []
    k = k % len(nums)              # k may exceed the length
    return nums[k:] + nums[:k]


def last_index_of(nums, target):
    for i in range(len(nums) - 1, -1, -1):
        if nums[i] == target:
            return i
    return -1


def second_largest(nums):
    distinct = sorted(set(nums), reverse=True)
    if len(distinct) < 2:
        return None
    return distinct[1]


def is_palindrome_list(nums):
    return nums == nums[::-1]


# B. BUILDING NEW LISTS


def without(nums, value):
    return [n for n in nums if n != value]


def clamp_negatives(nums):
    return [n if n > 0 else 0 for n in nums]


def move_zeros(nums):
    kept = [n for n in nums if n != 0]
    zeros = len(nums) - len(kept)
    return kept + [0] * zeros


def dedupe(nums):
    seen = set()
    out = []
    for n in nums:
        if n not in seen:
            seen.add(n)
            out.append(n)          # order preserved, unlike sorted(set(...))
    return out


def interleave(a, b):
    out = []
    for x, y in zip(a, b):
        out.append(x)
        out.append(y)
    return out


def chunk(nums, size):
    return [nums[i:i + size] for i in range(0, len(nums), size)]


def reverse_in_place(nums):
    left, right = 0, len(nums) - 1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1
    return nums                    # the caller's list really changed


def doubled(nums):
    return [n for n in nums for _ in range(2)]


# C. PREFIX SUMS AND RUNNING VALUES


def prefix_sums(nums):
    out = []
    so_far = 0
    for n in nums:
        so_far += n
        out.append(so_far)
    return out


def range_sum(nums, i, j):
    p = prefix_sums(nums)
    if i == 0:
        return p[j]
    return p[j] - p[i - 1]         # everything up to j, minus everything before i


def running_max(nums):
    out = []
    best = None
    for n in nums:
        best = n if best is None else max(best, n)
        out.append(best)
    return out


def average(nums):
    if not nums:
        return 0.0
    return sum(nums) / len(nums)


def count_below(nums, k):
    return len([n for n in nums if n < k])


def pivot_index(nums):
    grand = sum(nums)
    left = 0
    for i, n in enumerate(nums):
        # right side is everything except the left side and the pivot itself
        if left == grand - left - n:
            return i
        left += n
    return -1


# D. STRINGS


def reverse_words(s):
    return " ".join(s.split()[::-1])


def title_case(s):
    return " ".join(w[0].upper() + w[1:].lower() for w in s.split())


def is_palindrome(s):
    low = s.lower()
    return low == low[::-1]


def longest_word(s):
    best = ""
    for w in s.split():
        if len(w) > len(best):     # strict > keeps the FIRST on a tie
            best = w
    return best


def strip_vowels(s):
    return "".join(c for c in s if c not in "aeiou")


def positions(s):
    out = {}
    for i, c in enumerate(s):
        if c not in out:
            out[c] = []
        out[c].append(i)
    return out


def compress(s):
    if not s:
        return ""
    out = []
    current = s[0]
    count = 1
    for c in s[1:]:
        if c == current:
            count += 1
        else:
            out.append(current + str(count))
            current, count = c, 1
    out.append(current + str(count))   # the final run never hits the else
    return "".join(out)


def is_anagram(a, b):
    return sorted(a) == sorted(b)
