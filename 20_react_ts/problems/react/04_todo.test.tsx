// tests: do not edit
import { describe, expect, it } from "vitest";
import { render, screen, within } from "@testing-library/react";
import userEvent from "@testing-library/user-event";
import TodoList from "./04_todo";

async function add(text: string) {
  await userEvent.type(screen.getByTestId("input"), text);
  await userEvent.click(screen.getByTestId("add"));
}

describe("04 todo", () => {
  it("starts empty", () => {
    render(<TodoList />);
    expect(screen.queryAllByTestId("todo")).toHaveLength(0);
  });

  it("adds a todo and clears the input", async () => {
    render(<TodoList />);
    await add("buy milk");
    expect(screen.getAllByTestId("todo")).toHaveLength(1);
    expect(screen.getByTestId("text")).toHaveTextContent("buy milk");
    expect(screen.getByTestId("input")).toHaveValue("");
  });

  it("ignores blank input", async () => {
    render(<TodoList />);
    await userEvent.click(screen.getByTestId("add"));
    await add("   ");
    expect(screen.queryAllByTestId("todo")).toHaveLength(0);
  });

  it("adds several in order", async () => {
    render(<TodoList />);
    await add("one");
    await add("two");
    const texts = screen.getAllByTestId("text").map((el) => el.textContent);
    expect(texts).toEqual(["one", "two"]);
  });

  it("toggles done", async () => {
    render(<TodoList />);
    await add("one");
    const row = screen.getByTestId("todo");
    await userEvent.click(within(row).getByTestId("toggle"));
    expect(within(row).getByTestId("text")).toHaveClass("done");
    await userEvent.click(within(row).getByTestId("toggle"));
    expect(within(row).getByTestId("text")).not.toHaveClass("done");
  });

  it("deletes only the clicked row", async () => {
    render(<TodoList />);
    await add("one");
    await add("two");
    const rows = screen.getAllByTestId("todo");
    await userEvent.click(within(rows[0]).getByTestId("delete"));
    const texts = screen.getAllByTestId("text").map((el) => el.textContent);
    expect(texts).toEqual(["two"]);
  });

  it("counts the remaining undone todos", async () => {
    render(<TodoList />);
    await add("one");
    await add("two");
    expect(screen.getByTestId("remaining")).toHaveTextContent("2");
    const rows = screen.getAllByTestId("todo");
    await userEvent.click(within(rows[0]).getByTestId("toggle"));
    expect(screen.getByTestId("remaining")).toHaveTextContent("1");
  });
});
