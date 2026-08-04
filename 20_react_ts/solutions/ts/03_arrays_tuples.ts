export function firstAndLast(nums: number[]): [number, number] {
  // The annotation matters. Without `: [number, number]` TypeScript infers
  // number[] and callers lose the fixed-length guarantee.
  return [nums[0], nums[nums.length - 1]];
}

export function swap(pair: [string, number]): [number, string] {
  const [label, value] = pair;
  return [value, label];
}

export interface Name {
  first: string;
  last: string;
}

// Destructuring in the signature: the parameter is still one object, you just
// name its pieces up front.
export function fullName({ first, last }: Name): string {
  return `${first} ${last}`;
}

export function topThree(nums: number[]): number[] {
  // sort() sorts IN PLACE and would mutate the caller's array, so spread into
  // a copy first. This bites people constantly.
  // It also sorts lexicographically by default, hence the comparator:
  // [1, 10, 2].sort() gives [1, 10, 2].
  return [...nums].sort((a, b) => b - a).slice(0, 3);
}
