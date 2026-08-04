/**
 * PROBLEM : Counter
 * TOPIC   : useState, props, event handlers
 * LEVEL   : Easy
 *
 * Build a counter that starts at `start`.
 *
 * REQUIRED data-testid values (the tests select by these, exact spelling):
 *   value  - an element showing the current count as text
 *   inc    - button, adds 1
 *   dec    - button, subtracts 1
 *   reset  - button, returns the count to `start`
 *
 * Hint (only peek if you are stuck):
 *   const [count, setCount] = useState(start);
 *   <button data-testid="inc" onClick={() => setCount((c) => c + 1)}>+</button>
 *
 * HOW TO RUN:  npx vitest run problems/react/01_counter
 * SEE IT:      npm run dev   (already wired up in src/App.tsx)
 */
import { useState } from "react";

interface CounterProps {
  start: number;
}

export default function Counter({ start }: CounterProps) {
  // YOUR CODE HERE
  return <div>replace me</div>;
}
