// Reference answers for module 02. Implementations only; the test block lives
// in drills/02_memory.cpp.

#include <cstddef>
#include <functional>
#include <memory>
#include <string>
#include <vector>

#include "../harness/drill_harness.hpp"

inline std::vector<std::string>& trace() {
    static std::vector<std::string> log;
    return log;
}

// A. RAW HEAP

int* make_int(int value) { return new int(value); }

void destroy_int(int* p) {
    delete p;  // delete on nullptr is defined and does nothing
}

int* make_array(std::size_t n) {
    return new int[n]();  // the () zeroes; without it you get garbage
}

void destroy_array(int* p) {
    delete[] p;  // [] because it was new[]. Mixing them is undefined.
}

int* clone_array(const int* src, std::size_t n) {
    int* copy = new int[n];
    for (std::size_t i = 0; i < n; ++i) copy[i] = src[i];
    return copy;
}

int sum_and_destroy(int* owned, std::size_t n) {
    int total = 0;
    for (std::size_t i = 0; i < n; ++i) total += owned[i];
    delete[] owned;
    return total;
}

int* grow(int* old_block, std::size_t old_n, std::size_t new_n) {
    int* bigger = new int[new_n]();
    for (std::size_t i = 0; i < old_n; ++i) bigger[i] = old_block[i];
    delete[] old_block;  // free the old one only after copying out of it
    return bigger;
}

// B. RAII BY HAND

class IntBuffer {
public:
    explicit IntBuffer(std::size_t n) : data_(new int[n]()), size_(n) {}
    ~IntBuffer() { delete[] data_; }

    std::size_t size() const { return size_; }
    int& at(std::size_t i) { return data_[i]; }

private:
    int* data_ = nullptr;
    std::size_t size_ = 0;
};

void fill_buffer(IntBuffer& buffer, int value) {
    for (std::size_t i = 0; i < buffer.size(); ++i) buffer.at(i) = value;
}

class Tracker {
public:
    explicit Tracker(std::string name) : name_(std::move(name)) {}
    ~Tracker() { trace().push_back(name_); }

private:
    std::string name_;
};

std::vector<std::string> destruction_order() {
    trace().clear();
    {
        Tracker a("a");
        Tracker b("b");
        Tracker c("c");
    }  // destroyed here, in reverse: c, b, a
    return trace();
}

void boom();

std::vector<std::string> cleanup_on_throw() {
    trace().clear();
    try {
        Tracker guard("cleanup");
        boom();
        // a manual `delete` written here would never run
    } catch (const std::exception&) {
        // the Tracker destructor already ran during stack unwinding
    }
    return trace();
}

class ScopeGuard {
public:
    explicit ScopeGuard(std::function<void()> action) : action_(std::move(action)) {}
    ~ScopeGuard() {
        if (action_) action_();
    }

private:
    std::function<void()> action_;
};

std::vector<std::string> guarded() {
    trace().clear();
    {
        ScopeGuard guard([] { trace().push_back("done"); });
    }
    return trace();
}

int sum_with_early_return(std::size_t n, int fill) {
    if (n == 0) return 0;
    IntBuffer buffer(n);
    fill_buffer(buffer, fill);
    int total = 0;
    for (std::size_t i = 0; i < n; ++i) total += buffer.at(i);
    return total;  // the buffer frees itself on every exit path
}

// C. unique_ptr

std::unique_ptr<int> make_owned(int value) { return std::make_unique<int>(value); }

int read_owned(const std::unique_ptr<int>& owned) { return *owned; }

int consume(std::unique_ptr<int> owned) {
    // by value, so the caller had to std::move and no longer owns it
    return *owned;
}

bool move_leaves_source_empty(std::unique_ptr<int>& from) {
    std::unique_ptr<int> taken = std::move(from);
    return from == nullptr;
}

std::unique_ptr<int[]> make_owned_array(std::size_t n) {
    return std::make_unique<int[]>(n);  // zero-initialised, deletes with []
}

int* release_from(std::unique_ptr<int>& owned) {
    return owned.release();  // hands the pointer over WITHOUT deleting
}

class OwnedBuffer {
public:
    explicit OwnedBuffer(std::size_t n) : data_(std::make_unique<int[]>(n)), size_(n) {}
    // no destructor: the unique_ptr member writes it for us
    std::size_t size() const { return size_; }
    int& at(std::size_t i) { return data_[i]; }

private:
    std::unique_ptr<int[]> data_;
    std::size_t size_ = 0;
};

// D. shared_ptr AND weak_ptr

std::shared_ptr<int> make_shared_int(int value) { return std::make_shared<int>(value); }

long owner_count(const std::shared_ptr<int>& p) { return p.use_count(); }

long count_after_copy(const std::shared_ptr<int>& p) {
    std::shared_ptr<int> copy = p;  // legal, and bumps the count
    return copy.use_count();
}  // copy dies here and the count drops back

int value_through_weak(const std::shared_ptr<int>& p) {
    std::weak_ptr<int> watcher = p;
    std::shared_ptr<int> locked = watcher.lock();
    return *locked;
}

bool weak_expires_after_owner_dies() {
    std::weak_ptr<int> watcher;
    {
        auto owner = std::make_shared<int>(1);
        watcher = owner;
    }  // last owner dies here
    return watcher.expired();
}

struct Node {
    std::shared_ptr<Node> strong_peer;
    std::weak_ptr<Node> weak_peer;
    ~Node() { trace().push_back("node"); }
};

int nodes_destroyed_with_weak_link() {
    trace().clear();
    {
        auto a = std::make_shared<Node>();
        auto b = std::make_shared<Node>();
        a->strong_peer = b;  // a owns b
        b->weak_peer = a;    // b only WATCHES a, so no cycle
    }
    return static_cast<int>(trace().size());
}

std::vector<std::string> custom_deleter_runs() {
    trace().clear();
    {
        auto closer = [](int* p) {
            trace().push_back("closed");
            delete p;
        };
        // the deleter is part of the type, which is why this is spelled out
        std::unique_ptr<int, void (*)(int*)> handle(new int(1), closer);
    }
    return trace();
}
