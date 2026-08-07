// MODULE 00 DRILLS - types, references, const, functions. 30 reps.
//
// Coming from Python, the thing to unlearn is that a variable is a name for an
// object somewhere else. In C++ a variable IS the object. Assigning copies.
// Passing copies. That single fact explains references, const&, and later the
// entire rule of five.
//
// RUN
//     make 00_basics
//     make 00_basics ARGS=12        one drill
//     make 00_basics ARGS=10-20     a range
//     make 00_basics ARGS=const     name substring
//     make 00_basics ARGS=-v        list passing drills too
//
// Replace TODO with your code. Do not edit the block at the bottom.

#include <climits>
#include <cstddef>
#include <string>
#include <vector>

#include "../harness/drill_harness.hpp"

// ===========================================================================
// A. TYPES, SIZES, CONVERSIONS
// ===========================================================================

// 1. Return a + b.
int add(int a, int b) { TODO; }

// 2. Integer division TRUNCATES toward zero, it does not floor.
//    trunc_div(7, 2) -> 3 and trunc_div(-7, 2) -> -3.
//    Python's // floors, so -7 // 2 is -4 there. This is a real difference.
int trunc_div(int a, int b) { TODO; }

// 3. Return a / b as a real number.  real_div(7, 2) -> 3.5
//    int / int is integer division no matter what you assign it to, so one
//    side has to become a double FIRST. static_cast<double>(a) / b.
double real_div(int a, int b) { TODO; }

// 4. Return sizeof(double), in bytes.
//    sizeof yields a std::size_t and is evaluated at compile time.
std::size_t size_of_double() { TODO; }

// 5. Return true when int is at least 32 bits wide on this machine.
//    Bits per byte is CHAR_BIT from <climits>, not always 8 in the standard
//    (though it is 8 everywhere you will actually work).
bool int_is_at_least_32_bits() { TODO; }

// 6. Add two bytes and let the result WRAP.
//    wrap_add(200, 100) -> 44        because 300 - 256 = 44
//    Both operands get promoted to int before the addition, so you must cast
//    the result back down explicitly. Unsigned overflow is defined behaviour
//    and wraps; SIGNED overflow is undefined and the sanitiser will catch it.
unsigned char wrap_add(unsigned char a, unsigned char b) { TODO; }

// 7. Return the result of comparing a signed -1 against an unsigned 1.
//    Return the value of the expression (-1 < 1u).
//    This is the classic trap: the int is converted to unsigned, -1 becomes a
//    huge number, and the comparison is FALSE. Never mix signed and unsigned
//    in a comparison. Your compiler warns about this for a reason.
bool minus_one_less_than_unsigned_one() { TODO; }

// 8. Convert a double to an int, truncating toward zero.
//    to_int(3.9) -> 3,  to_int(-3.9) -> -3
int to_int(double value) { TODO; }

// ===========================================================================
// B. REFERENCES AND VALUE SEMANTICS
// ===========================================================================

// 9. Add one to the caller's variable.
//    A reference parameter (int&) is another name for the caller's object,
//    not a copy of it.
void increment(int& n) { TODO; }

// 10. Take an int BY VALUE and add one to it. The caller must NOT change.
//     Write the body that modifies your local copy. The test checks the
//     caller's variable is untouched, which is the whole point.
void increment_copy(int n) { TODO; }

// 11. Return a REFERENCE to the element at index i, so the caller can assign
//     through it:  element_at(v, 1) = 99;
//     Returning `int` instead of `int&` would hand back a copy and the
//     assignment would not compile.
int& element_at(std::vector<int>& v, std::size_t i) { TODO; }

// 12. Swap two ints through references.
void swap_ints(int& a, int& b) { TODO; }

// 13. Sum a vector taken by CONST REFERENCE.
//     const std::vector<int>& means "I will read it and not copy it". Taking
//     it by value would copy every element on every call.
int sum(const std::vector<int>& v) { TODO; }

// 14. Append a value to the caller's vector.
void append(std::vector<int>& v, int value) { TODO; }

// 15. Return true when the two references name the SAME object.
//     Compare addresses with &a == &b. Comparing a == b would compare values.
bool same_object(const int& a, const int& b) { TODO; }

// 16. Return the number of elements, without changing anything.
//     .size() gives a std::size_t; the drill wants an int, so cast.
int count_of(const std::vector<int>& v) { TODO; }

// ===========================================================================
// C. CONST CORRECTNESS
// ===========================================================================

// 17. Return the first element of a const vector.
int first(const std::vector<int>& v) { TODO; }

// 18. Return a const REFERENCE to whichever string is longer. On a tie return
//     the first. The test checks you returned a reference to one of the
//     arguments rather than a copy, by comparing addresses.
const std::string& longer(const std::string& a, const std::string& b) { TODO; }

// 19. Set every element to `value`.
void fill_with(std::vector<int>& v, int value) { TODO; }

// 20. A counter whose value() is a const member function.
//     A const member function promises not to modify the object, which is
//     what lets you call it on a const Counter. Write both members.
class Counter {
public:
    explicit Counter(int start) : value_(start) {}
    void bump() { TODO; }
    int value() const { TODO; }

private:
    int value_ = 0;
};

// 21. Return the average as a double.
//     sum(v) / v.size() would be integer division AND mix signed with
//     unsigned. Cast the sum to double first.
double average(const std::vector<int>& v) { TODO; }

// 22. Return a pointer to a string literal.
//     The type is const char*, meaning "pointer to characters I must not
//     modify". Read it right to left: char, const, pointer.
const char* library_name() { TODO; }

// 23. Clamp v into [lo, hi].
int clamp(int v, int lo, int hi) { TODO; }

// ===========================================================================
// D. FUNCTIONS, OVERLOADS, LAMBDAS
// ===========================================================================

// 24. Greet someone. `greeting` DEFAULTS to "Hello".
//     greet("Gautam") -> "Hello, Gautam"
//     A default argument goes in the declaration, and every parameter after
//     one with a default must also have one.
std::string greet(const std::string& name, const std::string& greeting = "Hello") {
    TODO;
}

// 25. Two overloads of describe(). Same name, different parameter types; the
//     compiler picks by argument type at the call site.
//     describe(42) -> "int: 42",  describe("hi") -> "string: hi"
std::string describe(int value) { TODO; }
std::string describe(const std::string& value) { TODO; }

// 26. Apply a function passed as a FUNCTION POINTER.
//     apply(3, twice) -> 6
//     `int (*fn)(int)` reads as: fn is a pointer to a function taking int and
//     returning int.
int apply(int value, int (*fn)(int)) { TODO; }

// 27. Count how many values are greater than zero.
//     Write it with a plain loop, or with std::count_if and a lambda:
//       [](int n) { return n > 0; }
int count_positive(const std::vector<int>& v) { TODO; }

// 28. Sum a vector using a lambda that captures a running total BY REFERENCE.
//     [&total](int n) { total += n; } captures by reference, so the lambda
//     writes to the real variable. Capturing [total] by value would modify a
//     copy that is thrown away.
int sum_with_lambda(const std::vector<int>& v) { TODO; }

// 29. Return the larger of two values, using a TRAILING return type.
//     The signature is already written for you in that style; just fill in
//     the body. auto f(params) -> Type is the modern spelling, and it is
//     required when the return type depends on the parameters.
auto larger(int a, int b) -> int { TODO; }

// 30. Factorial, recursively. factorial(5) -> 120, factorial(0) -> 1.
long long factorial(int n) { TODO; }

// --------------------------- tests: do not edit ---------------------------

static int twice_helper(int n) { return n * 2; }

int main(int argc, char** argv) {
    return drill::run(
        {
            {"A. TYPES, SIZES, CONVERSIONS",
             {
                 {"add", [](drill::Check& c) { c.eq(add(2, 3), 5); c.eq(add(-1, 1), 0); }},
                 {"trunc_div",
                  [](drill::Check& c) {
                      c.eq(trunc_div(7, 2), 3);
                      c.eq(trunc_div(-7, 2), -3);
                  }},
                 {"real_div",
                  [](drill::Check& c) {
                      c.eq(real_div(7, 2), 3.5);
                      c.eq(real_div(1, 4), 0.25);
                  }},
                 {"size_of_double",
                  [](drill::Check& c) { c.eq(size_of_double(), sizeof(double)); }},
                 {"int_is_at_least_32_bits",
                  [](drill::Check& c) { c.is_true(int_is_at_least_32_bits()); }},
                 {"wrap_add",
                  [](drill::Check& c) {
                      c.eq(static_cast<int>(wrap_add(200, 100)), 44);
                      c.eq(static_cast<int>(wrap_add(1, 2)), 3);
                  }},
                 {"minus_one_less_than_unsigned_one",
                  [](drill::Check& c) { c.is_false(minus_one_less_than_unsigned_one()); }},
                 {"to_int",
                  [](drill::Check& c) { c.eq(to_int(3.9), 3); c.eq(to_int(-3.9), -3); }},
             }},
            {"B. REFERENCES AND VALUE SEMANTICS",
             {
                 {"increment",
                  [](drill::Check& c) {
                      int n = 5;
                      increment(n);
                      c.eq(n, 6);
                  }},
                 {"increment_copy",
                  [](drill::Check& c) {
                      int n = 5;
                      increment_copy(n);
                      c.eq(n, 5);
                  }},
                 {"element_at",
                  [](drill::Check& c) {
                      std::vector<int> v{1, 2, 3};
                      element_at(v, 1) = 99;
                      c.eq(v[1], 99);
                      c.eq(element_at(v, 0), 1);
                  }},
                 {"swap_ints",
                  [](drill::Check& c) {
                      int a = 1, b = 2;
                      swap_ints(a, b);
                      c.eq(a, 2);
                      c.eq(b, 1);
                  }},
                 {"sum",
                  [](drill::Check& c) {
                      c.eq(sum({1, 2, 3}), 6);
                      c.eq(sum({}), 0);
                  }},
                 {"append",
                  [](drill::Check& c) {
                      std::vector<int> v{1};
                      append(v, 2);
                      c.eq(v, std::vector<int>{1, 2});
                  }},
                 {"same_object",
                  [](drill::Check& c) {
                      int a = 5, b = 5;
                      c.is_false(same_object(a, b));
                      c.is_true(same_object(a, a));
                  }},
                 {"count_of",
                  [](drill::Check& c) {
                      c.eq(count_of({1, 2}), 2);
                      c.eq(count_of({}), 0);
                  }},
             }},
            {"C. CONST CORRECTNESS",
             {
                 {"first", [](drill::Check& c) { c.eq(first({7, 8}), 7); }},
                 {"longer",
                  [](drill::Check& c) {
                      std::string a = "hi", b = "there";
                      c.eq(longer(a, b), std::string("there"));
                      c.is_true(&longer(a, b) == &b, "return a reference, not a copy");
                      std::string x = "aa", y = "bb";
                      c.is_true(&longer(x, y) == &x, "on a tie return the first");
                  }},
                 {"fill_with",
                  [](drill::Check& c) {
                      std::vector<int> v{1, 2, 3};
                      fill_with(v, 9);
                      c.eq(v, std::vector<int>{9, 9, 9});
                  }},
                 {"Counter",
                  [](drill::Check& c) {
                      Counter counter(5);
                      counter.bump();
                      counter.bump();
                      const Counter& frozen = counter;
                      c.eq(frozen.value(), 7);
                  }},
                 {"average",
                  [](drill::Check& c) {
                      c.eq(average({1, 2}), 1.5);
                      c.eq(average({2, 2}), 2.0);
                  }},
                 {"library_name",
                  [](drill::Check& c) {
                      c.eq(std::string(library_name()), std::string("godCode"));
                  }},
                 {"clamp",
                  [](drill::Check& c) {
                      c.eq(clamp(5, 1, 3), 3);
                      c.eq(clamp(0, 1, 3), 1);
                      c.eq(clamp(2, 1, 3), 2);
                  }},
             }},
            {"D. FUNCTIONS, OVERLOADS, LAMBDAS",
             {
                 {"greet",
                  [](drill::Check& c) {
                      c.eq(greet("Gautam"), std::string("Hello, Gautam"));
                      c.eq(greet("Gautam", "Hey"), std::string("Hey, Gautam"));
                  }},
                 {"describe",
                  [](drill::Check& c) {
                      c.eq(describe(42), std::string("int: 42"));
                      c.eq(describe(std::string("hi")), std::string("string: hi"));
                  }},
                 {"apply",
                  [](drill::Check& c) { c.eq(apply(3, twice_helper), 6); }},
                 {"count_positive",
                  [](drill::Check& c) {
                      c.eq(count_positive({-1, 2, 3}), 2);
                      c.eq(count_positive({}), 0);
                  }},
                 {"sum_with_lambda",
                  [](drill::Check& c) {
                      c.eq(sum_with_lambda({1, 2, 3}), 6);
                      c.eq(sum_with_lambda({}), 0);
                  }},
                 {"larger",
                  [](drill::Check& c) { c.eq(larger(2, 5), 5); c.eq(larger(5, 2), 5); }},
                 {"factorial",
                  [](drill::Check& c) {
                      c.eq(factorial(5), 120LL);
                      c.eq(factorial(0), 1LL);
                  }},
             }},
        },
        argc, argv);
}
