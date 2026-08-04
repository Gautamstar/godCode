import { useState } from "react";

interface CounterProps {
  start: number;
}

export default function Counter({ start }: CounterProps) {
  const [count, setCount] = useState(start);

  return (
    <div>
      <span data-testid="value">{count}</span>
      {/* The callback form setCount((c) => c + 1) reads the freshest value.
          setCount(count + 1) twice in a row would only add 1, because both
          calls close over the same stale `count`. */}
      <button data-testid="inc" onClick={() => setCount((c) => c + 1)}>
        +
      </button>
      <button data-testid="dec" onClick={() => setCount((c) => c - 1)}>
        -
      </button>
      {/* onClick wants a FUNCTION. onClick={setCount(start)} would call it
          during render and loop forever. */}
      <button data-testid="reset" onClick={() => setCount(start)}>
        reset
      </button>
    </div>
  );
}
