import { useEffect, useState } from "react";

export default function Clock() {
  const [seconds, setSeconds] = useState(0);
  const [running, setRunning] = useState(false);

  useEffect(() => {
    // Bail out when stopped. No interval is created, so there is nothing to
    // clean up on this pass.
    if (!running) return;

    const id = setInterval(() => {
      // Callback form. setSeconds(seconds + 1) would capture the value from
      // the render that created this interval and stick at 1 forever.
      setSeconds((s) => s + 1);
    }, 1000);

    // The returned function is the cleanup. React runs it before the next
    // effect and once more on unmount. Without it every toggle leaks another
    // interval and the counter starts skipping.
    return () => clearInterval(id);
  }, [running]); // re-run only when `running` changes

  return (
    <div>
      <span data-testid="seconds">{seconds}</span>
      <button data-testid="toggle" onClick={() => setRunning((r) => !r)}>
        {running ? "stop" : "start"}
      </button>
    </div>
  );
}
