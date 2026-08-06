/**
 * TYPESCRIPT DRILLS - one idea at a time.
 *
 * Same format as the React drills. Each one adds exactly ONE thing to the one
 * before it. Most are a single line.
 *
 * TWO GRADERS, and you need both:
 *
 *   npx vitest problems/ts/00_drills     checks BEHAVIOUR (what the code does)
 *   npm run typecheck                    checks TYPES (what you annotated)
 *
 * This matters because types are erased before the code runs. vitest will
 * happily pass a function with no annotations at all. The typecheck is the
 * only thing that grades the actual TypeScript.
 *
 * EXPECT RED SQUIGGLES on every unfinished drill. A missing annotation is an
 * error under `strict`, so the squiggle IS the instruction. They disappear as
 * you fill each one in.
 */

// ---------------------------------------------------------------------------
// PART 1: annotations
// ---------------------------------------------------------------------------

// 1. Return n doubled. Annotate the parameter AND the return type.
//
//    A parameter with no annotation is an implicit `any`, which turns the
//    checker off for that value. Under `strict` that is an error.
//
//    Shape:  function name(param: Type): ReturnType { }
export function double(n) {
  // YOUR CODE HERE
  throw new Error("not implemented");
}

// 2. Return the string in UPPERCASE.  shout("hi") -> "HI"
//
//    Same shape, different types. The method you want is .toUpperCase()
export function shout(s) {
  // YOUR CODE HERE
  throw new Error("not implemented");
}

// 3. Return true when n is even.
//
//    The return type here is `boolean`. `n % 2 === 0` already produces one,
//    so you do not need an if statement.
export function isEven(n) {
  // YOUR CODE HERE
  throw new Error("not implemented");
}

// ---------------------------------------------------------------------------
// PART 2: optional, default, and rest parameters
// ---------------------------------------------------------------------------

// 4. Raise base to exp. `exp` DEFAULTS to 2 when not passed.
//      power(3)     -> 9
//      power(2, 3)  -> 8
//
//    A default value is written in the signature:  exp: number = 2
//    Giving a default automatically makes the parameter optional.
export function power(base, exp) {
  // YOUR CODE HERE
  throw new Error("not implemented");
}

// 5. Join a prefix and text with ": ". If prefix is missing, return text alone.
//      label("hello")           -> "hello"
//      label("hello", "INFO")   -> "INFO: hello"
//
//    Mark it optional with a question mark:  prefix?: string
//    Inside, its type is `string | undefined`, so the compiler forces you to
//    handle the missing case. That is the entire point of the `?`.
export function label(text, prefix) {
  // YOUR CODE HERE
  throw new Error("not implemented");
}

// 6. Add up any number of arguments.
//      sum(1, 2, 3)  -> 6
//      sum()         -> 0
//
//    A rest parameter collects whatever is left into a real array:
//      ...nums: number[]
//    It must be the LAST parameter.
export function sum(...nums) {
  // YOUR CODE HERE
  throw new Error("not implemented");
}

// ---------------------------------------------------------------------------
// PART 3: unions and narrowing
// ---------------------------------------------------------------------------

// 7. Return "number: 5" or "string: hi" depending on what came in.
//    Annotate the parameter as a union of string and number.
//
//    A union is written with a pipe:  value: string | number
//    Then `typeof value === "number"` NARROWS it, meaning inside that branch
//    the compiler knows it is a number and lets you use number methods.
//
//    Careful: do not write `if (value)`. The number 0 is falsy and would take
//    the wrong branch.
export function describe(value) {
  // YOUR CODE HERE
  throw new Error("not implemented");
}

// 8. Return the length of the string, or 0 if nothing was passed.
//      maybeLength("abc")  -> 3
//      maybeLength()       -> 0
//
//    Optional parameter again, but this time the missing case needs a real
//    answer rather than a different string.
export function maybeLength(s) {
  // YOUR CODE HERE
  throw new Error("not implemented");
}

// 9. Return 1 for "asc" and -1 for "desc".
//
//    Annotate `dir` as a LITERAL union:  dir: "asc" | "desc"
//    Those are exact string values used as types, so passing "up" becomes a
//    compile error instead of a silent wrong answer. This is very common for
//    options and modes.
export function directionSign(dir) {
  // YOUR CODE HERE
  throw new Error("not implemented");
}

// ---------------------------------------------------------------------------
// PART 4: interfaces
// ---------------------------------------------------------------------------

// 10. Describe a point with two numbers, x and y.
//
//     An interface names the SHAPE of an object. Fill in the two properties.
export interface Point {
  // YOUR CODE HERE
}

// 11. Return the distance of a point from the origin.
//       originDistance({ x: 3, y: 4 })  ->  5
//
//     Annotate the parameter with the interface you just wrote.
//     Math.sqrt and ** 2 are what you need.
export function originDistance(p) {
  // YOUR CODE HERE
  throw new Error("not implemented");
}

// 12. Describe a book: a title, and an OPTIONAL author.
export interface Book {
  // YOUR CODE HERE
}

// 13. Format a book.
//       formatBook({ title: "Dune", author: "Herbert" })  -> "Dune by Herbert"
//       formatBook({ title: "Beowulf" })                  -> "Beowulf by Unknown"
//
//     Because `author` is optional its type includes `undefined`, so you have
//     to decide what happens when it is missing.
export function formatBook(b) {
  // YOUR CODE HERE
  throw new Error("not implemented");
}

// 14. Describe a bag of counts: any string key, number values.
//
//     Use an INDEX SIGNATURE when the keys are data rather than a fixed set:
//       [key: string]: number
export interface Counts {
  // YOUR CODE HERE
}

// 15. Add up every value in a Counts object.
//       totalCount({ a: 1, b: 2 })  ->  3
//
//     Object.values(obj) gives you an array of the values.
export function totalCount(c) {
  // YOUR CODE HERE
  throw new Error("not implemented");
}

// 16. Parse a JSON string into a Point.
//
//     JSON.parse returns `any`. An ASSERTION tells the compiler what shape to
//     expect:  JSON.parse(text) as Point
//     It is a promise you are making. Nothing is checked at runtime.
export function parsePoint(text) {
  // YOUR CODE HERE
  throw new Error("not implemented");
}

// ---------------------------------------------------------------------------
// PART 5: arrays, tuples, destructuring
// ---------------------------------------------------------------------------

// 17. Return the largest number in the array.
//     Annotate the parameter as an array of numbers:  nums: number[]
//
//     Math.max(...nums) spreads the array into separate arguments.
export function largest(nums) {
  // YOUR CODE HERE
  throw new Error("not implemented");
}

// 18. Return the first and last item as a TUPLE.
//       ends([1, 2, 3])  ->  [1, 3]
//
//     An array is any length, all one type:      number[]
//     A tuple is a fixed length, type per slot:  [number, number]
//     The annotation is what carries that meaning, so write it on the return.
export function ends(nums) {
  // YOUR CODE HERE
  throw new Error("not implemented");
}

// 19. Swap a two-slot tuple.  swap(["a", 1]) -> [1, "a"]
//
//     DESTRUCTURE the input rather than indexing into it:
//       const [first, second] = pair;
export function swap(pair) {
  // YOUR CODE HERE
  throw new Error("not implemented");
}

// 20. Build a full name from an object with `first` and `last`.
//       fullName({ first: "Ada", last: "Lovelace" })  ->  "Ada Lovelace"
//
//     Destructure in the SIGNATURE, the same way React props do it:
//       function f({ first, last }: SomeType)
//     Define the parameter's type inline or with an interface, your choice.
export function fullName(person) {
  // YOUR CODE HERE
  throw new Error("not implemented");
}

// ---------------------------------------------------------------------------
// PART 6: classes
// ---------------------------------------------------------------------------

// 21. A Counter that starts at a given number and can be bumped.
//
//     Use a PARAMETER PROPERTY: putting an access modifier on a constructor
//     parameter declares the field and assigns it in one line.
//       constructor(private value: number) {}
//     Without a modifier it is just an argument that vanishes when the
//     constructor ends.
//
//     bump() adds 1. current() returns the value.
export class Counter {
  // YOUR CODE HERE (constructor, bump, current)
}

// 22. A Person with a `fullName` GETTER.
//
//     A getter is called WITHOUT parentheses:  person.fullName
//       get fullName(): string { return ...; }
//     Store first and last as public parameter properties.
export class Person {
  // YOUR CODE HERE (constructor, get fullName)
}

// 23. An Animal that speaks, and a Dog that speaks differently.
//
//     Animal:  constructor takes a name. Make it `protected` so subclasses can
//              read it but outside code cannot.
//              speak() returns "<name> makes a sound"
//     Dog:     extends Animal, overrides speak() to return "<name> barks"
//              The subclass constructor must call super(name) FIRST, before
//              any use of `this`.
export class Animal {
  // YOUR CODE HERE
}

export class Dog extends Animal {
  // YOUR CODE HERE
}

// 24. A Widget that counts how many have ever been created.
//
//     A STATIC member belongs to the class, not to an instance:
//       static made = 0;
//     Read and write it as Widget.made, never this.made.
export class Widget {
  // YOUR CODE HERE (static made, constructor that increments it)
}

// ---------------------------------------------------------------------------
// PART 7: generics
// ---------------------------------------------------------------------------

// 25. Return the argument unchanged, KEEPING its type.
//
//     A generic is a type the caller fills in:  function identity<T>(x: T): T
//     Compare `(x: any): any`, which compiles but throws away everything the
//     compiler knew, so identity(7).toUpperCase() would slip through.
export function identity(x) {
  // YOUR CODE HERE
  throw new Error("not implemented");
}

// 26. Return the first element, or null when the array is empty.
//       firstOrNull([1, 2])  ->  1
//       firstOrNull([])      ->  null
//
//     The return type is a union of the element type and null:  T | null
export function firstOrNull(xs) {
  // YOUR CODE HERE
  throw new Error("not implemented");
}

// 27. Pull one property out of every object in a list.
//       pluck([{ id: 1 }, { id: 2 }], "id")  ->  [1, 2]
//
//     Two type parameters. `keyof T` is the union of T's property names, and
//     `K extends keyof T` says the key must really exist on T, so a typo is a
//     compile error rather than an array of undefined.
//     The return type is T[K][] : the type of that property, arrayed.
export function pluck(items, key) {
  // YOUR CODE HERE
  throw new Error("not implemented");
}
