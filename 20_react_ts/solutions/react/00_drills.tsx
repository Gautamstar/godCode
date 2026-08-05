import { useState } from "react";

// PART 1: JSX

export function Hello() {
  return <p>Hello</p>;
}

export function Greeting() {
  const name = "Gautam";
  // {name} evaluates the variable. Without braces it is literal text.
  return <p>{name}</p>;
}

export function Total() {
  const a = 2;
  const b = 3;
  return <p>{a + b}</p>;
}

export function Loud() {
  // className, not class
  return <p className="big">Loud</p>;
}

export function Styled() {
  const cls = "warning";
  // braces in an attribute read the variable; quotes would be a literal string
  return <p className={cls}>text</p>;
}

export function Pair() {
  // a fragment groups siblings without adding an element to the page
  return (
    <>
      <p>one</p>
      <p>two</p>
    </>
  );
}

// PART 2: props

export function Echo({ text }: { text: string }) {
  return <p>{text}</p>;
}

export function Score({ count }: { count: number }) {
  return <p>{count}</p>;
}

export function Welcome({ name }: { name: string }) {
  return <p>Hi, {name}!</p>;
}

// PART 3: conditionals

export function Switch({ isOn }: { isOn: boolean }) {
  // two returns is perfectly good React, and often the clearest option
  if (isOn) return <p>ON</p>;
  return <p>OFF</p>;
}

export function SwitchTernary({ isOn }: { isOn: boolean }) {
  return <p>{isOn ? "ON" : "OFF"}</p>;
}

export function MaybeError({ hasError }: { hasError: boolean }) {
  // false renders as nothing, so && is the "show only when" pattern
  return <>{hasError && <p>Error!</p>}</>;
}

export function ItemsBadge({ count }: { count: number }) {
  // count > 0, never bare count. {0 && ...} evaluates to 0 and React prints it.
  return <>{count > 0 && <p>Has items</p>}</>;
}

// PART 4: lists

export function WordList({ words }: { words: string[] }) {
  return (
    <ul>
      {words.map((w) => (
        <li key={w}>{w}</li>
      ))}
    </ul>
  );
}

export function UserList({ users }: { users: { id: number; name: string }[] }) {
  return (
    <ul>
      {users.map((u) => (
        <li key={u.id}>{u.name}</li>
      ))}
    </ul>
  );
}

export function LongWords({ words }: { words: string[] }) {
  return (
    <ul>
      {words
        .filter((w) => w.length > 3)
        .map((w) => (
          <li key={w}>{w}</li>
        ))}
    </ul>
  );
}

// PART 5: events

export function GoButton({ onGo }: { onGo: () => void }) {
  // no parentheses: pass the function, do not call it
  return <button onClick={onGo}>Go</button>;
}

export function DeleteButton({
  id,
  onDelete,
}: {
  id: number;
  onDelete: (id: number) => void;
}) {
  // the arrow delays the call until the click actually happens
  return <button onClick={() => onDelete(id)}>Delete</button>;
}

// PART 6: state

export function ShowState() {
  const [value] = useState(7);
  return <p>{value}</p>;
}

export function Clicker() {
  const [count, setCount] = useState(0);
  return (
    <div>
      <p>{count}</p>
      <button onClick={() => setCount(count + 1)}>add</button>
    </div>
  );
}

export function DoubleClicker() {
  const [count, setCount] = useState(0);
  return (
    <div>
      <p>{count}</p>
      <button
        onClick={() => {
          // the callback form reads the freshest value each time, so these
          // stack. setCount(count + 1) twice would both compute the same
          // number and add only 1.
          setCount((c) => c + 1);
          setCount((c) => c + 1);
        }}
      >
        add 2
      </button>
    </div>
  );
}

export function TextMirror() {
  const [text, setText] = useState("");
  return (
    <div>
      {/* both halves required: value makes React the source of truth,
          onChange lets typing update it */}
      <input value={text} onChange={(e) => setText(e.target.value)} />
      <p>{text}</p>
    </div>
  );
}

export function Toggle() {
  const [on, setOn] = useState(false);
  return (
    <div>
      <p>{on ? "on" : "off"}</p>
      <button onClick={() => setOn((o) => !o)}>toggle</button>
    </div>
  );
}
