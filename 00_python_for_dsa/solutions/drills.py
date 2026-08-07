"""Reference answers for module 00 drills. Read one only after a real attempt,
then close it and rewrite from memory."""

# A. NUMBERS AND OPERATORS


def add(a, b):
    return a + b


def whole_divide(a, b):
    return a // b          # // floors; / would give a float


def remainder(a, b):
    return a % b


def power(a, b):
    return a ** b


def is_even(n):
    return n % 2 == 0      # already a bool, no if needed


def distance(n):
    return abs(n)


def to_int(n):
    return int(n)          # truncates toward zero, does not round


def smaller(a, b):
    if a < b:
        return a
    return b


# B. STRINGS


def shout(s):
    return s.upper()


def whisper(s):
    return s.lower()


def first_char(s):
    return s[0]


def last_char(s):
    return s[-1]


def char_count(s):
    return len(s)


def reverse_string(s):
    return s[::-1]


def contains(s, part):
    return part in s


def starts_with(s, part):
    return s.startswith(part)


def trim(s):
    return s.strip()


def split_words(s):
    return s.split()       # bare .split() also drops empty pieces


def join_words(words):
    return "-".join(words)


def only_digits(s):
    return "".join([c for c in s if c.isdigit()])


def count_char(s, ch):
    return s.count(ch)


def replace_all(s, old, new):
    return s.replace(old, new)


# C. LISTS: INDEXING AND SLICING


def last_element(nums):
    return nums[-1]


def first_three(nums):
    return nums[0:3]       # a short list just gives back what it has


def reverse_list(items):
    return items[::-1]


def last_two(nums):
    return nums[-2:]


def drop_first(nums):
    return nums[1:]


def every_other(nums):
    return nums[::2]


def middle(nums):
    return nums[len(nums) // 2]


def size(nums):
    return len(nums)


def with_added(nums, item):
    return nums + [item]   # .append mutates and returns None


def concat(a, b):
    return a + b


def has(nums, target):
    return target in nums


def position_of(nums, target):
    if target in nums:
        return nums.index(target)
    return -1


# D. LOOPS AND CONDITIONALS


def total(nums):
    running_total = 0
    for n in nums:
        running_total += n
    return running_total


def count_positive(nums):
    found = 0
    for n in nums:
        if n > 0:
            found += 1
    return found


def index_of_max(nums):
    best = 0
    for i, n in enumerate(nums):
        if n > nums[best]:
            best = i
    return best


def first_negative(nums):
    for n in nums:
        if n < 0:
            return n       # leave immediately, do not scan the rest
    return None


def all_even(nums):
    for n in nums:
        if n % 2 != 0:
            return False
    return True            # an empty list never enters the loop, so True


def any_negative(nums):
    for n in nums:
        if n < 0:
            return True
    return False


def largest(nums):
    best = nums[0]
    for n in nums:
        if n > best:
            best = n
    return best


def running(nums):
    out = []
    so_far = 0
    for n in nums:
        so_far += n
        out.append(so_far)
    return out


def fizz(n):
    if n % 3 == 0 and n % 5 == 0:   # both FIRST, or 15 never reaches here
        return "fizzbuzz"
    if n % 3 == 0:
        return "fizz"
    if n % 5 == 0:
        return "buzz"
    return str(n)


def sign_word(n):
    if n < 0:
        return "negative"
    if n == 0:
        return "zero"
    return "positive"


# E. DICTS AND SETS


def count_items(items):
    freq = {}
    for i in items:
        freq[i] = freq.get(i, 0) + 1   # .get avoids a KeyError on first sight
    return freq


def unique_sorted(items):
    return sorted(set(items))


def lookup(d, key, fallback):
    return d.get(key, fallback)


def has_key(d, key):
    return key in d        # `in` on a dict checks KEYS


def sorted_keys(d):
    return sorted(d)       # iterating a dict gives its keys


def sum_values(d):
    return sum(d.values())


def invert(d):
    out = {}
    for key, value in d.items():
        out[value] = key
    return out


def top_key(d):
    return max(d, key=d.get)


def in_both(a, b):
    return sorted(set(a) & set(b))


def only_in_first(a, b):
    return sorted(set(a) - set(b))


def in_either(a, b):
    return sorted(set(a) | set(b))


def first_repeat(nums):
    seen = set()
    for n in nums:
        if n in seen:      # check BEFORE adding, or everything looks repeated
            return n
        seen.add(n)
    return None


def two_sum(nums, target):
    seen = {}              # value -> index
    for i, n in enumerate(nums):
        want = target - n
        if want in seen:   # look before inserting, so n cannot match itself
            return [seen[want], i]
        seen[n] = i
    return []


def group_by_first(words):
    out = {}
    for w in words:
        key = w[0]
        if key not in out:
            out[key] = []  # create the bucket on first sighting
        out[key].append(w)
    return out


# F. COMPREHENSIONS


def doubled_evens(nums):
    return [n * 2 for n in nums if n % 2 == 0]


def squares(nums):
    return [n ** 2 for n in nums]


def long_words(words):
    return [w for w in words if len(w) > 3]


def lengths(words):
    return [len(w) for w in words]


def flatten(rows):
    return [item for row in rows for item in row]   # outer loop first


def length_map(words):
    return {w: len(w) for w in words}


def first_letters(words):
    return {w[0] for w in words}    # braces with no colon is a set


def sum_two_lists(a, b):
    return [x + y for x, y in zip(a, b)]


def upper_all(words):
    return [w.upper() for w in words]


def pairs(items):
    return list(enumerate(items))


# G. TUPLES, UNPACKING, FUNCTIONS


def swap(a, b):
    return (b, a)


def min_and_max(nums):
    return (min(nums), max(nums))


def difference(pair):
    a, b = pair
    return a - b


def add_all(*nums):
    return sum(nums)       # *args arrives as a tuple


def repeat(word, times=2):
    return " ".join([word] * times)


def zip_dict(keys, values):
    return dict(zip(keys, values))


# H. SORTING


def sort_desc(nums):
    return sorted(nums, reverse=True)


def by_length(words):
    return sorted(words, key=len)


def by_score(rows):
    return sorted(rows, key=lambda pair: pair[1], reverse=True)


def by_alpha(words):
    return sorted(words, key=str.lower)


def top_k(nums, k):
    return sorted(nums, reverse=True)[:k]


def sort_keys_by_value(d):
    return sorted(d, key=d.get)
