/**
 * PROBLEM : Controlled Form with Validation
 * TOPIC   : controlled inputs, form submit, validation
 * LEVEL   : Easy-Medium
 *
 * A signup form with an email and a password.
 *
 * REQUIRED data-testid values:
 *   email     - text input, controlled
 *   password  - password input, controlled
 *   submit    - submit button, DISABLED unless the form is valid
 *   error     - rendered ONLY when the email is non-empty and invalid,
 *               with the text "Invalid email"
 *   success   - rendered ONLY after a successful submit,
 *               with the text "Welcome <email>"
 *
 * Valid means: the email contains "@" AND the password is at least 6 chars.
 *
 * Hint (only peek if you are stuck):
 *   Controlled input needs BOTH value and onChange:
 *     <input value={email} onChange={(e) => setEmail(e.target.value)} />
 *   Wrap in a <form> and call e.preventDefault() in onSubmit, or the page
 *   reloads and your state is wiped.
 *
 * HOW TO RUN:  npx vitest run problems/react/03_form
 */
import { useState } from "react";

export default function SignupForm() {
  // data-testid = ""
  const [email, setEmail] = useState("")
  const [password, setPassword] = useState("")
  const emailValid = email.includes("@")
  const formValid = password.length >= 6 && emailValid
  const showError = email.length > 0 && !emailValid
  const [submitted, setSubmitted] = useState("")
  return <div>
    <form onSubmit={(e) =>
      {
        e.preventDefault();
        setSubmitted(email)
      }
    }>
    <input data-testid="email" value={email} onChange={(e)=> setEmail(e.target.value)}/>
      <input type="password" data-testid="password" value={password} onChange={(p) => setPassword(p.target.value)} />
      <button type="submit" data-testid="submit" disabled={!formValid}>
      </button>
      {submitted && <p data-testid="success">Welcome {submitted}</p>}
      {showError && <p data-testid="error">Invalid email</p>}
    </form>
  </div>;
}
