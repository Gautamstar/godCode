// tests: do not edit
import { beforeEach, describe, expect, it } from "vitest";
import { Animal, Dog } from "./04_classes";

describe("04 classes", () => {
  beforeEach(() => {
    (Animal as unknown as { count: number }).count = 0;
  });

  it("Animal speaks", () => {
    expect(new Animal("Rex").speak()).toBe("Rex makes a sound");
  });

  it("Animal has a label getter, not a method", () => {
    const a = new Animal("Rex");
    expect(a.label).toBe("Animal: Rex");
  });

  it("name is not exposed publicly", () => {
    const a = new Animal("Rex") as unknown as Record<string, unknown>;
    // protected fields still exist at runtime, but must not be `public name`
    // on the type. This just confirms the value was actually stored.
    expect(a.name).toBe("Rex");
  });

  it("Dog overrides speak", () => {
    expect(new Dog("Fido", "corgi").speak()).toBe("Fido barks");
  });

  it("Dog can read the inherited name", () => {
    expect(new Dog("Fido", "corgi").describe()).toBe("Fido is a corgi");
  });

  it("Dog is an Animal", () => {
    expect(new Dog("Fido", "corgi")).toBeInstanceOf(Animal);
  });

  it("static count includes subclasses", () => {
    new Animal("a");
    new Dog("b", "pug");
    new Dog("c", "pug");
    expect((Animal as unknown as { count: number }).count).toBe(3);
  });
});
