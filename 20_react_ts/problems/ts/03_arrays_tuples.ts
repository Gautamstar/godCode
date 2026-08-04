/**
 * PROBLEM : Arrays, Tuples & Destructuring
 * TOPIC   : TypeScript basics
 * LEVEL   : Easy
 *
 * An array is any length, all one type:      number[]
 * A tuple is a FIXED length with a type per slot:  [string, number]
 *
 * Hint (only peek if you are stuck):
 *   Destructure an array:   const [a, b] = pair;
 *   Destructure an object:  function f({ first, last }: Name) { ... }
 *   Copy before sorting:    [...nums].sort((a, b) => b - a)
 *
 * HOW TO RUN:  npx vitest run problems/ts/03_arrays_tuples
 */

/**
 * Return the first and last elements as a two-slot tuple.
 *   firstAndLast([1, 2, 3])  ->  [1, 3]
 *   firstAndLast([5])        ->  [5, 5]
 * Assume the array is never empty.
 */
export function firstAndLast(nums: number[]): [number, number] {
  // YOUR CODE HERE
  throw new Error("not implemented");
}

/**
 * Flip a [string, number] tuple into a [number, string] tuple.
 *   swap(["age", 30])  ->  [30, "age"]
 * Destructure the input, do not index into it.
 */
export function swap(pair: [string, number]): [number, string] {
  // YOUR CODE HERE
  throw new Error("not implemented");
}

export interface Name {
  first: string;
  last: string;
}

/**
 * Build a full name. Destructure the parameter in the signature.
 *   fullName({ first: "Ada", last: "Lovelace" })  ->  "Ada Lovelace"
 */
export function fullName(name: Name): string {
  // YOUR CODE HERE
  throw new Error("not implemented");
}

/**
 * Return the three largest numbers, highest first.
 *   topThree([4, 9, 1, 7, 3])  ->  [9, 7, 4]
 * If there are fewer than three, return all of them sorted high to low.
 * Do NOT mutate the input array. The test checks that.
 */
export function topThree(nums: number[]): number[] {
  // YOUR CODE HERE
  throw new Error("not implemented");
}
