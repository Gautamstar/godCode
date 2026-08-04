import { useState } from "react";

export default function SignupForm() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [submitted, setSubmitted] = useState("");

  // Derived, not stored. These recompute on every render, so they can never
  // disagree with the inputs.
  const emailOk = email.includes("@");
  const valid = emailOk && password.length >= 6;
  const showError = email.length > 0 && !emailOk;

  function handleSubmit(e: React.FormEvent) {
    // Without this the browser does a full page navigation and every piece
    // of state resets. It is the number one form bug.
    e.preventDefault();
    setSubmitted(email);
  }

  return (
    <form onSubmit={handleSubmit}>
      {/* A controlled input needs BOTH value and onChange. With value alone
          the box is read-only; with onChange alone React never re-renders. */}
      <input
        data-testid="email"
        value={email}
        onChange={(e) => setEmail(e.target.value)}
        placeholder="email"
      />
      <input
        data-testid="password"
        type="password"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
        placeholder="password"
      />

      {showError && <p data-testid="error">Invalid email</p>}

      <button data-testid="submit" type="submit" disabled={!valid}>
        Sign up
      </button>

      {submitted && <p data-testid="success">Welcome {submitted}</p>}
    </form>
  );
}
