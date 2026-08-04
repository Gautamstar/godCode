/**
 * PROBLEM : Type Annotations & Functions
 * TOPIC   : TypeScript basics
 * LEVEL   : Easy
 *
 * Four small functions. The point is not the logic, it is writing the types
 * correctly so the compiler is happy and the behaviour is right.
 *
 * Hint (only peek if you are stuck):
 *   Optional parameter:  (greeting?: string)
 *   Default parameter:   (greeting: string = "Hello")
 *   Narrow a union with: if (typeof value === "number") { ... }
 *   Rest parameter:      (...nums: number[])
 *
 * HOW TO RUN:  npx vitest run problems/ts/01_annotations
 */

/** Add two numbers. */
export function add(a: number, b: number): number {
  // YOUR CODE HERE
  throw new Error("not implemented");
}

/**
 * Greet someone. `greeting` is optional and defaults to "Hello".
 *   greet("Gautam")           -> "Hello, Gautam!"
 *   greet("Gautam", "Hey")    -> "Hey, Gautam!"
 */
export function greet(name: string, greeting?: string): string {
  // YOUR CODE HERE
  throw new Error("not implemented");
}

/**
 * Describe a value that may be a string or a number.
 *   describe(42)      -> "number: 42"
 *   describe("hi")    -> "string: hi"
 * Use typeof narrowing. Do not use `as`.
 */
export function describe(value: string | number): string {
  // YOUR CODE HERE
  throw new Error("not implemented");
}

/**
 * Sum any amount of numbers passed as separate arguments.
 *   total(1, 2, 3)  -> 6
 *   total()         -> 0
 */
export function total(...nums: number[]): number {
  // YOUR CODE HERE
  throw new Error("not implemented");
}
