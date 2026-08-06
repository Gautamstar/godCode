// tests: do not edit
//
// These grade BEHAVIOUR only. Types are erased before this runs, so a function
// with no annotations at all can pass here. Run `npm run typecheck` for those.
import { describe, expect, it } from "vitest";
import {
  double,
  shout,
  isEven,
  power,
  label,
  sum,
  describe as describeValue,
  maybeLength,
  directionSign,
  originDistance,
  formatBook,
  totalCount,
  parsePoint,
  largest,
  ends,
  swap,
  fullName,
  Counter,
  Person,
  Animal,
  Dog,
  Widget,
  identity,
  firstOrNull,
  pluck,
} from "./00_drills";

describe("part 1: annotations", () => {
  it("1. double", () => {
    expect(double(4)).toBe(8);
    expect(double(0)).toBe(0);
    expect(double(-3)).toBe(-6);
  });

  it("2. shout", () => {
    expect(shout("hi")).toBe("HI");
    expect(shout("")).toBe("");
  });

  it("3. isEven", () => {
    expect(isEven(4)).toBe(true);
    expect(isEven(7)).toBe(false);
    expect(isEven(0)).toBe(true);
  });
});

describe("part 2: optional, default, rest", () => {
  it("4. power defaults exp to 2", () => {
    expect(power(3)).toBe(9);
    expect(power(2, 3)).toBe(8);
    expect(power(5, 0)).toBe(1);
  });

  it("5. label handles a missing prefix", () => {
    expect(label("hello")).toBe("hello");
    expect(label("hello", "INFO")).toBe("INFO: hello");
  });

  it("6. sum takes any number of args", () => {
    expect(sum(1, 2, 3)).toBe(6);
    expect(sum()).toBe(0);
    expect(sum(5)).toBe(5);
  });
});

describe("part 3: unions and narrowing", () => {
  it("7. describe narrows", () => {
    expect(describeValue(5)).toBe("number: 5");
    expect(describeValue("hi")).toBe("string: hi");
  });

  it("7b. describe handles 0, which is falsy", () => {
    expect(describeValue(0), "use typeof, not if (value)").toBe("number: 0");
    expect(describeValue("")).toBe("string: ");
  });

  it("8. maybeLength", () => {
    expect(maybeLength("abc")).toBe(3);
    expect(maybeLength()).toBe(0);
    expect(maybeLength("")).toBe(0);
  });

  it("9. directionSign", () => {
    expect(directionSign("asc")).toBe(1);
    expect(directionSign("desc")).toBe(-1);
  });
});

describe("part 4: interfaces", () => {
  it("11. originDistance", () => {
    expect(originDistance({ x: 3, y: 4 })).toBe(5);
    expect(originDistance({ x: 0, y: 0 })).toBe(0);
  });

  it("13. formatBook with an author", () => {
    expect(formatBook({ title: "Dune", author: "Herbert" })).toBe(
      "Dune by Herbert"
    );
  });

  it("13b. formatBook without an author", () => {
    expect(formatBook({ title: "Beowulf" })).toBe("Beowulf by Unknown");
  });

  it("15. totalCount", () => {
    expect(totalCount({ a: 1, b: 2 })).toBe(3);
    expect(totalCount({})).toBe(0);
  });

  it("16. parsePoint", () => {
    const p = parsePoint('{"x":1,"y":2}');
    expect(p.x).toBe(1);
    expect(p.y).toBe(2);
  });
});

describe("part 5: arrays, tuples, destructuring", () => {
  it("17. largest", () => {
    expect(largest([3, 9, 1])).toBe(9);
    expect(largest([-5, -2])).toBe(-2);
  });

  it("18. ends", () => {
    expect(ends([1, 2, 3])).toEqual([1, 3]);
    expect(ends([7])).toEqual([7, 7]);
  });

  it("19. swap", () => {
    expect(swap(["a", 1])).toEqual([1, "a"]);
  });

  it("20. fullName", () => {
    expect(fullName({ first: "Ada", last: "Lovelace" })).toBe("Ada Lovelace");
  });
});

describe("part 6: classes", () => {
  it("21. Counter", () => {
    const c = new Counter(5);
    expect(c.current()).toBe(5);
    c.bump();
    c.bump();
    expect(c.current()).toBe(7);
  });

  it("22. Person has a getter, not a method", () => {
    const p = new Person("Ada", "Lovelace");
    expect(
      p.fullName,
      "fullName must be a getter, called without parentheses"
    ).toBe("Ada Lovelace");
  });

  it("23. Animal speaks", () => {
    expect(new Animal("Rex").speak()).toBe("Rex makes a sound");
  });

  it("23b. Dog overrides speak and reads the inherited name", () => {
    const d = new Dog("Fido");
    expect(d.speak()).toBe("Fido barks");
    expect(d).toBeInstanceOf(Animal);
  });

  it("24. Widget counts instances", () => {
    (Widget as unknown as { made: number }).made = 0;
    new Widget();
    new Widget();
    new Widget();
    expect((Widget as unknown as { made: number }).made).toBe(3);
  });
});

describe("part 7: generics", () => {
  it("25. identity returns the same reference", () => {
    expect(identity("hi")).toBe("hi");
    const obj = { a: 1 };
    expect(identity(obj), "return it unchanged, do not copy").toBe(obj);
  });

  it("26. firstOrNull", () => {
    expect(firstOrNull([1, 2])).toBe(1);
    expect(firstOrNull([])).toBeNull();
    expect(firstOrNull(["a"])).toBe("a");
  });

  it("27. pluck", () => {
    expect(pluck([{ id: 1 }, { id: 2 }], "id")).toEqual([1, 2]);
    expect(pluck([{ name: "Ada" }], "name")).toEqual(["Ada"]);
    expect(pluck([], "id")).toEqual([]);
  });
});
