export function add(a: number, b: number): number {
  return a + b;
}

// A default value makes the parameter optional automatically, so you do not
// write both `?` and `= "Hello"`. Pick one. The default is usually nicer
// because the body never has to handle undefined.
export function greet(name: string, greeting: string = "Hello"): string {
  return `${greeting}, ${name}!`;
}

// typeof narrowing: inside the if, TypeScript knows `value` is a number, so
// you get number methods with no cast. This is why unions beat `any`.
export function describe(value: string | number): string {
  if (typeof value === "number") return `number: ${value}`;
  return `string: ${value}`;
}

// A rest parameter collects the remaining arguments into a real array.
export function total(...nums: number[]): number {
  return nums.reduce((sum, n) => sum + n, 0);
}
