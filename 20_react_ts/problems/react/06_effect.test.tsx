// tests: do not edit
import { afterEach, beforeEach, describe, expect, it, vi } from "vitest";
import { act, render, screen } from "@testing-library/react";
import Clock from "./06_effect";

beforeEach(() => vi.useFakeTimers());
afterEach(() => vi.useRealTimers());

function click(el: HTMLElement) {
  act(() => {
    el.dispatchEvent(new MouseEvent("click", { bubbles: true }));
  });
}

function advance(ms: number) {
  act(() => {
    vi.advanceTimersByTime(ms);
  });
}

describe("06 useEffect", () => {
  it("starts at 0 and stopped", () => {
    render(<Clock />);
    expect(screen.getByTestId("seconds")).toHaveTextContent("0");
    advance(3000);
    expect(screen.getByTestId("seconds")).toHaveTextContent("0");
  });

  it("ticks once per second while running", () => {
    render(<Clock />);
    click(screen.getByTestId("toggle"));
    advance(3000);
    expect(screen.getByTestId("seconds")).toHaveTextContent("3");
  });

  it("holds the value when stopped", () => {
    render(<Clock />);
    const toggle = screen.getByTestId("toggle");
    click(toggle);
    advance(2000);
    click(toggle);
    advance(5000);
    expect(screen.getByTestId("seconds")).toHaveTextContent("2");
  });

  it("clears the interval on unmount", () => {
    const { unmount } = render(<Clock />);
    click(screen.getByTestId("toggle"));
    advance(1000);
    unmount();
    expect(vi.getTimerCount()).toBe(0);
  });
});
