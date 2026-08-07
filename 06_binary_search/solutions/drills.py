"""Reference answers for module 06 drills."""

# A. THE INVARIANT


def binary_search(nums, target):
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            lo = mid + 1       # the +1 is what guarantees progress
        else:
            hi = mid - 1
    return -1


def binary_search_rec(nums, target, lo=0, hi=None):
    if hi is None:
        hi = len(nums) - 1
    if lo > hi:                # empty range, not found
        return -1
    mid = (lo + hi) // 2
    if nums[mid] == target:
        return mid
    if nums[mid] < target:
        return binary_search_rec(nums, target, mid + 1, hi)
    return binary_search_rec(nums, target, lo, mid - 1)


def first_index(nums, target):
    lo, hi = 0, len(nums) - 1
    found = -1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            found = mid
            hi = mid - 1       # record it, then keep looking LEFT
        elif nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return found


def last_index(nums, target):
    lo, hi = 0, len(nums) - 1
    found = -1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            found = mid
            lo = mid + 1       # keep looking RIGHT
        elif nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return found


def count_of(nums, target):
    first = first_index(nums, target)
    if first == -1:
        return 0
    return last_index(nums, target) - first + 1


def insert_position(nums, target):
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return lo                  # lo lands on the insertion point


def exists(nums, target):
    return binary_search(nums, target) != -1


def closest(nums, target):
    pos = insert_position(nums, target)
    best = None
    for i in (pos - 1, pos):   # only the two neighbours can win
        if 0 <= i < len(nums):
            if best is None or abs(nums[i] - target) < abs(best - target):
                best = nums[i]
    return best


# B. BOUNDS AND PREDICATES


def floor_value(nums, x):
    lo, hi = 0, len(nums) - 1
    best = None
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] <= x:
            best = nums[mid]
            lo = mid + 1       # valid, but maybe a bigger one also fits
        else:
            hi = mid - 1
    return best


def ceil_value(nums, x):
    lo, hi = 0, len(nums) - 1
    best = None
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] >= x:
            best = nums[mid]
            hi = mid - 1
        else:
            lo = mid + 1
    return best


def count_at_most(nums, x):
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] <= x:
            lo = mid + 1
        else:
            hi = mid - 1
    return lo


def first_true(flags):
    lo, hi = 0, len(flags) - 1
    found = -1
    while lo <= hi:
        mid = (lo + hi) // 2
        if flags[mid]:
            found = mid
            hi = mid - 1
        else:
            lo = mid + 1
    return found


def last_false(flags):
    lo, hi = 0, len(flags) - 1
    found = -1
    while lo <= hi:
        mid = (lo + hi) // 2
        if not flags[mid]:
            found = mid
            lo = mid + 1
        else:
            hi = mid - 1
    return found


def sqrt_floor(n):
    lo, hi = 0, n
    best = 0
    while lo <= hi:
        mid = (lo + hi) // 2
        if mid * mid <= n:
            best = mid
            lo = mid + 1
        else:
            hi = mid - 1
    return best


def peak_index(nums):
    lo, hi = 0, len(nums) - 1
    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid] < nums[mid + 1]:
            lo = mid + 1       # still climbing, peak is to the right
        else:
            hi = mid           # falling, peak is here or left
    return lo


def min_rotated(nums):
    lo, hi = 0, len(nums) - 1
    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid] > nums[hi]:
            lo = mid + 1       # the dip is in the right half
        else:
            hi = mid
    return nums[lo]


# C. ROTATION, AND SEARCHING THE ANSWER


def rotation_count(nums):
    lo, hi = 0, len(nums) - 1
    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid] > nums[hi]:
            lo = mid + 1
        else:
            hi = mid
    return lo                  # the index of the minimum


def search_rotated(nums, target):
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            return mid
        if nums[lo] <= nums[mid]:          # the left half is properly sorted
            if nums[lo] <= target < nums[mid]:
                hi = mid - 1
            else:
                lo = mid + 1
        else:                              # then the right half must be
            if nums[mid] < target <= nums[hi]:
                lo = mid + 1
            else:
                hi = mid - 1
    return -1


def first_bad(n, bad):
    lo, hi = 1, n
    while lo < hi:
        mid = (lo + hi) // 2
        if mid >= bad:         # this is the "is it broken?" check
            hi = mid
        else:
            lo = mid + 1
    return lo


def count_negatives(nums):
    lo, hi = 0, len(nums) - 1
    first = len(nums)          # index of the first negative, if any
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] < 0:
            first = mid
            hi = mid - 1
        else:
            lo = mid + 1
    return len(nums) - first


def smallest_square_at_least(n):
    lo, hi = 0, max(n, 1)
    best = hi
    while lo <= hi:
        mid = (lo + hi) // 2
        if mid * mid >= n:
            best = mid
            hi = mid - 1
        else:
            lo = mid + 1
    return best


def two_sum_bs(nums, target):
    for i, n in enumerate(nums):
        want = target - n
        lo, hi = i + 1, len(nums) - 1      # search only to the right
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] == want:
                return [i, mid]
            if nums[mid] < want:
                lo = mid + 1
            else:
                hi = mid - 1
    return []


def _days_needed(weights, capacity):
    days = 1
    load = 0
    for w in weights:
        if load + w > capacity:
            days += 1
            load = 0
        load += w
    return days


def min_capacity(weights, days):
    # any capacity below max(weights) can never move the heaviest item
    lo, hi = max(weights), sum(weights)
    best = hi
    while lo <= hi:
        mid = (lo + hi) // 2
        if _days_needed(weights, mid) <= days:
            best = mid
            hi = mid - 1       # it worked, so try a smaller ship
        else:
            lo = mid + 1
    return best


def _hours_needed(piles, speed):
    total = 0
    for p in piles:
        total += -(-p // speed)            # ceiling division without math
    return total


def min_speed(piles, hours):
    lo, hi = 1, max(piles)
    best = hi
    while lo <= hi:
        mid = (lo + hi) // 2
        if _hours_needed(piles, mid) <= hours:
            best = mid
            hi = mid - 1
        else:
            lo = mid + 1
    return best
