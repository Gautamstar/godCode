"""Reference answers for module 03 drills."""

VOWELS = "aeiouAEIOU"


# A. CONVERGING FROM BOTH ENDS


def reverse_in_place(nums):
    left, right = 0, len(nums) - 1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1
    return nums


def is_palindrome(s):
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True


def two_sum_sorted(nums, target):
    left, right = 0, len(nums) - 1
    while left < right:
        total = nums[left] + nums[right]
        if total == target:
            return [left, right]
        if total < target:
            left += 1          # need more, and only the left can grow
        else:
            right -= 1         # need less, and only the right can shrink
    return []


def has_pair_sorted(nums, target):
    return two_sum_sorted(nums, target) != []


def count_pairs_sorted(nums, target):
    found = 0
    left, right = 0, len(nums) - 1
    while left < right:
        total = nums[left] + nums[right]
        if total == target:
            found += 1
            left += 1
            right -= 1
        elif total < target:
            left += 1
        else:
            right -= 1
    return found


def is_clean_palindrome(s):
    left, right = 0, len(s) - 1
    while left < right:
        # skip anything that is not a letter or digit, on either side
        if not s[left].isalnum():
            left += 1
        elif not s[right].isalnum():
            right -= 1
        elif s[left].lower() != s[right].lower():
            return False
        else:
            left += 1
            right -= 1
    return True


def reverse_vowels(s):
    chars = list(s)
    left, right = 0, len(chars) - 1
    while left < right:
        if chars[left] not in VOWELS:
            left += 1
        elif chars[right] not in VOWELS:
            right -= 1
        else:                  # both are vowels, so swap
            chars[left], chars[right] = chars[right], chars[left]
            left += 1
            right -= 1
    return "".join(chars)


def max_water(heights):
    best = 0
    left, right = 0, len(heights) - 1
    while left < right:
        height = min(heights[left], heights[right])
        best = max(best, height * (right - left))
        # width only shrinks from here, so the only hope is a taller wall.
        # moving the taller side can never help.
        if heights[left] < heights[right]:
            left += 1
        else:
            right -= 1
    return best


def closest_sum(nums, target):
    best = nums[0] + nums[1]
    left, right = 0, len(nums) - 1
    while left < right:
        total = nums[left] + nums[right]
        if abs(total - target) < abs(best - target):
            best = total
        if total < target:
            left += 1
        elif total > target:
            right -= 1
        else:
            return total
    return best


# B. SAME DIRECTION: READ AND WRITE POINTERS


def remove_value(nums, value):
    write = 0
    for read in range(len(nums)):
        if nums[read] != value:
            nums[write] = nums[read]
            write += 1         # only advances when something is KEPT
    return write


def dedupe_sorted(nums):
    if not nums:
        return 0
    write = 1
    for read in range(1, len(nums)):
        if nums[read] != nums[write - 1]:   # compare to the last thing WRITTEN
            nums[write] = nums[read]
            write += 1
    return write


def move_zeros(nums):
    write = 0
    for read in range(len(nums)):
        if nums[read] != 0:
            nums[write] = nums[read]
            write += 1
    for i in range(write, len(nums)):
        nums[i] = 0            # everything past the write head is zero
    return nums


def merge_sorted(a, b):
    out = []
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            out.append(a[i])
            i += 1
        else:
            out.append(b[j])
            j += 1
    out.extend(a[i:])          # one of these is always empty
    out.extend(b[j:])
    return out


def partition_even_first(nums):
    return [n for n in nums if n % 2 == 0] + [n for n in nums if n % 2 != 0]


def sorted_squares(nums):
    out = [0] * len(nums)
    left, right = 0, len(nums) - 1
    for slot in range(len(nums) - 1, -1, -1):   # fill back to front
        if abs(nums[left]) > abs(nums[right]):
            out[slot] = nums[left] ** 2
            left += 1
        else:
            out[slot] = nums[right] ** 2
            right -= 1
    return out


def intersect_sorted(a, b):
    out = []
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] == b[j]:
            if not out or out[-1] != a[i]:      # collapse duplicates
                out.append(a[i])
            i += 1
            j += 1
        elif a[i] < b[j]:
            i += 1
        else:
            j += 1
    return out


def is_subsequence(small, big):
    i = 0
    for c in big:
        if i < len(small) and small[i] == c:
            i += 1             # advance the small pointer only on a match
    return i == len(small)


def compact(nums):
    out = []
    for n in nums:
        if not out or out[-1] != n:
            out.append(n)
    return out


# C. SCANNING WITH TWO CURSORS


def middle_slow_fast(nums):
    slow = fast = 0
    while fast + 1 < len(nums):
        slow += 1
        fast += 2
    return nums[slow]


def nth_from_end(nums, n):
    lead = n                   # put the lead pointer n ahead
    trail = 0
    while lead < len(nums):
        lead += 1
        trail += 1
    return nums[trail]


def longest_run(nums):
    if not nums:
        return 0
    best = 1
    length = 1
    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            length += 1
            best = max(best, length)
        else:
            length = 1
    return best


def min_gap_sorted(nums):
    best = None
    for i in range(1, len(nums)):
        gap = nums[i] - nums[i - 1]
        best = gap if best is None else min(best, gap)
    return best


def count_distinct_sorted(nums):
    found = 0
    for i, n in enumerate(nums):
        if i == 0 or n != nums[i - 1]:
            found += 1
    return found


def merge_intervals(intervals):
    out = []
    for start, end in intervals:
        if out and start <= out[-1][1]:         # overlaps the last one
            out[-1] = (out[-1][0], max(out[-1][1], end))
        else:
            out.append((start, end))
    return out


def _apply_backspaces(s):
    out = []
    for c in s:
        if c == "#":
            if out:
                out.pop()      # step the write head back
        else:
            out.append(c)
    return "".join(out)


def backspace_equal(a, b):
    return _apply_backspaces(a) == _apply_backspaces(b)


def repeats_sorted(nums):
    ordered = sorted(nums)
    out = []
    for i in range(1, len(ordered)):
        if ordered[i] == ordered[i - 1]:
            if not out or out[-1] != ordered[i]:
                out.append(ordered[i])
    return out
