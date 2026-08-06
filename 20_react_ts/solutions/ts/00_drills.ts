// PART 1: annotations

export function double(n: number): number {
  return n * 2;
}

export function shout(s: string): string {
  return s.toUpperCase();
}

// `n % 2 === 0` is already a boolean, so no if statement is needed
export function isEven(n: number): boolean {
  return n % 2 === 0;
}

// PART 2: optional, default, rest

// a default value makes the parameter optional automatically, and the body
// never has to handle undefined
export function power(base: number, exp: number = 2): number {
  return base ** exp;
}

// `prefix?: string` means its type is `string | undefined` inside, so the
// compiler forces this check
export function label(text: string, prefix?: string): string {
  if (prefix === undefined) return text;
  return `${prefix}: ${text}`;
}

// a rest parameter collects the remaining arguments into a real array
export function sum(...nums: number[]): number {
  return nums.reduce((total, n) => total + n, 0);
}

// PART 3: unions and narrowing

// typeof narrowing: inside the if, the compiler knows `value` is a number.
// `if (value)` would be wrong because 0 is falsy and would take the string branch.
export function describe(value: string | number): string {
  if (typeof value === "number") return `number: ${value}`;
  return `string: ${value}`;
}

export function maybeLength(s?: string): number {
  if (s === undefined) return 0;
  return s.length;
}

// a literal union: the type is the exact allowed values, so directionSign("up")
// is a compile error rather than a silent undefined
export function directionSign(dir: "asc" | "desc"): number {
  return dir === "asc" ? 1 : -1;
}

// PART 4: interfaces

export interface Point {
  x: number;
  y: number;
}

export function originDistance(p: Point): number {
  return Math.sqrt(p.x ** 2 + p.y ** 2);
}

export interface Book {
  title: string;
  author?: string; // the ? makes it optional
}

export function formatBook(b: Book): string {
  // b.author is `string | undefined`, so the missing case has to be handled
  return `${b.title} by ${b.author ?? "Unknown"}`;
}

// an index signature: any string key, number values. Use it when the key names
// are data rather than part of a fixed schema.
export interface Counts {
  [key: string]: number;
}

export function totalCount(c: Counts): number {
  return Object.values(c).reduce((total, n) => total + n, 0);
}

export function parsePoint(text: string): Point {
  // JSON.parse returns `any`. The assertion is a promise you are making,
  // not a runtime check.
  return JSON.parse(text) as Point;
}

// PART 5: arrays, tuples, destructuring

export function largest(nums: number[]): number {
  return Math.max(...nums);
}

// the tuple annotation is load-bearing. Without it TypeScript infers number[]
// and callers lose the fixed length.
export function ends(nums: number[]): [number, number] {
  return [nums[0], nums[nums.length - 1]];
}

export function swap(pair: [string, number]): [number, string] {
  const [first, second] = pair;
  return [second, first];
}

// destructuring in the signature: still one argument, you just name its pieces
export function fullName({
  first,
  last,
}: {
  first: string;
  last: string;
}): string {
  return `${first} ${last}`;
}

// PART 6: classes

export class Counter {
  // parameter property: declares the field, assigns it, and sets visibility
  // in one line. Without the modifier it would be a plain argument.
  constructor(private value: number) {}

  bump(): void {
    this.value++;
  }

  current(): number {
    return this.value;
  }
}

export class Person {
  constructor(public first: string, public last: string) {}

  // a getter is read as person.fullName, with no parentheses
  get fullName(): string {
    return `${this.first} ${this.last}`;
  }
}

export class Animal {
  // protected = readable here and in subclasses, not from outside.
  // `private` would break Dog.
  constructor(protected name: string) {}

  speak(): string {
    return `${this.name} makes a sound`;
  }
}

export class Dog extends Animal {
  constructor(name: string) {
    super(name); // must come before any use of `this`
  }

  // same signature, different body. The subclass version wins.
  speak(): string {
    return `${this.name} barks`;
  }
}

export class Widget {
  // static belongs to the class itself, shared by every instance
  static made = 0;

  constructor() {
    Widget.made++;
  }
}

// PART 7: generics

export function identity<T>(x: T): T {
  return x;
}

export function firstOrNull<T>(xs: T[]): T | null {
  return xs.length > 0 ? xs[0] : null;
}

// K extends keyof T constrains the key to one that really exists on T, so a
// typo is a compile error. T[K][] is "the type of that property, arrayed".
export function pluck<T, K extends keyof T>(items: T[], key: K): T[K][] {
  return items.map((item) => item[key]);
}
