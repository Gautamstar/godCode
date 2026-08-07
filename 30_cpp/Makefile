# godCode C++ drills.
#
#   make               build and run every drill set
#   make 00_basics     build and run one set
#   make 00_basics ARGS=12        run only drill 12
#   make 00_basics ARGS=10-20     a range
#   make 00_basics ARGS=pointer   name substring
#   make 00_basics ARGS=-v        list passing drills too
#   make clean
#
# Sanitisers are ON by default. In this module that is the point: most C++
# mistakes are silent at runtime, and -fsanitize=address,undefined turns a
# dangling pointer or a signed overflow into a loud error instead of a wrong
# answer that happens to work today.
#
#   make SAN=0 00_basics     turn them off if a drill is slow

CXX      ?= g++
STD      ?= c++20
# -Wno-unused-parameter because an unfinished stub never touches its arguments,
# and 30 warnings on a fresh file is noise, not signal.
WARN      = -Wall -Wextra -Wpedantic -Wshadow -Wno-unused-parameter
SAN      ?= 1
ifeq ($(SAN),1)
SANFLAGS  = -fsanitize=address,undefined -fno-omit-frame-pointer
else
SANFLAGS  =
endif
CXXFLAGS  = -std=$(STD) $(WARN) $(SANFLAGS) -g -O0 -Iharness

SRC  := $(wildcard drills/*.cpp)
SETS := $(notdir $(basename $(SRC)))
BIN  := build

.PHONY: all clean list $(SETS)

all: $(SETS)

# Build and run one drill set. The `-` lets `make all` keep going when one
# set still has unfinished drills.
$(SETS): %: $(BIN)/%
	@echo "=== $* ==="
	@-./$(BIN)/$* $(ARGS)

$(BIN)/%: drills/%.cpp harness/drill_harness.hpp | $(BIN)
	@$(CXX) $(CXXFLAGS) $< -o $@

$(BIN):
	@mkdir -p $(BIN)

list:
	@echo $(SETS) | tr ' ' '\n'

clean:
	@rm -rf $(BIN)
