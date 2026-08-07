// Shared runner for every C++ drills file. You do not need to edit this.
//
// A drills file looks like:
//
//     #include "../harness/drill_harness.hpp"
//
//     int twice(int n) { TODO; }
//
//     int main(int argc, char** argv) {
//         return drill::run({
//             {"A. SECTION TITLE", {
//                 {"twice", [](drill::Check& c) {
//                     c.eq(twice(2), 4);
//                     c.eq(twice(0), 0);
//                 }},
//             }},
//         }, argc, argv);
//     }
//
// TODO throws, and the runner reports that drill as "not started" rather than
// failing it, so an untouched file reads 0/30 not-started instead of 30 wrong.
#pragma once

#include <cstddef>
#include <cstdint>
#include <exception>
#include <functional>
#include <iostream>
#include <map>
#include <set>
#include <sstream>
#include <string>
#include <type_traits>
#include <vector>

namespace drill {

// Thrown by an unfinished drill. TODO is the macro you write in a stub.
struct NotImplemented {};
#define TODO throw ::drill::NotImplemented {}

// ---------------------------------------------------------------------------
// printing values in failure messages
// ---------------------------------------------------------------------------

inline std::string show(bool v) { return v ? "true" : "false"; }
inline std::string show(char v) { return std::string("'") + v + "'"; }
inline std::string show(const std::string& v) { return "\"" + v + "\""; }
inline std::string show(const char* v) { return std::string("\"") + v + "\""; }

template <class T>
std::enable_if_t<std::is_arithmetic_v<T>, std::string> show(T v) {
    std::ostringstream out;
    out << v;
    return out.str();
}

template <class T>
std::string show(const std::vector<T>& v) {
    std::ostringstream out;
    out << "[";
    for (std::size_t i = 0; i < v.size(); ++i) {
        if (i) out << ", ";
        out << show(v[i]);
    }
    out << "]";
    return out.str();
}

template <class K, class V>
std::string show(const std::map<K, V>& m) {
    std::ostringstream out;
    out << "{";
    bool first = true;
    for (const auto& [k, v] : m) {
        if (!first) out << ", ";
        first = false;
        out << show(k) << ": " << show(v);
    }
    out << "}";
    return out.str();
}

template <class T>
std::string show(const std::set<T>& s) {
    std::ostringstream out;
    out << "{";
    bool first = true;
    for (const auto& x : s) {
        if (!first) out << ", ";
        first = false;
        out << show(x);
    }
    out << "}";
    return out.str();
}

// ---------------------------------------------------------------------------
// the checker handed to each drill
// ---------------------------------------------------------------------------

class Check {
public:
    bool ok = true;
    std::string detail;

    // The workhorse. Records only the FIRST failure so one broken drill does
    // not print twenty lines.
    template <class A, class B>
    void eq(const A& actual, const B& expected) {
        if (actual == expected) return;
        fail("got " + show(actual) + ", expected " + show(expected));
    }

    void is_true(bool value, const std::string& what = "") {
        if (value) return;
        fail(what.empty() ? "expected true, got false" : what);
    }

    void is_false(bool value, const std::string& what = "") {
        if (!value) return;
        fail(what.empty() ? "expected false, got true" : what);
    }

    // For anything the other helpers do not cover.
    void note_fail(const std::string& message) { fail(message); }

private:
    void fail(const std::string& message) {
        ok = false;
        if (detail.empty()) detail = message;
    }
};

using Body = std::function<void(Check&)>;

struct Drill {
    const char* name;
    Body body;
};

struct Section {
    const char* title;
    std::vector<Drill> drills;
};

// ---------------------------------------------------------------------------
// command-line filter: a number, a range like 12-20, or a name substring
// ---------------------------------------------------------------------------

inline bool all_digits(const std::string& s) {
    if (s.empty()) return false;
    for (char c : s)
        if (c < '0' || c > '9') return false;
    return true;
}

inline bool lower_contains(std::string hay, std::string needle) {
    for (char& c : hay) c = static_cast<char>(std::tolower(c));
    for (char& c : needle) c = static_cast<char>(std::tolower(c));
    return hay.find(needle) != std::string::npos;
}

inline bool selected(const std::string& filter, int number, const std::string& name) {
    if (filter.empty()) return true;
    if (all_digits(filter)) return number == std::stoi(filter);

    auto dash = filter.find('-');
    if (dash != std::string::npos) {
        std::string lo = filter.substr(0, dash);
        std::string hi = filter.substr(dash + 1);
        if (all_digits(lo) && all_digits(hi))
            return number >= std::stoi(lo) && number <= std::stoi(hi);
    }
    return lower_contains(name, filter);
}

// ---------------------------------------------------------------------------
// the runner
// ---------------------------------------------------------------------------

inline int run(const std::vector<Section>& sections, int argc, char** argv) {
    std::string filter;
    bool verbose = false;
    for (int i = 1; i < argc; ++i) {
        std::string arg = argv[i];
        if (arg == "-v")
            verbose = true;
        else if (filter.empty())
            filter = arg;
    }

    int passed = 0, failed = 0, todo = 0, number = 0;
    int first_todo_number = 0;
    std::string first_todo_name;
    bool shown_any = false;

    for (const auto& section : sections) {
        bool header_shown = false;
        for (const auto& d : section.drills) {
            ++number;
            if (!selected(filter, number, d.name)) continue;

            Check check;
            std::string status;
            try {
                d.body(check);
                status = check.ok ? "PASS" : "FAIL";
            } catch (const NotImplemented&) {
                status = "TODO";
            } catch (const std::exception& e) {
                status = "FAIL";
                check.detail = std::string("threw std::exception: ") + e.what();
            } catch (...) {
                status = "FAIL";
                check.detail = "threw an unknown exception";
            }

            if (status == "PASS") ++passed;
            if (status == "FAIL") ++failed;
            if (status == "TODO") {
                ++todo;
                if (first_todo_number == 0) {
                    first_todo_number = number;
                    first_todo_name = d.name;
                }
            }

            if (status == "PASS" && !verbose) continue;

            if (!header_shown) {
                std::cout << "\n" << section.title << "\n";
                std::cout << std::string(std::string(section.title).size(), '-') << "\n";
                header_shown = true;
            }
            shown_any = true;
            std::cout << "  " << (number < 10 ? " " : "") << number << "  " << status
                      << "  " << d.name << "\n";
            if (status == "FAIL") std::cout << "          " << check.detail << "\n";
        }
    }

    int total = passed + failed + todo;
    if (!shown_any && total > 0)
        std::cout << "\nAll " << total << " selected drills pass.\n";

    std::cout << "\n" << std::string(46, '=') << "\n";
    std::cout << "  " << passed << "/" << total << " complete    " << failed
              << " failing    " << todo << " not started\n";
    if (first_todo_number)
        std::cout << "  next up: drill " << first_todo_number << ", " << first_todo_name
                  << "\n";
    std::cout << std::string(46, '=') << "\n";

    return failed == 0 ? 0 : 1;
}

}  // namespace drill
