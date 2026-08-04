/**
 * PROBLEM : useEffect and Cleanup
 * TOPIC   : side effects, intervals, unmount cleanup
 * LEVEL   : Medium
 *
 * A ticker that counts seconds while it is running.
 *
 * REQUIRED data-testid values:
 *   seconds  - text showing the elapsed seconds, starting at 0
 *   toggle   - button, starts or stops the ticking
 *
 * Rules:
 *   - It starts STOPPED. Nothing ticks until toggle is clicked.
 *   - While running, `seconds` goes up by 1 every 1000ms.
 *   - Clicking toggle again stops it and the number holds.
 *   - The interval MUST be cleared when the component unmounts and whenever
 *     it stops. A leaked interval is the classic useEffect bug and the test
 *     checks for it.
 *
 * Hint (only peek if you are stuck):
 *   useEffect(() => {
 *     if (!running) return;
 *     const id = setInterval(() => setSeconds((s) => s + 1), 1000);
 *     return () => clearInterval(id);     // <- the cleanup function
 *   }, [running]);
 *
 *   Use the callback form setSeconds((s) => s + 1). Writing
 *   setSeconds(seconds + 1) captures a stale value and sticks at 1.
 *
 * HOW TO RUN:  npx vitest run problems/react/06_effect
 */
import { useEffect, useState } from "react";

export default function Clock() {
  // YOUR CODE HERE
  return <div>replace me</div>;
}
