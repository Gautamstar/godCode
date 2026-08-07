// Reference answers for module 01. Implementations only; the test block lives
// in drills/01_pointers.cpp.

#include <cstddef>
#include <string>
#include <vector>

#include "../harness/drill_harness.hpp"

// A. POINTER BASICS

int* address_of(int& x) { return &x; }

int read_through(const int* p) { return *p; }

void write_through(int* p, int value) { *p = value; }

bool is_null(const int* p) { return p == nullptr; }

int value_or(const int* p, int fallback) {
    if (p == nullptr) return fallback;
    return *p;
}

void swap_via_pointers(int* a, int* b) {
    int held = *a;
    *a = *b;
    *b = held;
}

bool pointers_are_same_size() { return sizeof(int*) == sizeof(double*); }

bool refers_to_same(int& ref, const int* ptr) { return &ref == ptr; }

// B. POINTERS AND ARRAYS

int first_element(const int* arr) { return arr[0]; }

int element_at(const int* arr, std::size_t i) {
    return arr[i];  // identical to *(arr + i)
}

int sum_array(const int* arr, std::size_t n) {
    int total = 0;
    for (std::size_t i = 0; i < n; ++i) total += arr[i];
    return total;
}

std::size_t length_of_local_array() {
    int arr[5] = {1, 2, 3, 4, 5};
    // works because arr is a real array here. Pass it to a function and it
    // decays to a pointer, and this same expression silently becomes
    // sizeof(int*) / sizeof(int).
    return sizeof(arr) / sizeof(arr[0]);
}

const int* advance(const int* arr, std::size_t n) {
    return arr + n;  // moves n * sizeof(int) bytes
}

std::ptrdiff_t elements_between(const int* first, const int* last) {
    return last - first;  // a count of elements, not bytes
}

const int* find_first(const int* arr, std::size_t n, int target) {
    for (std::size_t i = 0; i < n; ++i)
        if (arr[i] == target) return arr + i;
    return nullptr;
}

void reverse_array(int* arr, std::size_t n) {
    if (n == 0) return;
    std::size_t left = 0;
    std::size_t right = n - 1;
    while (left < right) {
        int held = arr[left];
        arr[left] = arr[right];
        arr[right] = held;
        ++left;
        --right;
    }
}

// C. C STRINGS

std::size_t c_length(const char* s) {
    std::size_t n = 0;
    while (s[n] != '\0') ++n;  // walk to the terminator
    return n;
}

void c_copy(char* dst, const char* src) {
    std::size_t i = 0;
    while (src[i] != '\0') {
        dst[i] = src[i];
        ++i;
    }
    dst[i] = '\0';  // the terminator is not copied by the loop
}

bool c_equal(const char* a, const char* b) {
    std::size_t i = 0;
    while (a[i] != '\0' && b[i] != '\0') {
        if (a[i] != b[i]) return false;
        ++i;
    }
    return a[i] == b[i];  // both must have ended together
}

const char* c_find(const char* s, char ch) {
    for (std::size_t i = 0; s[i] != '\0'; ++i)
        if (s[i] == ch) return s + i;
    return nullptr;
}

int c_count(const char* s, char ch) {
    int found = 0;
    for (std::size_t i = 0; s[i] != '\0'; ++i)
        if (s[i] == ch) ++found;
    return found;
}

void c_upper(char* s) {
    for (std::size_t i = 0; s[i] != '\0'; ++i)
        if (s[i] >= 'a' && s[i] <= 'z') s[i] = static_cast<char>(s[i] - 32);
}

// D. CONST, INDIRECTION, AND OUT-PARAMETERS

void bump_through_const_pointer(int* const p) {
    *p += 1;  // writing through p is fine; p = something_else would not be
}

void repoint(int** pp, int* target) { *pp = target; }

int sum_pointed_to(const std::vector<int*>& ptrs) {
    int total = 0;
    for (int* p : ptrs)
        if (p != nullptr) total += *p;
    return total;
}

bool try_divide(int a, int b, int* out) {
    if (b == 0) return false;  // leave *out alone on failure
    *out = a / b;
    return true;
}

static int op_add(int a, int b) { return a + b; }
static int op_mul(int a, int b) { return a * b; }

int apply_op(char op, int a, int b) {
    int (*fn)(int, int) = nullptr;
    if (op == '+') fn = op_add;
    if (op == '*') fn = op_mul;
    if (fn == nullptr) return 0;
    return fn(a, b);
}

const int* max_element_ptr(const int* arr, std::size_t n) {
    if (n == 0) return nullptr;
    const int* best = arr;
    for (std::size_t i = 1; i < n; ++i)
        if (arr[i] > *best) best = arr + i;
    return best;
}
