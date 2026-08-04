// tests: do not edit
import { describe, expect, it } from "vitest";
import { render, screen } from "@testing-library/react";
import userEvent from "@testing-library/user-event";
import Counter from "./01_counter";

describe("01 counter", () => {
  it("renders the starting value", () => {
    render(<Counter start={5} />);
    expect(screen.getByTestId("value")).toHaveTextContent("5");
  });

  it("increments", async () => {
    render(<Counter start={0} />);
    await userEvent.click(screen.getByTestId("inc"));
    await userEvent.click(screen.getByTestId("inc"));
    expect(screen.getByTestId("value")).toHaveTextContent("2");
  });

  it("decrements", async () => {
    render(<Counter start={0} />);
    await userEvent.click(screen.getByTestId("dec"));
    expect(screen.getByTestId("value")).toHaveTextContent("-1");
  });

  it("resets back to start", async () => {
    render(<Counter start={3} />);
    await userEvent.click(screen.getByTestId("inc"));
    await userEvent.click(screen.getByTestId("inc"));
    await userEvent.click(screen.getByTestId("reset"));
    expect(screen.getByTestId("value")).toHaveTextContent("3");
  });
});
