// tests: do not edit
import { describe, expect, it } from "vitest";
import { render, screen } from "@testing-library/react";
import userEvent from "@testing-library/user-event";
import SearchableList from "./05_search";

const FRUIT = ["Apple", "Banana", "Cherry", "grape", "Grapefruit"];

describe("05 searchable list", () => {
  it("shows everything with an empty query", () => {
    render(<SearchableList items={FRUIT} />);
    expect(screen.getAllByTestId("item")).toHaveLength(5);
    expect(screen.getByTestId("count")).toHaveTextContent("5");
  });

  it("filters as you type", async () => {
    render(<SearchableList items={FRUIT} />);
    await userEvent.type(screen.getByTestId("search"), "an");
    const texts = screen.getAllByTestId("item").map((el) => el.textContent);
    expect(texts).toEqual(["Banana"]);
  });

  it("is case-insensitive", async () => {
    render(<SearchableList items={FRUIT} />);
    await userEvent.type(screen.getByTestId("search"), "GRAPE");
    expect(screen.getAllByTestId("item")).toHaveLength(2);
  });

  it("matches anywhere in the string, not just the start", async () => {
    render(<SearchableList items={FRUIT} />);
    await userEvent.type(screen.getByTestId("search"), "rry");
    const texts = screen.getAllByTestId("item").map((el) => el.textContent);
    expect(texts).toEqual(["Cherry"]);
  });

  it("shows no-results and updates the count", async () => {
    render(<SearchableList items={FRUIT} />);
    await userEvent.type(screen.getByTestId("search"), "zzz");
    expect(screen.queryAllByTestId("item")).toHaveLength(0);
    expect(screen.getByTestId("noresults")).toHaveTextContent("No matches");
    expect(screen.getByTestId("count")).toHaveTextContent("0");
  });

  it("recovers when the query is cleared", async () => {
    render(<SearchableList items={FRUIT} />);
    const box = screen.getByTestId("search");
    await userEvent.type(box, "zzz");
    await userEvent.clear(box);
    expect(screen.getAllByTestId("item")).toHaveLength(5);
    expect(screen.queryByTestId("noresults")).toBeNull();
  });
});
