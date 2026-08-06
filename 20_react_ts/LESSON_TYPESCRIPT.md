# Module 20a: TypeScript Basics

> **Do the drills first.** `problems/ts/00_drills.ts`, 27 micro-exercises, one idea each.
> Come back and read this once they are green.
>
> ```bash
> npx vitest problems/ts/00_drills   # behaviour
> npm run typecheck                  # types
> ```
>
> Both graders matter. Types are erased before the code runs, so vitest will pass a
> function with no annotations at all. `npm run typecheck` is the only thing that grades
> the actual TypeScript.

Everything here maps to the HackerRank **TypeScript (Basic)** competency list: data types,
variable declaration and scoping, destructuring, arrays and tuples, type annotations,
interfaces and assertions, functions, classes, and inheritance.

If you know Python, most of this is familiar logic wearing types. The types are the part
being graded.

---

## The one idea

TypeScript is JavaScript plus a compiler that checks your assumptions before the code runs.
None of the types exist at runtime. They are erased. Their entire job is to make a wrong
assumption a red squiggle instead of a 2am `undefined is not a function`.

**Picture it:** JavaScript hands you an unlabelled box and you find out what is inside by
opening it. TypeScript makes you write the label first, and then complains if you try to
put a hamster in the box marked "screws".

---

## Annotations

```ts
let count: number = 0;
const name: string = "Gautam";
const tags: string[] = ["a", "b"];

function add(a: number, b: number): number {
  return a + b;
}
```

The return type after the parameter list is the part people forget. You can usually omit it
and let inference do the work, but on an assessment write it out. It documents intent and
it catches a wrong `return` inside a branch.

### const vs let

`const` means the binding cannot be reassigned. It does **not** mean the value is frozen.

```ts
const xs = [1, 2];
xs.push(3);   // fine, the array is mutated
xs = [4];     // error, the binding is reassigned
```

Prefer `const` everywhere and only reach for `let` when you genuinely reassign. Never `var`,
which is function-scoped and hoisted in ways that produce classic trick questions.

---

## Optional and default parameters

```ts
function greet(name: string, greeting?: string) {}          // greeting: string | undefined
function greet(name: string, greeting: string = "Hello") {} // greeting: string
```

The second form is usually better because the body never has to check for undefined. Note
that optional parameters must come **after** required ones.

---

## Union types and narrowing

```ts
function describe(value: string | number): string {
  if (typeof value === "number") {
    return `number: ${value}`;   // TypeScript knows it is a number in here
  }
  return `string: ${value}`;     // and a string out here
}
```

This is the mechanism that makes unions useful instead of annoying. The compiler follows
your `if` and narrows the type inside each branch. You almost never need a cast.

| Narrowing tool | Use for |
|---|---|
| `typeof x === "string"` | primitives |
| `Array.isArray(x)` | arrays |
| `x instanceof Dog` | classes |
| `"email" in user` | checking a property exists |
| `x === null` | null checks |

---

## Interfaces

An interface describes the shape of an object.

```ts
interface User {
  id: number;
  name: string;
  email?: string;      // optional: string | undefined
  readonly createdAt: string;
}
```

Optional properties are the graded detail. `u.email` is `string | undefined`, so the
compiler forces you to handle the missing case. That is the whole point of marking it.

### Index signatures

When the keys are data rather than a fixed schema:

```ts
interface Scores {
  [subject: string]: number;
}
```

This is TypeScript's version of a Python dict with a known value type. Use named properties
when you know the keys, an index signature when you do not.

### interface vs type

For object shapes they are nearly interchangeable. `interface` can be reopened and extended,
`type` can also express unions and primitives. Either is fine on an assessment.

---

## Assertions

```ts
const user = JSON.parse(json) as User;
```

An assertion tells the compiler "trust me, it is this shape". It is **not** a runtime check.
Nothing validates the JSON. If the shape is wrong you get exactly the same crash you would
get in plain JavaScript, just later.

Use it when you genuinely know the shape (a `JSON.parse` of your own API). Reach for
narrowing instead whenever you can prove the type in code.

---

## Arrays vs tuples

```ts
let xs: number[] = [1, 2, 3];          // any length, all numbers
let pair: [string, number] = ["a", 1]; // exactly 2 slots, types per position
```

A tuple is how you return two related values of different types without inventing an
interface. The annotation is load-bearing: drop it and TypeScript infers
`(string | number)[]`, which loses both the length and the per-slot type.

---

## Destructuring

```ts
const [first, second] = pair;
const { first, last } = name;

function fullName({ first, last }: Name): string {
  return `${first} ${last}`;
}
```

Destructuring in the parameter list is very common in React, so get comfortable with it
here. The object is still one argument, you are just naming its pieces up front.

### The sort trap

```ts
[1, 10, 2].sort()                 // [1, 10, 2]  sorted as STRINGS
[1, 10, 2].sort((a, b) => a - b)  // [1, 2, 10]  correct
```

`sort` also mutates in place. Spread into a copy first if the caller still needs the
original: `[...nums].sort(...)`.

---

## Classes

```ts
class Animal {
  static count = 0;

  constructor(protected name: string) {
    Animal.count++;
  }

  speak(): string {
    return `${this.name} makes a sound`;
  }

  get label(): string {
    return `Animal: ${this.name}`;
  }
}
```

Two things get tested constantly:

**Parameter properties.** Writing `constructor(protected name: string)` declares the field,
assigns it, and sets visibility in one line. Without a modifier, `name` is just an argument
that disappears when the constructor returns.

**Access modifiers.**

| Modifier | Visible in the class | In subclasses | Outside |
|---|---|---|---|
| `public` (default) | yes | yes | yes |
| `protected` | yes | yes | no |
| `private` | yes | **no** | no |

If a subclass needs the field, `private` is wrong. That distinction is the question.

A getter is accessed as `a.label`, with no parentheses. Calling `a.label()` is an error.

### Inheritance

```ts
class Dog extends Animal {
  constructor(name: string, public breed: string) {
    super(name);   // must come before any use of `this`
  }

  speak(): string {   // overrides the parent
    return `${this.name} barks`;
  }
}
```

`super(...)` first, always. Using `this` before it is a compile error.

---

## Generics

A generic is a type parameter: a type the caller fills in.

```ts
function identity<T>(x: T): T {
  return x;
}
```

Compare `function identity(x: any): any`. Both compile. The `any` version throws away what
it knew, so `identity("hi").toUpperCase()` is unchecked and `identity(7).toUpperCase()`
compiles and then crashes. The generic keeps the type flowing through.

### Constraints

```ts
function pluck<T, K extends keyof T>(items: T[], key: K): T[K][] {
  return items.map((item) => item[key]);
}
```

`keyof T` is the union of T's property names. `K extends keyof T` says the key must really
exist, so a typo is a compile error rather than an array of `undefined`. `T[K]` is the type
of that property.

---

## The practice set

```bash
cd 20_react_ts
npm install          # once
npm run ts           # run all TypeScript problems
```

Or one at a time:

```bash
npx vitest run problems/ts/01_annotations
```

| File | Covers |
|---|---|
| `00_drills.ts` | **start here.** 27 micro-exercises across all of the below |
| `01_annotations.ts` | annotations, optional and default params, unions, rest params |
| `02_interfaces.ts` | interfaces, optional properties, index signatures, assertions |
| `03_arrays_tuples.ts` | arrays, tuples, destructuring, the sort trap |
| `04_classes.ts` | parameter properties, access modifiers, getters, inheritance, statics |
| `05_generics.ts` | generic functions, constraints, indexed access types |

Write from memory. Compare with `solutions/ts/` only after a real attempt, then close it and
rewrite.
