// tests: do not edit
import { describe, expect, it } from "vitest";
import { render, screen } from "@testing-library/react";
import ItemList from "./02_list";

describe("02 list", () => {
  it("renders one li per item", () => {
    render(<ItemList items={["apple", "banana", "cherry"]} />);
    const items = screen.getAllByTestId("item");
    expect(items).toHaveLength(3);
    expect(items[0]).toHaveTextContent("apple");
    expect(items[2]).toHaveTextContent("cherry");
  });

  it("shows the count", () => {
    render(<ItemList items={["a", "b"]} />);
    expect(screen.getByTestId("count")).toHaveTextContent("2");
  });

  it("shows the empty state and hides the list", () => {
    render(<ItemList items={[]} />);
    expect(screen.getByTestId("empty")).toHaveTextContent("No items");
    expect(screen.queryByTestId("list")).toBeNull();
    expect(screen.queryAllByTestId("item")).toHaveLength(0);
  });

  it("hides the empty state when there are items", () => {
    render(<ItemList items={["a"]} />);
    expect(screen.queryByTestId("empty")).toBeNull();
    expect(screen.getByTestId("list")).toBeInTheDocument();
  });
});
