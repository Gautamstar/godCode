export function identity<T>(x: T): T {
  return x;
}

export function firstOrNull<T>(xs: T[]): T | null {
  return xs.length > 0 ? xs[0] : null;
}

// K extends keyof T constrains the key to one that really exists on T.
// pluck(users, "nmae") is then a compile error, not an array of undefined.
// The return type T[K][] is an "indexed access type": the type of that
// property, arrayed.
export function pluck<T, K extends keyof T>(items: T[], key: K): T[K][] {
  return items.map((item) => item[key]);
}

export function groupBy<T>(
  items: T[],
  keyOf: (item: T) => string
): Record<string, T[]> {
  const out: Record<string, T[]> = {};
  for (const item of items) {
    const key = keyOf(item);
    // create the bucket on first sighting, same shape as Python's
    // dict.setdefault or defaultdict(list)
    if (!out[key]) out[key] = [];
    out[key].push(item);
  }
  return out;
}
