// MODULE 01 DRILLS - pointers, arrays, C strings. 28 reps.
//
// A pointer is a variable holding an ADDRESS. That is all it is. Everything
// confusing about them comes from three separate ideas wearing the same
// asterisk:
//
//     int* p;      declaring:  p is a pointer to int
//     *p           dereferencing: the int p points at
//     &x           taking the address of x
//
// References are pointers with the sharp edges removed: always valid, never
// reseated, no dereference syntax. Use references by default. Use raw pointers
// when the thing may be absent (nullptr) or when you are walking memory.
//
// The sanitiser is on. A dangling read or an out-of-bounds index will abort
// with a stack trace instead of quietly returning garbage. That is the single
// most useful thing in this module.
//
// RUN
//     make 01_pointers
//     make 01_pointers ARGS=14
//     make 01_pointers ARGS=10-20
//     make 01_pointers ARGS=array
//     make 01_pointers ARGS=-v

#include <cstddef>
#include <string>
#include <vector>

#include "../harness/drill_harness.hpp"

// ===========================================================================
// A. POINTER BASICS
// ===========================================================================

// 1. Return the address of the referenced int.
//    & on a variable means "address of". On a type it means "reference to".
//    Same symbol, two unrelated jobs.
int* address_of(int& x) { TODO; }

// 2. Return the value a pointer points at.
//    * on a pointer variable means "the thing at that address".
int read_through(const int* p) { TODO; }

// 3. Write `value` into whatever p points at.
void write_through(int* p, int value) { TODO; }

// 4. Return true when the pointer holds no address.
//    Compare against nullptr. Not NULL, which is a macro for 0, and not 0.
bool is_null(const int* p) { TODO; }

// 5. Return what p points at, or `fallback` when p is null.
//    This is why raw pointers still exist: a reference cannot be absent.
int value_or(const int* p, int fallback) { TODO; }

// 6. Swap two ints through pointers. Note the extra syntax compared to the
//    reference version in module 00. That is the argument for references.
void swap_via_pointers(int* a, int* b) { TODO; }

// 7. Return true when a pointer is the same size regardless of what it points
//    at. Compare sizeof(int*) with sizeof(double*).
//    Both are just addresses, so both are the machine's word size.
bool pointers_are_same_size() { TODO; }

// 8. Return true when `ref` and `ptr` refer to the same object.
//    A reference has no address of its own; &ref gives the address of the
//    thing it names.
bool refers_to_same(int& ref, const int* ptr) { TODO; }

// ===========================================================================
// B. POINTERS AND ARRAYS
// ===========================================================================
//
// An array name converts to a pointer to its first element the moment you
// pass it anywhere. That conversion is called DECAY, and it is why a function
// taking `const int*` has no idea how long the array is. You must pass the
// length separately. This is the single largest source of C-style bugs, and
// the reason std::vector and std::span exist.

// 9. Return the first element.
int first_element(const int* arr) { TODO; }

// 10. Return the element at index i.
//     arr[i] and *(arr + i) are exactly the same thing. The subscript
//     operator is defined as pointer arithmetic.
int element_at(const int* arr, std::size_t i) { TODO; }

// 11. Sum n elements.
int sum_array(const int* arr, std::size_t n) { TODO; }

// 12. Return how many elements are in the local array declared inside this
//     function. Use sizeof(arr) / sizeof(arr[0]).
//     This works ONLY on a real array. Do it on a parameter and you get
//     sizeof(pointer) / sizeof(element), which is nonsense that compiles.
std::size_t length_of_local_array() { TODO; }

// 13. Return a pointer to the element n places past `arr`.
//     Pointer arithmetic moves in units of the pointed-to TYPE, not bytes:
//     arr + 1 advances by sizeof(int), not by 1.
const int* advance(const int* arr, std::size_t n) { TODO; }

// 14. Return how many elements lie between two pointers into the same array.
//     Subtracting pointers gives a std::ptrdiff_t, a count of ELEMENTS.
std::ptrdiff_t elements_between(const int* first, const int* last) { TODO; }

// 15. Return a pointer to the first element equal to target, or nullptr.
//     Returning a pointer is how C says "found it, or not".
const int* find_first(const int* arr, std::size_t n, int target) { TODO; }

// 16. Reverse n elements in place, using two pointers walking toward each
//     other. Same shape as the Python two-pointer drill, different syntax.
void reverse_array(int* arr, std::size_t n) { TODO; }

// ===========================================================================
// C. C STRINGS
// ===========================================================================
//
// A C string is a char array whose end is marked by a '\0' byte. Nothing
// records its length; you find the end by walking. Every buffer overflow in
// the history of the language lives in this idea.

// 17. Return the length, not counting the terminator. Do not call strlen.
std::size_t c_length(const char* s) { TODO; }

// 18. Copy src into dst, terminator included. Assume dst is large enough.
void c_copy(char* dst, const char* src) { TODO; }

// 19. Return true when the two strings have the same characters.
//     Comparing with == would compare ADDRESSES, which is almost never what
//     you want and is why std::string exists.
bool c_equal(const char* a, const char* b) { TODO; }

// 20. Return a pointer to the first occurrence of ch, or nullptr.
const char* c_find(const char* s, char ch) { TODO; }

// 21. Count how many times ch appears.
int c_count(const char* s, char ch) { TODO; }

// 22. Uppercase the string in place. Only touch 'a' through 'z'.
//     A lowercase letter is 32 above its uppercase form in ASCII.
void c_upper(char* s) { TODO; }

// ===========================================================================
// D. CONST, INDIRECTION, AND OUT-PARAMETERS
// ===========================================================================

// 23. Add one to the pointed-to int. The parameter is `int* const`, meaning
//     the POINTER is const but the int is not. Read declarations right to
//     left: p is a const pointer to int.
//
//         const int* p    pointer to const int   (cannot write *p)
//         int* const p    const pointer to int   (cannot reseat p)
//         const int* const p   neither
void bump_through_const_pointer(int* const p) { TODO; }

// 24. Point *pp at `target`. A pointer-to-pointer is how you change the
//     caller's POINTER rather than the thing it points at.
void repoint(int** pp, int* target) { TODO; }

// 25. Sum the values behind a vector of pointers, skipping any nullptr.
int sum_pointed_to(const std::vector<int*>& ptrs) { TODO; }

// 26. Divide a by b. Return false when b is zero and leave *out untouched;
//     otherwise write the result to *out and return true.
//     This is the classic C out-parameter pattern, and it is why modern C++
//     reaches for std::optional instead.
bool try_divide(int a, int b, int* out) { TODO; }

// 27. Apply an operation chosen by character, using a function pointer.
//     '+' adds, '*' multiplies, anything else returns 0.
//     Declare the pointer as: int (*fn)(int, int)
int apply_op(char op, int a, int b) { TODO; }

// 28. Return a pointer to the LARGEST element, or nullptr when n is 0.
//     Returning a pointer into someone else's array is fine, as long as the
//     array outlives the pointer. Getting that wrong is a dangling pointer,
//     which the sanitiser will catch for you here but not in production.
const int* max_element_ptr(const int* arr, std::size_t n) { TODO; }

// --------------------------- tests: do not edit ---------------------------

static int add_op(int a, int b) { return a + b; }

int main(int argc, char** argv) {
    return drill::run(
        {
            {"A. POINTER BASICS",
             {
                 {"address_of",
                  [](drill::Check& c) {
                      int x = 5;
                      c.is_true(address_of(x) == &x);
                  }},
                 {"read_through",
                  [](drill::Check& c) {
                      int x = 7;
                      c.eq(read_through(&x), 7);
                  }},
                 {"write_through",
                  [](drill::Check& c) {
                      int x = 1;
                      write_through(&x, 9);
                      c.eq(x, 9);
                  }},
                 {"is_null",
                  [](drill::Check& c) {
                      int x = 1;
                      c.is_true(is_null(nullptr));
                      c.is_false(is_null(&x));
                  }},
                 {"value_or",
                  [](drill::Check& c) {
                      int x = 4;
                      c.eq(value_or(&x, 0), 4);
                      c.eq(value_or(nullptr, 99), 99);
                  }},
                 {"swap_via_pointers",
                  [](drill::Check& c) {
                      int a = 1, b = 2;
                      swap_via_pointers(&a, &b);
                      c.eq(a, 2);
                      c.eq(b, 1);
                  }},
                 {"pointers_are_same_size",
                  [](drill::Check& c) { c.is_true(pointers_are_same_size()); }},
                 {"refers_to_same",
                  [](drill::Check& c) {
                      int x = 1, y = 1;
                      c.is_true(refers_to_same(x, &x));
                      c.is_false(refers_to_same(x, &y));
                  }},
             }},
            {"B. POINTERS AND ARRAYS",
             {
                 {"first_element",
                  [](drill::Check& c) {
                      const int arr[] = {4, 5, 6};
                      c.eq(first_element(arr), 4);
                  }},
                 {"element_at",
                  [](drill::Check& c) {
                      const int arr[] = {4, 5, 6};
                      c.eq(element_at(arr, 2), 6);
                  }},
                 {"sum_array",
                  [](drill::Check& c) {
                      const int arr[] = {1, 2, 3};
                      c.eq(sum_array(arr, 3), 6);
                      c.eq(sum_array(arr, 0), 0);
                  }},
                 {"length_of_local_array",
                  [](drill::Check& c) { c.eq(length_of_local_array(), std::size_t{5}); }},
                 {"advance",
                  [](drill::Check& c) {
                      const int arr[] = {4, 5, 6};
                      c.is_true(advance(arr, 2) == arr + 2);
                      c.eq(*advance(arr, 1), 5);
                  }},
                 {"elements_between",
                  [](drill::Check& c) {
                      const int arr[] = {1, 2, 3, 4};
                      c.eq(elements_between(arr, arr + 3), std::ptrdiff_t{3});
                  }},
                 {"find_first",
                  [](drill::Check& c) {
                      const int arr[] = {1, 2, 3};
                      c.is_true(find_first(arr, 3, 2) == arr + 1);
                      c.is_true(find_first(arr, 3, 9) == nullptr);
                  }},
                 {"reverse_array",
                  [](drill::Check& c) {
                      int arr[] = {1, 2, 3};
                      reverse_array(arr, 3);
                      c.eq(arr[0], 3);
                      c.eq(arr[2], 1);
                  }},
             }},
            {"C. C STRINGS",
             {
                 {"c_length",
                  [](drill::Check& c) {
                      c.eq(c_length("abc"), std::size_t{3});
                      c.eq(c_length(""), std::size_t{0});
                  }},
                 {"c_copy",
                  [](drill::Check& c) {
                      char buffer[8] = {};
                      c_copy(buffer, "abc");
                      c.eq(std::string(buffer), std::string("abc"));
                  }},
                 {"c_equal",
                  [](drill::Check& c) {
                      c.is_true(c_equal("abc", "abc"));
                      c.is_false(c_equal("abc", "abd"));
                      c.is_false(c_equal("ab", "abc"));
                  }},
                 {"c_find",
                  [](drill::Check& c) {
                      const char* s = "abc";
                      c.is_true(c_find(s, 'b') == s + 1);
                      c.is_true(c_find(s, 'z') == nullptr);
                  }},
                 {"c_count",
                  [](drill::Check& c) {
                      c.eq(c_count("banana", 'a'), 3);
                      c.eq(c_count("abc", 'z'), 0);
                  }},
                 {"c_upper",
                  [](drill::Check& c) {
                      char buffer[8] = "a1b";
                      c_upper(buffer);
                      c.eq(std::string(buffer), std::string("A1B"));
                  }},
             }},
            {"D. CONST, INDIRECTION, AND OUT-PARAMETERS",
             {
                 {"bump_through_const_pointer",
                  [](drill::Check& c) {
                      int x = 4;
                      bump_through_const_pointer(&x);
                      c.eq(x, 5);
                  }},
                 {"repoint",
                  [](drill::Check& c) {
                      int a = 1, b = 2;
                      int* p = &a;
                      repoint(&p, &b);
                      c.is_true(p == &b);
                  }},
                 {"sum_pointed_to",
                  [](drill::Check& c) {
                      int a = 1, b = 2;
                      c.eq(sum_pointed_to({&a, nullptr, &b}), 3);
                      c.eq(sum_pointed_to({}), 0);
                  }},
                 {"try_divide",
                  [](drill::Check& c) {
                      int out = -1;
                      c.is_true(try_divide(7, 2, &out));
                      c.eq(out, 3);
                      out = -1;
                      c.is_false(try_divide(7, 0, &out));
                      c.eq(out, -1);
                  }},
                 {"apply_op",
                  [](drill::Check& c) {
                      c.eq(apply_op('+', 2, 3), 5);
                      c.eq(apply_op('*', 2, 3), 6);
                      c.eq(apply_op('?', 2, 3), 0);
                      c.eq(add_op(1, 1), 2);
                  }},
                 {"max_element_ptr",
                  [](drill::Check& c) {
                      const int arr[] = {1, 9, 3};
                      c.is_true(max_element_ptr(arr, 3) == arr + 1);
                      c.is_true(max_element_ptr(arr, 0) == nullptr);
                  }},
             }},
        },
        argc, argv);
}
