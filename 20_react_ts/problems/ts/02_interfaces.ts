/**
 * PROBLEM : Interfaces, Optional Properties & Assertions
 * TOPIC   : TypeScript basics
 * LEVEL   : Easy
 *
 * Interfaces describe the SHAPE of an object. This is the single most common
 * TypeScript question type on a basic assessment.
 *
 * Hint (only peek if you are stuck):
 *   Optional property:  email?: string
 *   Index signature:    [subject: string]: number
 *   Assertion:          JSON.parse(json) as User
 *
 * HOW TO RUN:  npx vitest run problems/ts/02_interfaces
 */

/**
 * Describe a user: a numeric id, a name, and an OPTIONAL email.
 */
export interface User {
  // YOUR CODE HERE
}

/**
 * Format a user for display.
 *   { id: 1, name: "Ada", email: "ada@x.com" }  ->  "Ada <ada@x.com>"
 *   { id: 2, name: "Bob" }                      ->  "Bob (no email)"
 */
export function formatUser(u: User): string {
  // YOUR CODE HERE
  throw new Error("not implemented");
}

/**
 * A record of subject name -> score. Any subject name is allowed, so this
 * needs an index signature rather than named properties.
 */
export interface Scores {
  // YOUR CODE HERE
}

/**
 * Return the subject with the highest score.
 *   bestSubject({ math: 90, art: 72 })  ->  "math"
 * If the object is empty, return "".
 * On a tie, return whichever subject appears first.
 */
export function bestSubject(scores: Scores): string {
  // YOUR CODE HERE
  throw new Error("not implemented");
}

/**
 * Parse a JSON string into a User.
 * JSON.parse returns `any`, so you must assert the result is a User.
 */
export function parseUser(json: string): User {
  // YOUR CODE HERE
  throw new Error("not implemented");
}
