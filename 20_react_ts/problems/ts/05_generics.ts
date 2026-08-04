/**
 * PROBLEM : Generics & Narrowing
 * TOPIC   : TypeScript basics
 * LEVEL   : Easy-Medium
 *
 * A generic is a type PARAMETER. `<T>` means "some type the caller picks",
 * so one function works for strings, numbers, or objects without using `any`
 * and without losing the type on the way out.
 *
 * Hint (only peek if you are stuck):
 *   Generic function:  function identity<T>(x: T): T
 *   Constraint:        <K extends keyof T>
 *   Indexed type:      T[K]
 *
 * HOW TO RUN:  npx vitest run problems/ts/05_generics
 */

/**
 * Return the argument unchanged, keeping its type.
 *   identity("hi")  ->  "hi"   (typed string, not any)
 */
export function identity<T>(x: T): T {
  // YOUR CODE HERE
  throw new Error("not implemented");
}

/**
 * Return the first element, or null if the array is empty.
 *   firstOrNull([1, 2])  ->  1
 *   firstOrNull([])      ->  null
 */
export function firstOrNull<T>(xs: T[]): T | null {
  // YOUR CODE HERE
  throw new Error("not implemented");
}

/**
 * Pull one property out of every object in a list.
 *   pluck([{ id: 1 }, { id: 2 }], "id")  ->  [1, 2]
 *
 * `K extends keyof T` means the key must actually exist on T, so a typo is a
 * compile error rather than a runtime undefined.
 */
export function pluck<T, K extends keyof T>(items: T[], key: K): T[K][] {
  // YOUR CODE HERE
  throw new Error("not implemented");
}

/**
 * Group values by the string a function returns for them.
 *   groupBy(["ant", "bee", "ape"], w => w[0])
 *     ->  { a: ["ant", "ape"], b: ["bee"] }
 */
export function groupBy<T>(
  items: T[],
  keyOf: (item: T) => string
): Record<string, T[]> {
  // YOUR CODE HERE
  throw new Error("not implemented");
}
