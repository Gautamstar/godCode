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
  // YOUR CODE HERE
  return <div>replace me</div>;
}
