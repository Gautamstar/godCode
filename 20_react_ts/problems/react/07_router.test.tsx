// tests: do not edit
import { describe, expect, it } from "vitest";
import { render, screen } from "@testing-library/react";
import userEvent from "@testing-library/user-event";
import { MemoryRouter } from "react-router-dom";
import Nav from "./07_router";

function at(path: string) {
  return render(
    <MemoryRouter initialEntries={[path]}>
      <Nav />
    </MemoryRouter>
  );
}

describe("07 routing", () => {
  it("renders Home at /", () => {
    at("/");
    expect(screen.getByTestId("page")).toHaveTextContent("Home");
  });

  it("renders About at /about", () => {
    at("/about");
    expect(screen.getByTestId("page")).toHaveTextContent("About");
  });

  it("renders Not Found for an unknown path", () => {
    at("/nope");
    expect(screen.getByTestId("page")).toHaveTextContent("Not Found");
  });

  it("navigates by clicking a link", async () => {
    at("/");
    await userEvent.click(screen.getByTestId("link-about"));
    expect(screen.getByTestId("page")).toHaveTextContent("About");
    await userEvent.click(screen.getByTestId("link-home"));
    expect(screen.getByTestId("page")).toHaveTextContent("Home");
  });
});
