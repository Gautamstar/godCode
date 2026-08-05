// tests: do not edit
import { describe, expect, it, vi } from "vitest";
import { render, screen } from "@testing-library/react";
import userEvent from "@testing-library/user-event";
import {
  Hello,
  Greeting,
  Total,
  Loud,
  Styled,
  Pair,
  Echo,
  Score,
  Welcome,
  Switch,
  SwitchTernary,
  MaybeError,
  ItemsBadge,
  WordList,
  UserList,
  LongWords,
  GoButton,
  DeleteButton,
  ShowState,
  Clicker,
  DoubleClicker,
  TextMirror,
  Toggle,
} from "./00_drills";

const textOf = (el: HTMLElement) => (el.textContent ?? "").trim();

describe("part 1: JSX", () => {
  it("1. Hello renders a paragraph", () => {
    const { container } = render(<Hello />);
    const p = container.querySelector("p");
    expect(p, "expected a <p> element").not.toBeNull();
    expect(textOf(p as HTMLElement)).toBe("Hello");
  });

  it("2. Greeting prints the variable, not the word", () => {
    const { container } = render(<Greeting />);
    expect(textOf(container)).toBe("Gautam");
  });

  it("3. Total evaluates the expression", () => {
    const { container } = render(<Total />);
    expect(textOf(container)).toBe("5");
  });

  it("4. Loud uses className", () => {
    const { container } = render(<Loud />);
    const p = container.querySelector("p");
    expect(p, "expected a <p> element").not.toBeNull();
    expect(p).toHaveClass("big");
    expect(textOf(p as HTMLElement)).toBe("Loud");
  });

  it("5. Styled reads the class from a variable", () => {
    const { container } = render(<Styled />);
    expect(container.querySelector("p")).toHaveClass("warning");
  });

  it("6. Pair renders two paragraphs with no wrapper div", () => {
    const { container } = render(<Pair />);
    const ps = container.querySelectorAll("p");
    expect(ps).toHaveLength(2);
    expect(textOf(ps[0] as HTMLElement)).toBe("one");
    expect(textOf(ps[1] as HTMLElement)).toBe("two");
    expect(
      container.querySelectorAll("div"),
      "use a fragment <>...</>, not a <div>"
    ).toHaveLength(0);
  });
});

describe("part 2: props", () => {
  it("7. Echo shows the text prop", () => {
    const { container } = render(<Echo text="hi there" />);
    expect(textOf(container)).toBe("hi there");
  });

  it("8. Score shows a number prop", () => {
    const { container } = render(<Score count={42} />);
    expect(textOf(container)).toBe("42");
  });

  it("9. Welcome mixes text and a prop", () => {
    const { container } = render(<Welcome name="Ada" />);
    expect(textOf(container)).toBe("Hi, Ada!");
  });
});

describe("part 3: conditionals", () => {
  it("10. Switch picks a branch", () => {
    expect(textOf(render(<Switch isOn={true} />).container)).toBe("ON");
    expect(textOf(render(<Switch isOn={false} />).container)).toBe("OFF");
  });

  it("11. SwitchTernary picks inside one element", () => {
    const on = render(<SwitchTernary isOn={true} />).container;
    expect(on.querySelectorAll("p")).toHaveLength(1);
    expect(textOf(on)).toBe("ON");
    expect(textOf(render(<SwitchTernary isOn={false} />).container)).toBe("OFF");
  });

  it("12. MaybeError shows only when true", () => {
    expect(textOf(render(<MaybeError hasError={true} />).container)).toBe(
      "Error!"
    );
    expect(textOf(render(<MaybeError hasError={false} />).container)).toBe("");
  });

  it("13. ItemsBadge does not leak a 0 onto the page", () => {
    expect(textOf(render(<ItemsBadge count={2} />).container)).toBe("Has items");
    expect(
      textOf(render(<ItemsBadge count={0} />).container),
      "compare count > 0, or React prints the 0"
    ).toBe("");
  });
});

describe("part 4: lists", () => {
  it("14. WordList renders one li per word", () => {
    const { container } = render(<WordList words={["a", "b", "c"]} />);
    expect(container.querySelector("ul")).not.toBeNull();
    const lis = container.querySelectorAll("li");
    expect(lis).toHaveLength(3);
    expect(textOf(lis[1] as HTMLElement)).toBe("b");
  });

  it("14b. WordList sets a key (no React warning)", () => {
    const spy = vi.spyOn(console, "error").mockImplementation(() => {});
    render(<WordList words={["x", "y"]} />);
    const warned = spy.mock.calls.some((args) =>
      String(args[0]).includes("unique \"key\"")
    );
    spy.mockRestore();
    expect(warned, "each <li> needs a key prop").toBe(false);
  });

  it("15. UserList shows each name", () => {
    const users = [
      { id: 1, name: "Ada" },
      { id: 2, name: "Bob" },
    ];
    const { container } = render(<UserList users={users} />);
    const names = [...container.querySelectorAll("li")].map((li) =>
      textOf(li as HTMLElement)
    );
    expect(names).toEqual(["Ada", "Bob"]);
  });

  it("16. LongWords filters before mapping", () => {
    const { container } = render(
      <LongWords words={["hi", "tree", "a", "house"]} />
    );
    const shown = [...container.querySelectorAll("li")].map((li) =>
      textOf(li as HTMLElement)
    );
    expect(shown).toEqual(["tree", "house"]);
  });
});

describe("part 5: events", () => {
  it("17. GoButton calls the handler on click, not on render", async () => {
    const onGo = vi.fn();
    render(<GoButton onGo={onGo} />);
    expect(onGo, "do not call onGo during render").not.toHaveBeenCalled();
    await userEvent.click(screen.getByRole("button"));
    expect(onGo).toHaveBeenCalledTimes(1);
  });

  it("18. DeleteButton passes the id", async () => {
    const onDelete = vi.fn();
    render(<DeleteButton id={9} onDelete={onDelete} />);
    expect(onDelete, "wrap it in an arrow function").not.toHaveBeenCalled();
    await userEvent.click(screen.getByRole("button"));
    expect(onDelete).toHaveBeenCalledWith(9);
  });
});

describe("part 6: state", () => {
  it("19. ShowState displays the initial value", () => {
    const { container } = render(<ShowState />);
    expect(textOf(container)).toBe("7");
  });

  it("20. Clicker increments", async () => {
    const { container } = render(<Clicker />);
    const p = container.querySelector("p") as HTMLElement;
    expect(textOf(p)).toBe("0");
    await userEvent.click(screen.getByRole("button"));
    expect(textOf(p)).toBe("1");
    await userEvent.click(screen.getByRole("button"));
    expect(textOf(p)).toBe("2");
  });

  it("21. DoubleClicker adds 2 per click", async () => {
    const { container } = render(<DoubleClicker />);
    const p = container.querySelector("p") as HTMLElement;
    await userEvent.click(screen.getByRole("button"));
    expect(
      textOf(p),
      "two setCount(count + 1) calls only add 1; use setCount((c) => c + 1)"
    ).toBe("2");
    await userEvent.click(screen.getByRole("button"));
    expect(textOf(p)).toBe("4");
  });

  it("22. TextMirror is a controlled input", async () => {
    const { container } = render(<TextMirror />);
    const input = container.querySelector("input") as HTMLInputElement;
    expect(input, "expected an <input>").not.toBeNull();
    await userEvent.type(input, "abc");
    expect(input, "the input needs value={text}").toHaveValue("abc");
    expect(textOf(container.querySelector("p") as HTMLElement)).toBe("abc");
  });

  it("23. Toggle flips", async () => {
    const { container } = render(<Toggle />);
    const p = container.querySelector("p") as HTMLElement;
    const button = screen.getByRole("button");
    expect(textOf(p)).toBe("off");
    await userEvent.click(button);
    expect(textOf(p)).toBe("on");
    await userEvent.click(button);
    expect(textOf(p)).toBe("off");
  });
});
