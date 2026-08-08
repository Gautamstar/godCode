// MODULE 02 DRILLS - the heap, RAII, and smart pointers. 28 reps.
//
// This is the module that low-level interviews actually probe. The whole
// subject collapses to one question: WHO OWNS THIS, AND WHEN DOES IT DIE?
//
//   Stack   objects die at the closing brace, automatically, in reverse order
//           of construction. Nothing to remember.
//   Heap    objects live until someone says delete. Forget, and you leak.
//           Say it twice, and you corrupt the allocator. Say it too early,
//           and every remaining pointer dangles.
//
// RAII is the answer C++ gives: wrap the heap thing in a stack object whose
// destructor frees it. Then the automatic stack rule does your bookkeeping,
// including on the exception path where a manual delete would be skipped.
// unique_ptr and shared_ptr are that idea, already written for you.
//
// Sections A and B are what you must be able to write. Sections C and D are
// what you should actually use.
//
// RUN
//     make 02_memory
//     make 02_memory ARGS=15
//     make 02_memory ARGS=unique
//     make leaks SET=02_memory      run again with leak detection on
//
// Leak detection is off in the normal loop, because an unfinished drill throws
// before it can free anything. Turn it on once a section is green.

#include <cstddef>
#include <functional>
#include <memory>
#include <string>
#include <vector>

#include "../harness/drill_harness.hpp"

// A shared log the drills write to, so the tests can observe when destructors
// run. Given to you, not a drill.
inline std::vector<std::string>& trace() {
    static std::vector<std::string> log;
    return log;
}

// ===========================================================================
// A. RAW HEAP: new AND delete
// ===========================================================================
//
// You will rarely write these in modern code. You need them anyway, because
// they are what unique_ptr is doing, and because you will read old code.

// 1. Allocate one int on the heap holding `value` and return it.
//    The CALLER is now responsible for deleting it. Saying that out loud in a
//    comment is the only ownership documentation raw pointers have.
int* make_int(int value) { TODO; }

// 2. Free an int allocated with new.
//    delete on a null pointer is defined and does nothing, so no guard needed.
void destroy_int(int* p) { TODO; }

// 3. Allocate an array of n ints, every element zero.
//    `new int[n]()` value-initialises. `new int[n]` leaves garbage.
int* make_array(std::size_t n) { TODO; }

// 4. Free an array allocated with new[].
//    delete[], not delete. Using the wrong one is undefined behaviour: the
//    array form has to walk the elements to destroy them, and it looks up a
//    count the scalar form never stored.
void destroy_array(int* p) { TODO; }

// 5. Allocate a copy of n elements from src and return it.
int* clone_array(const int* src, std::size_t n) { TODO; }

// 6. Take ownership of an array, sum it, free it, return the sum.
//    A function that frees what it was handed is "sinking" the pointer. With
//    raw pointers nothing in the signature says so, which is the problem
//    unique_ptr exists to fix.
int sum_and_destroy(int* owned, std::size_t n) { TODO; }

// 7. Grow an array: allocate new_n elements, copy the old ones across, free
//    the old block, return the new one. Assume new_n >= old_n and zero the
//    tail. This is std::vector's growth, done by hand.
int* grow(int* old_block, std::size_t old_n, std::size_t new_n) { TODO; }

// ===========================================================================
// B. RAII BY HAND
// ===========================================================================

// 8. A buffer that owns its memory.
//    The constructor allocates, the destructor frees. Once that holds, no
//    caller can leak it, and no early return or thrown exception can skip the
//    cleanup, because destructors of stack objects always run.
//
//    Fill in the constructor, destructor, size(), and at().
class IntBuffer {
public:
    explicit IntBuffer(std::size_t n) { TODO; }
    ~IntBuffer() { TODO; }

    std::size_t size() const { TODO; }
    int& at(std::size_t i) { TODO; }

private:
    int* data_ = nullptr;
    std::size_t size_ = 0;
};

// 9. Fill every slot of a buffer with `value`.
void fill_buffer(IntBuffer& buffer, int value) { TODO; }

// 10. Construct three Tracker objects named "a", "b", "c" in that order inside
//     a scope, then let the scope end. Return the trace.
//     Destructors run in REVERSE order of construction, so you should get
//     "c", "b", "a". Tracker is written for you below.
class Tracker {
public:
    explicit Tracker(std::string name) : name_(std::move(name)) {}
    ~Tracker() { trace().push_back(name_); }

private:
    std::string name_;
};

std::vector<std::string> destruction_order() { TODO; }

// 11. Call `boom` inside a try/catch, with a Tracker named "cleanup" alive on
//     the stack when it throws. Swallow the exception and return the trace.
//     The point: the destructor still ran. A manual `delete` written after the
//     throwing call would have been skipped. This is the argument for RAII in
//     one drill.
void boom();  // defined in the test block, throws std::runtime_error
std::vector<std::string> cleanup_on_throw() { TODO; }

// 12. A guard that runs a callback when it goes out of scope.
//     Store the callback, invoke it in the destructor. This is the shape of
//     every ScopeGuard / defer helper you will meet.
class ScopeGuard {
public:
    explicit ScopeGuard(std::function<void()> action) { TODO; }
    ~ScopeGuard() { TODO; }

private:
    std::function<void()> action_;
};

// 13. Use a ScopeGuard to push "done" onto the trace when the scope ends, and
//     return the trace after the scope has closed.
std::vector<std::string> guarded() { TODO; }

// 14. Return the sum of a heap array WITHOUT leaking, even though the middle
//     of the function returns early when n is 0. Use IntBuffer, not new.
//     Written with raw new and a delete at the bottom, the early return leaks.
int sum_with_early_return(std::size_t n, int fill) { TODO; }

// ===========================================================================
// C. unique_ptr: SOLE OWNERSHIP
// ===========================================================================
//
// unique_ptr is a pointer that deletes what it holds when it dies, and that
// CANNOT be copied. Copying would mean two owners and a double free, so the
// language stops you at compile time. You can only MOVE it, which transfers
// ownership and leaves the source empty.

// 15. Return a unique_ptr owning a new int holding `value`.
//     Prefer std::make_unique<int>(value) over unique_ptr<int>(new int(value)).
std::unique_ptr<int> make_owned(int value) { TODO; }

// 16. Read the value out of a unique_ptr. Dereference it like a raw pointer.
int read_owned(const std::unique_ptr<int>& owned) { TODO; }

// 17. Take ownership by value, return the int inside.
//     Taking unique_ptr BY VALUE in the signature is how you say "I am taking
//     ownership" in a way the compiler enforces. The caller must std::move
//     into it, so the transfer is visible at the call site.
int consume(std::unique_ptr<int> owned) { TODO; }

// 18. Move `from` into a new unique_ptr, and return whether `from` is empty
//     afterwards. It should be: a move leaves the source holding nullptr.
bool move_leaves_source_empty(std::unique_ptr<int>& from) { TODO; }

// 19. Return a unique_ptr owning an array of n zeroed ints.
//     std::make_unique<int[]>(n). The array specialisation calls delete[] for
//     you, which is one fewer thing to get wrong.
std::unique_ptr<int[]> make_owned_array(std::size_t n) { TODO; }

// 20. Release ownership out of a unique_ptr and return the raw pointer.
//     .release() hands the pointer over and empties the unique_ptr WITHOUT
//     deleting. The caller inherits the obligation. Compare .reset(), which
//     deletes what is held.
int* release_from(std::unique_ptr<int>& owned) { TODO; }

// 21. A type that owns a buffer through a unique_ptr member.
//     Notice there is no destructor to write: the member's destructor does it.
//     That is the "rule of zero", and it is the goal for most classes.
class OwnedBuffer {
public:
    explicit OwnedBuffer(std::size_t n) { TODO; }
    std::size_t size() const { TODO; }
    int& at(std::size_t i) { TODO; }

private:
    std::unique_ptr<int[]> data_;
    std::size_t size_ = 0;
};

// ===========================================================================
// D. shared_ptr AND weak_ptr: SHARED OWNERSHIP
// ===========================================================================
//
// shared_ptr keeps a reference count. The object dies when the last owner
// does. That costs an atomic increment per copy, and it buys you the ability
// to not know who finishes last. Reach for unique_ptr first; use shared_ptr
// when ownership genuinely is shared.

// 22. Return a shared_ptr owning a new int.
std::shared_ptr<int> make_shared_int(int value) { TODO; }

// 23. Return how many shared_ptrs own the same object as `p`.
//     .use_count(). Useful in drills and tests, misleading in real concurrent
//     code, where the count can change the instant after you read it.
long owner_count(const std::shared_ptr<int>& p) { TODO; }

// 24. Copy the shared_ptr into a local and return the use count while both
//     are alive. Copying a shared_ptr is legal and bumps the count, which is
//     exactly what unique_ptr forbids.
long count_after_copy(const std::shared_ptr<int>& p) { TODO; }

// 25. Make a weak_ptr from the shared_ptr, then lock it and return the value.
//     A weak_ptr observes without owning. .lock() gives you a shared_ptr if
//     the object is still alive, and an empty one if it is not.
int value_through_weak(const std::shared_ptr<int>& p) { TODO; }

// 26. Create a shared_ptr, take a weak_ptr to it, destroy the shared_ptr, and
//     return whether the weak_ptr has expired. It should have.
//     This is why weak_ptr exists: a raw pointer could not tell you.
bool weak_expires_after_owner_dies() { TODO; }

// 27. Two Nodes pointing at each other with shared_ptr never die: each holds
//     the other's count at 1 forever. That is a reference CYCLE, and it is the
//     one leak a reference-counted pointer cannot solve.
//
//     Build two Nodes, link a->peer to b with shared, and b->peer to a with
//     WEAK, let them go out of scope, and return how many destructors ran.
//     With the weak link the answer is 2. Make both shared and it is 0.
struct Node {
    std::shared_ptr<Node> strong_peer;
    std::weak_ptr<Node> weak_peer;
    ~Node() { trace().push_back("node"); }
};

int nodes_destroyed_with_weak_link() { TODO; }

// 28. A unique_ptr with a CUSTOM DELETER that pushes "closed" onto the trace
//     instead of calling delete on a raw resource. Return the trace after the
//     pointer has gone out of scope.
//     This is how you wrap a C API handle (FILE*, socket, mutex) in RAII.
//     Use a lambda deleter and note the type changes:
//       std::unique_ptr<int, void(*)(int*)>
std::vector<std::string> custom_deleter_runs() { TODO; }

// --------------------------- tests: do not edit ---------------------------

#include <stdexcept>

void boom() { throw std::runtime_error("boom"); }

int main(int argc, char** argv) {
    return drill::run(
        {
            {"A. RAW HEAP",
             {
                 {"make_int",
                  [](drill::Check& c) {
                      int* p = make_int(7);
                      c.eq(*p, 7);
                      delete p;
                  }},
                 {"destroy_int",
                  [](drill::Check& c) {
                      destroy_int(new int(1));
                      destroy_int(nullptr);
                      c.is_true(true);
                  }},
                 {"make_array",
                  [](drill::Check& c) {
                      int* p = make_array(3);
                      c.eq(p[0], 0);
                      c.eq(p[2], 0);
                      delete[] p;
                  }},
                 {"destroy_array",
                  [](drill::Check& c) {
                      destroy_array(new int[4]());
                      c.is_true(true);
                  }},
                 {"clone_array",
                  [](drill::Check& c) {
                      const int src[] = {1, 2, 3};
                      int* copy = clone_array(src, 3);
                      c.is_true(copy != src);
                      c.eq(copy[1], 2);
                      delete[] copy;
                  }},
                 {"sum_and_destroy",
                  [](drill::Check& c) {
                      int* owned = new int[3]{1, 2, 3};
                      c.eq(sum_and_destroy(owned, 3), 6);
                  }},
                 {"grow",
                  [](drill::Check& c) {
                      int* block = new int[2]{1, 2};
                      int* bigger = grow(block, 2, 4);
                      c.eq(bigger[0], 1);
                      c.eq(bigger[1], 2);
                      c.eq(bigger[3], 0);
                      delete[] bigger;
                  }},
             }},
            {"B. RAII BY HAND",
             {
                 {"IntBuffer",
                  [](drill::Check& c) {
                      IntBuffer buffer(3);
                      c.eq(buffer.size(), std::size_t{3});
                      buffer.at(1) = 9;
                      c.eq(buffer.at(1), 9);
                  }},
                 {"fill_buffer",
                  [](drill::Check& c) {
                      IntBuffer buffer(3);
                      fill_buffer(buffer, 7);
                      c.eq(buffer.at(0), 7);
                      c.eq(buffer.at(2), 7);
                  }},
                 {"destruction_order",
                  [](drill::Check& c) {
                      c.eq(destruction_order(),
                           std::vector<std::string>{"c", "b", "a"});
                  }},
                 {"cleanup_on_throw",
                  [](drill::Check& c) {
                      c.eq(cleanup_on_throw(), std::vector<std::string>{"cleanup"});
                  }},
                 {"ScopeGuard",
                  [](drill::Check& c) {
                      trace().clear();
                      {
                          ScopeGuard guard([] { trace().push_back("ran"); });
                          c.eq(trace().size(), std::size_t{0});
                      }
                      c.eq(trace(), std::vector<std::string>{"ran"});
                      trace().clear();
                  }},
                 {"guarded",
                  [](drill::Check& c) {
                      c.eq(guarded(), std::vector<std::string>{"done"});
                  }},
                 {"sum_with_early_return",
                  [](drill::Check& c) {
                      c.eq(sum_with_early_return(3, 2), 6);
                      c.eq(sum_with_early_return(0, 2), 0);
                  }},
             }},
            {"C. unique_ptr",
             {
                 {"make_owned",
                  [](drill::Check& c) {
                      auto owned = make_owned(5);
                      c.eq(*owned, 5);
                  }},
                 {"read_owned",
                  [](drill::Check& c) {
                      auto owned = std::make_unique<int>(8);
                      c.eq(read_owned(owned), 8);
                  }},
                 {"consume",
                  [](drill::Check& c) {
                      auto owned = std::make_unique<int>(4);
                      c.eq(consume(std::move(owned)), 4);
                      c.is_true(owned == nullptr, "moving from it should empty it");
                  }},
                 {"move_leaves_source_empty",
                  [](drill::Check& c) {
                      auto owned = std::make_unique<int>(1);
                      c.is_true(move_leaves_source_empty(owned));
                  }},
                 {"make_owned_array",
                  [](drill::Check& c) {
                      auto owned = make_owned_array(3);
                      c.eq(owned[0], 0);
                      owned[2] = 5;
                      c.eq(owned[2], 5);
                  }},
                 {"release_from",
                  [](drill::Check& c) {
                      auto owned = std::make_unique<int>(6);
                      int* raw = release_from(owned);
                      c.is_true(owned == nullptr, "release must empty the unique_ptr");
                      c.eq(*raw, 6);
                      delete raw;
                  }},
                 {"OwnedBuffer",
                  [](drill::Check& c) {
                      OwnedBuffer buffer(4);
                      c.eq(buffer.size(), std::size_t{4});
                      buffer.at(3) = 1;
                      c.eq(buffer.at(3), 1);
                  }},
             }},
            {"D. shared_ptr AND weak_ptr",
             {
                 {"make_shared_int",
                  [](drill::Check& c) {
                      auto p = make_shared_int(3);
                      c.eq(*p, 3);
                  }},
                 {"owner_count",
                  [](drill::Check& c) {
                      auto p = std::make_shared<int>(1);
                      c.eq(owner_count(p), 1L);
                      auto q = p;
                      c.eq(owner_count(p), 2L);
                  }},
                 {"count_after_copy",
                  [](drill::Check& c) {
                      auto p = std::make_shared<int>(1);
                      c.eq(count_after_copy(p), 2L);
                      c.eq(p.use_count(), 1L);
                  }},
                 {"value_through_weak",
                  [](drill::Check& c) {
                      auto p = std::make_shared<int>(9);
                      c.eq(value_through_weak(p), 9);
                  }},
                 {"weak_expires_after_owner_dies",
                  [](drill::Check& c) { c.is_true(weak_expires_after_owner_dies()); }},
                 {"nodes_destroyed_with_weak_link",
                  [](drill::Check& c) { c.eq(nodes_destroyed_with_weak_link(), 2); }},
                 {"custom_deleter_runs",
                  [](drill::Check& c) {
                      c.eq(custom_deleter_runs(), std::vector<std::string>{"closed"});
                  }},
             }},
        },
        argc, argv);
}
