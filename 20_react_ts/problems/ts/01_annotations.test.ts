// tests: do not edit
import { describe as group, expect, it } from "vitest";
import { add, greet, describe, total } from "./01_annotations";

group("01 annotations", () => {
  it("add", () => {
    expect(add(2, 3)).toBe(5);
    expect(add(-1, 1)).toBe(0);
  });

  it("greet uses a default greeting", () => {
    expect(greet("Gautam")).toBe("Hello, Gautam!");
    expect(greet("Gautam", "Hey")).toBe("Hey, Gautam!");
  });

  it("describe narrows the union", () => {
    expect(describe(42)).toBe("number: 42");
    expect(describe("hi")).toBe("string: hi");
    expect(describe(0)).toBe("number: 0");
  });

  it("total takes any number of args", () => {
    expect(total(1, 2, 3)).toBe(6);
    expect(total()).toBe(0);
    expect(total(5)).toBe(5);
  });
});
