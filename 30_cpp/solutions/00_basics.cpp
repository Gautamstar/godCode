// Reference answers for module 00. Read one only after a real attempt, then
// close it and rewrite from memory.
//
// This file holds the implementations only. The test block lives in
// drills/00_basics.cpp.

#include <climits>
#include <cstddef>
#include <string>
#include <vector>

#include "../harness/drill_harness.hpp"

// A. TYPES, SIZES, CONVERSIONS

int add(int a, int b) { return a + b; }

// truncates toward zero since C++11, so -7/2 is -3, not Python's -4
int trunc_div(int a, int b) { return a / b; }

double real_div(int a, int b) {
    // the cast must happen BEFORE the division, or you divide as ints and
    // then widen a number that has already lost its fraction
    return static_cast<double>(a) / b;
}

std::size_t size_of_double() { return sizeof(double); }

bool int_is_at_least_32_bits() { return sizeof(int) * CHAR_BIT >= 32; }

unsigned char wrap_add(unsigned char a, unsigned char b) {
    // a and b are promoted to int, so a + b is 300 here. Narrowing back is
    // where the wrap happens, and it has to be explicit.
    return static_cast<unsigned char>(a + b);
}

bool minus_one_less_than_unsigned_one() {
    // Written directly as (-1 < 1u) this compiles with a -Wsign-compare
    // warning and evaluates to FALSE, because the int is converted to
    // unsigned first and -1 becomes 4294967295. The cast below says the same
    // thing out loud.
    return static_cast<unsigned>(-1) < 1u;
}

int to_int(double value) { return static_cast<int>(value); }

// B. REFERENCES AND VALUE SEMANTICS

void increment(int& n) { n += 1; }

void increment_copy(int n) {
    n += 1;  // n is a copy; the caller never sees this
}

int& element_at(std::vector<int>& v, std::size_t i) { return v[i]; }

void swap_ints(int& a, int& b) {
    int held = a;
    a = b;
    b = held;
}

int sum(const std::vector<int>& v) {
    int total = 0;
    for (int n : v) total += n;
    return total;
}

void append(std::vector<int>& v, int value) { v.push_back(value); }

bool same_object(const int& a, const int& b) {
    return &a == &b;  // addresses, not values
}

int count_of(const std::vector<int>& v) { return static_cast<int>(v.size()); }

// C. CONST CORRECTNESS

int first(const std::vector<int>& v) { return v[0]; }

const std::string& longer(const std::string& a, const std::string& b) {
    // >= keeps the FIRST on a tie
    return a.size() >= b.size() ? a : b;
}

void fill_with(std::vector<int>& v, int value) {
    for (int& slot : v) slot = value;  // int& so the assignment lands in v
}

class Counter {
public:
    explicit Counter(int start) : value_(start) {}
    void bump() { value_ += 1; }
    // const promises not to modify, which is what allows calling it on a
    // const Counter&
    int value() const { return value_; }

private:
    int value_ = 0;
};

double average(const std::vector<int>& v) {
    return static_cast<double>(sum(v)) / static_cast<double>(v.size());
}

const char* library_name() { return "godCode"; }

int clamp(int v, int lo, int hi) {
    if (v < lo) return lo;
    if (v > hi) return hi;
    return v;
}

// D. FUNCTIONS, OVERLOADS, LAMBDAS

std::string greet(const std::string& name, const std::string& greeting = "Hello") {
    return greeting + ", " + name;
}

std::string describe(int value) { return "int: " + std::to_string(value); }
std::string describe(const std::string& value) { return "string: " + value; }

int apply(int value, int (*fn)(int)) { return fn(value); }

int count_positive(const std::vector<int>& v) {
    int found = 0;
    for (int n : v)
        if (n > 0) ++found;
    return found;
}

int sum_with_lambda(const std::vector<int>& v) {
    int total = 0;
    auto add_one = [&total](int n) { total += n; };  // & captures the real total
    for (int n : v) add_one(n);
    return total;
}

auto larger(int a, int b) -> int { return a > b ? a : b; }

long long factorial(int n) {
    if (n <= 1) return 1;
    return n * factorial(n - 1);
}
