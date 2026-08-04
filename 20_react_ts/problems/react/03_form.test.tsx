// tests: do not edit
import { describe, expect, it } from "vitest";
import { render, screen } from "@testing-library/react";
import userEvent from "@testing-library/user-event";
import SignupForm from "./03_form";

describe("03 form", () => {
  it("inputs are controlled", async () => {
    render(<SignupForm />);
    const email = screen.getByTestId("email");
    await userEvent.type(email, "a@b.com");
    expect(email).toHaveValue("a@b.com");
  });

  it("submit starts disabled", () => {
    render(<SignupForm />);
    expect(screen.getByTestId("submit")).toBeDisabled();
  });

  it("shows an error for an invalid non-empty email", async () => {
    render(<SignupForm />);
    await userEvent.type(screen.getByTestId("email"), "nope");
    expect(screen.getByTestId("error")).toHaveTextContent("Invalid email");
  });

  it("no error while the email is still empty", () => {
    render(<SignupForm />);
    expect(screen.queryByTestId("error")).toBeNull();
  });

  it("stays disabled when the password is too short", async () => {
    render(<SignupForm />);
    await userEvent.type(screen.getByTestId("email"), "a@b.com");
    await userEvent.type(screen.getByTestId("password"), "12345");
    expect(screen.getByTestId("submit")).toBeDisabled();
  });

  it("enables and submits when valid", async () => {
    render(<SignupForm />);
    await userEvent.type(screen.getByTestId("email"), "a@b.com");
    await userEvent.type(screen.getByTestId("password"), "123456");

    const submit = screen.getByTestId("submit");
    expect(submit).toBeEnabled();
    expect(screen.queryByTestId("success")).toBeNull();

    await userEvent.click(submit);
    expect(screen.getByTestId("success")).toHaveTextContent("Welcome a@b.com");
  });
});
