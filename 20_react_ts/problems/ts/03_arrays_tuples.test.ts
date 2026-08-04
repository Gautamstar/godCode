// tests: do not edit
import { describe, expect, it } from "vitest";
import { firstAndLast, swap, fullName, topThree } from "./03_arrays_tuples";

describe("03 arrays & tuples", () => {
  it("firstAndLast", () => {
    expect(firstAndLast([1, 2, 3])).toEqual([1, 3]);
    expect(firstAndLast([5])).toEqual([5, 5]);
  });

  it("swap", () => {
    expect(swap(["age", 30])).toEqual([30, "age"]);
  });

  it("fullName", () => {
    expect(fullName({ first: "Ada", last: "Lovelace" })).toBe("Ada Lovelace");
  });

  it("topThree", () => {
    expect(topThree([4, 9, 1, 7, 3])).toEqual([9, 7, 4]);
    expect(topThree([2, 1])).toEqual([2, 1]);
    expect(topThree([])).toEqual([]);
  });

  it("topThree does not mutate its input", () => {
    const original = [4, 9, 1, 7, 3];
    topThree(original);
    expect(original).toEqual([4, 9, 1, 7, 3]);
  });
});
