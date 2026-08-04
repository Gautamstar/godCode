// tests: do not edit
import { describe, expect, it } from "vitest";
import { formatUser, bestSubject, parseUser } from "./02_interfaces";

describe("02 interfaces", () => {
  it("formatUser with an email", () => {
    expect(formatUser({ id: 1, name: "Ada", email: "ada@x.com" })).toBe(
      "Ada <ada@x.com>"
    );
  });

  it("formatUser without an email", () => {
    expect(formatUser({ id: 2, name: "Bob" })).toBe("Bob (no email)");
  });

  it("bestSubject", () => {
    expect(bestSubject({ math: 90, art: 72 })).toBe("math");
    expect(bestSubject({ art: 72, math: 90, cs: 88 })).toBe("math");
    expect(bestSubject({})).toBe("");
  });

  it("bestSubject keeps the first on a tie", () => {
    expect(bestSubject({ art: 90, math: 90 })).toBe("art");
  });

  it("parseUser", () => {
    const u = parseUser('{"id":7,"name":"Cy"}');
    expect(u.id).toBe(7);
    expect(u.name).toBe("Cy");
  });
});
