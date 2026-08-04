// tests: do not edit
import { describe, expect, it } from "vitest";
import { identity, firstOrNull, pluck, groupBy } from "./05_generics";

describe("05 generics", () => {
  it("identity", () => {
    expect(identity("hi")).toBe("hi");
    expect(identity(7)).toBe(7);
    const obj = { a: 1 };
    expect(identity(obj)).toBe(obj);
  });

  it("firstOrNull", () => {
    expect(firstOrNull([1, 2])).toBe(1);
    expect(firstOrNull<number>([])).toBeNull();
    expect(firstOrNull(["a"])).toBe("a");
  });

  it("pluck", () => {
    expect(pluck([{ id: 1 }, { id: 2 }], "id")).toEqual([1, 2]);
    expect(pluck([{ name: "Ada" }, { name: "Bob" }], "name")).toEqual([
      "Ada",
      "Bob",
    ]);
    expect(pluck([], "id" as never)).toEqual([]);
  });

  it("groupBy", () => {
    expect(groupBy(["ant", "bee", "ape"], (w) => w[0])).toEqual({
      a: ["ant", "ape"],
      b: ["bee"],
    });
    expect(groupBy([], () => "x")).toEqual({});
  });
});
