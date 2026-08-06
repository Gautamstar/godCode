/**
 * REACT DRILLS - one idea at a time, no components to "design".
 *
 * Same spirit as 00_python_for_dsa/drills.py. Each drill adds exactly ONE new
 * thing to the one before it. Most are a single line. If a drill takes more
 * than three minutes, the explanation above it did not land, so re-read it
 * rather than guessing.
 *
 * Do these BEFORE 01_counter. The lesson makes far more sense afterwards.
 *
 * RUN:  npx vitest run problems/react/00_drills
 * WATCH (re-runs on save, best way to do these):
 *       npx vitest problems/react/00_drills
 */
import { useState } from "react";

// ---------------------------------------------------------------------------
// PART 1: JSX is just a value you return
// ---------------------------------------------------------------------------

// 1. Return a paragraph with the text: Hello
//
//    A component is a function that RETURNS what should be on screen. That
//    HTML-looking thing is JSX, and it is an ordinary value, like a number or
//    a string. You can return it, store it in a variable, put it in an array.
//
//    Write:  return <p>Hello</p>;
export function Hello() {
  return <p>Hello</p>;
}

// 2. Return a paragraph containing the value of `name` (not the word "name").
//
//    Curly braces drop you out of JSX and back into JavaScript. Whatever is
//    inside gets evaluated and its result is printed.
//
//    <p>name</p>    prints the literal text "name"
//    <p>{name}</p>  prints what the variable holds
export function Greeting() {
  const name = "Gautam";
  // YOUR CODE HERE
  return <p>{name}</p>;
}

// 3. Return a paragraph containing the SUM of a and b, as text.
//
//    Anything inside {} must be an EXPRESSION, meaning something that produces
//    a value. `a + b` works. `if (a) {...}` does not, because a statement does
//    not produce a value. This is why React uses ternaries and && later on.
export function Total() {
  const a = 2;
  const b = 3;
  // YOUR CODE HERE
  return <>{a + b}</>;
}

// 4. Return a <p> with the CSS class "big" and the text: Loud
//
//    In JSX the attribute is `className`, not `class`. `class` is a reserved
//    word in JavaScript, so React had to pick a different name.
export function Loud() {
  return <p className = "big">Loud</p>;
}

// 5. Return a <p> whose className comes from the `cls` variable.
//
//    Braces work in attributes too, not just between tags.
//    className="cls"    sets the literal class "cls"
//    className={cls}    sets whatever the variable holds
export function Styled() {
  const cls = "warning";
  // YOUR CODE HERE
  return <p className = {cls}></p>;
}

// 6. Return TWO paragraphs, "one" and "two", with no extra <div> around them.
//
//    A function returns one value, so two sibling elements need a wrapper.
//    <>...</> is a fragment: a wrapper that groups them without adding a real
//    element to the page.
export function Pair() {
  return <>
    <p>one</p>
    <p>two</p>
  </>;
}

// ---------------------------------------------------------------------------
// PART 2: props are the function's arguments
// ---------------------------------------------------------------------------

// 7. Return a <p> containing the `text` prop.
//
//    Props are how a parent passes data in. <Echo text="hi" /> calls this
//    function with { text: "hi" }. The braces in the parameter list are
//    destructuring, exactly like in TypeScript: pull `text` out of the object.
export function Echo({ text }: { text: string }) {
  // YOUR CODE HERE
  return <p>{text}</p>;
}

// 8. Return a <p> containing the `count` prop.
//
//    Numbers pass through braces: <Score count={5} />, not count="5".
//    React prints numbers fine, so no conversion is needed.
export function Score({ count }: { count: number }) {
  // YOUR CODE HERE
  return <p>{count}</p>;
}

// 9. Return a <p> containing "Hi, <name>!" using the `name` prop.
//
//    You can mix literal text and braces freely inside a tag.
//    Both of these work, pick either:
//      <p>Hi, {name}!</p>
//      <p>{`Hi, ${name}!`}</p>
export function Welcome({ name }: { name: string }) {
  // YOUR CODE HERE
  return <p>Hi, {name}!</p>;
}

// ---------------------------------------------------------------------------
// PART 3: showing things conditionally
// ---------------------------------------------------------------------------

// 10. If `isOn` is true return a <p> saying "ON", otherwise one saying "OFF".
//
//     A plain if/else with two returns is completely fine here and is often
//     the clearest thing to write. Do it that way first.
export function Switch({ isOn }: { isOn: boolean }) {
  if (isOn) { return <p>ON</p> }
  return <p>OFF</p>;
}

// 11. Same as drill 10, but do it INSIDE one <p> using a ternary.
//     Expected text is "ON" or "OFF".
//
//     A ternary is an expression, so it is allowed inside braces:
//       <p>{isOn ? "ON" : "OFF"}</p>
//     This is the standard way to choose between two things in JSX.
export function SwitchTernary({ isOn }: { isOn: boolean }) {
  // YOUR CODE HERE
  return <>
    {isOn ?
      <p>ON </p> :
      <p>OFF</p>
    }
  </>;
}

// 12. Return a <p> with the text "Error!" ONLY when `hasError` is true.
//     When it is false, render nothing at all.
//
//     `a && b` returns b when a is truthy, and a when it is falsy. React
//     renders nothing for false, null, and undefined, so this shows the
//     element only when the condition holds:
//       {hasError && <p>Error!</p>}
export function MaybeError({ hasError }: { hasError: boolean }) {
  return <>
    {hasError && <p>Error!</p>}
  </>;
}

// 13. Render <p>Has items</p> only when `count` is greater than 0.
//     When count is 0, the page must be EMPTY. No "0" on screen.
//
//     This is the trap version of drill 12. Writing {count && <p>...</p>}
//     returns 0 when count is 0, and React prints the number 0. Compare
//     explicitly instead: count > 0.
export function ItemsBadge({ count }: { count: number }) {
  // YOUR CODE HERE
  return <>
    {count > 0 && <p>Has items</p>}
  </>;
}

// ---------------------------------------------------------------------------
// PART 4: lists
// ---------------------------------------------------------------------------

// 14. Return a <ul> with one <li> per word in `words`.
//     Give each <li> a `key` prop set to the word itself.
//
//     .map() turns an array of strings into an array of JSX elements, and
//     React renders an array by rendering each element in order:
//       <ul>{words.map((w) => <li key={w}>{w}</li>)}</ul>
//
//     `key` lets React tell the items apart between renders. Without it you
//     get a console warning and, later, real bugs.
export function WordList({ words }: { words: string[] }) {
  // YOUR CODE HERE
  return <ul>
    {words.map((w) => <li key = {w}>
      {w}
    </li>)}
  </ul>;
}

// 15. Return a <ul> of <li>, one per user, showing each user's name.
//     Use the user's `id` as the key.
//
//     With objects, the key should be a stable unique id, not the name and
//     not the array position.
export function UserList({ users }: { users: { id: number; name: string }[] }) {
  return <ul>
    {
      users.map((u) => <li key={u.id}>
        {u.name}
      </li>)
    }
  </ul>;
}

// 16. Return a <ul> containing only the words LONGER than 3 characters.
//
//     Filter first, then map. Chaining them is normal and readable:
//       words.filter(...).map(...)
//     This is the whole idea behind the searchable-list problem later.
export function LongWords({ words }: { words: string[] }) {
  return <ul>
    {words.filter((wo) => wo.length > 3)
      .map((w) => <li key={w}>
        {w}
      </li>)}
  </ul>;
}

// ---------------------------------------------------------------------------
// PART 5: events
// ---------------------------------------------------------------------------

// 17. Return a <button> with the text "Go" that calls `onGo` when clicked.
//
//     onClick takes a FUNCTION, and `onGo` already is one, so pass it by name
//     with no parentheses:
//       <button onClick={onGo}>Go</button>
//     Writing onClick={onGo()} calls it immediately during render instead.
export function GoButton({ onGo }: { onGo: () => void }) {
  // YOUR CODE HERE
  return <button onClick = {onGo}>GO</button>;
}

// 18. Return a <button> "Delete" that calls onDelete(id) when clicked.
//
//     You need to pass an argument, but onClick wants a function, not a call.
//     Wrap it in an arrow so the call happens on click, not on render:
//       onClick={() => onDelete(id)}
//     This wrapper is the single most common line in React event code.
export function DeleteButton({
  id,
  onDelete,
}: {
  id: number;
  onDelete: (id: number) => void;
}) {
  return <button onClick ={()=> onDelete(id)}>Delete</button>;
}

// ---------------------------------------------------------------------------
// PART 6: state
// ---------------------------------------------------------------------------

// 19. Show the current value of a state variable that starts at 7,
//     inside a <p>.
//
//     useState(7) returns a two-slot array: the current value, and a function
//     that replaces it. Destructure it:
//       const [value, setValue] = useState(7);
//     Nothing is clickable yet. Just display it.
export function ShowState() {
  const [value, setValue] = useState(7)
  return <ul>{value}</ul>;
}

// 20. A <p> showing a count that starts at 0, and a <button> "add" that
//     increases it by 1.
//
//     THE RULE: never assign to the variable. `count = count + 1` changes a
//     local that is thrown away when the function ends, and nothing redraws.
//     Only the setter tells React to re-run your function:
//       onClick={() => setCount(count + 1)}
export function Clicker() {
  const [count, setCount] = useState(0)
  return <>
    <p>{count}</p>
    <button onClick={()=> setCount((x)=> x + 1)}>add</button>
  </>;
}

// 21. Same as drill 20, but the button must add 2 by calling the setter
//     TWICE in one click. The count goes 0, 2, 4.
//
//     setCount(count + 1) twice adds only 1, because both calls read the same
//     `count` from this render. The callback form reads the freshest value:
//       setCount((c) => c + 1);
//       setCount((c) => c + 1);
//     Use the callback form whenever the new value depends on the old one.
export function DoubleClicker() {
  // YOUR CODE HERE
  return null;
}

// 22. A text <input> whose value is state, plus a <p> showing what was typed.
//
//     A controlled input needs BOTH halves:
//       value={text}                              React owns what is shown
//       onChange={(e) => setText(e.target.value)}  typing updates React
//
//     `e` is the event, `e.target` is the input element, `e.target.value` is
//     its current text. With only `value`, the box is frozen. With only
//     `onChange`, React never re-renders and the box looks frozen too.
export function TextMirror() {
  // YOUR CODE HERE
  return null;
}

// 23. A <button> "toggle" and a <p> showing "on" or "off".
//     It starts off. Each click flips it.
//
//     Boolean state plus the callback form:
//       setOn((o) => !o)
//     Everything you just learned, combined: state, event, ternary.
export function Toggle() {
  // YOUR CODE HERE
  return null;
}
