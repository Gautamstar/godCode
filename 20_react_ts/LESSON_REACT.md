# Module 20b: React Basics

> **Do the drills first.** If this lesson reads as a wall, that is expected. Open
> `problems/react/00_drills.tsx` instead and work down it. 23 tiny exercises, one idea each,
> most of them a single line, with the explanation sitting directly above the blank. Come
> back and read this once they are green and it will read as review rather than as new
> material.
>
> ```bash
> npx vitest problems/react/00_drills
> ```

This covers the HackerRank **React (Basic)** competency list: rendering elements, internal
state management, handling events, form validation, ES6 and JavaScript, and basic routing.

Nothing else. No context, no reducers, no custom hooks, no memoization, no Suspense, no data
fetching libraries. Those are real React skills and they are not on this test. Ignore them
for now.

---

## The one idea

**A component is a function that takes data and returns what the screen should look like.**

You never touch the DOM yourself. You change state, React re-runs your function, and it
works out the minimum set of DOM edits to match your new output.

**Picture it:** you are not a stagehand moving props around between scenes. You are a
scriptwriter who hands over a fresh description of the scene, and someone else works out
what to move.

This is why `document.getElementById(...)` and `element.innerHTML = ...` are wrong in React.
If you find yourself reaching for them, you want state instead.

---

## JSX

```tsx
function Hello({ name }: { name: string }) {
  return <p className="greeting">Hello {name}</p>;
}
```

It looks like HTML. Differences that cause real errors:

| HTML | JSX | Why |
|---|---|---|
| `class="x"` | `className="x"` | `class` is a reserved word |
| `for="x"` | `htmlFor="x"` | same |
| `onclick="f()"` | `onClick={f}` | camelCase, and a real function |
| `<br>` | `<br />` | every tag must close |

`{}` drops back into JavaScript. Anything inside is an expression, so `{a + b}` and
`{items.length}` work, but `{if (x) ...}` does not because `if` is a statement.

Returning two elements side by side needs one wrapper. Use a fragment when you do not want
an extra div:

```tsx
return (
  <>
    <p>one</p>
    <p>two</p>
  </>
);
```

---

## Props

Props are the function's arguments. They are **read only**. A component never writes to its
own props.

```tsx
interface CounterProps {
  start: number;
  label?: string;              // optional
  onDone: () => void;          // functions are just props too
}

export default function Counter({ start, label = "Count" }: CounterProps) { ... }
```

Destructuring in the signature with a default is the idiomatic form and it is exactly the
TypeScript destructuring from the other lesson.

---

## State

```tsx
const [count, setCount] = useState(0);
```

`useState` returns a pair: the current value, and a function to replace it. Calling the
setter tells React "this is stale, run my function again".

**Three rules that cover most bugs.**

**1. Never assign directly.** `count = 5` changes a local variable and nothing re-renders.
Only the setter works.

**2. Never mutate objects or arrays in state.** React compares by reference. If you hand
back the same array it assumes nothing changed, even if the contents differ.

```tsx
items.push(x);            // nothing happens on screen
setItems([...items, x]);  // correct: a new array

setItems(items.filter((i) => i.id !== id));                          // delete
setItems(items.map((i) => (i.id === id ? { ...i, done: true } : i))); // update one
```

Those three lines are the entire to-do list problem.

**3. Use the callback form when the new value depends on the old one.**

```tsx
setCount(count + 1);       // reads a possibly stale value
setCount((c) => c + 1);    // reads the freshest value
```

Calling `setCount(count + 1)` twice in a row adds 1, not 2, because both calls captured the
same `count`. Inside a `setInterval` this is worse: the value freezes at whatever it was
when the interval was created.

### Derive, do not duplicate

The most common structural mistake, and the one cert tests are built to catch:

```tsx
// WRONG: two sources of truth that drift apart
const [items, setItems] = useState(all);
const [filtered, setFiltered] = useState(all);

// RIGHT: one source of truth, the rest computed
const [query, setQuery] = useState("");
const visible = items.filter((i) => i.toLowerCase().includes(query.toLowerCase()));
```

If a value can be calculated from other state, calculate it during render. Do not store it.
It costs nothing and the two can never disagree.

---

## Events

```tsx
<button onClick={() => setCount(count + 1)}>+</button>
```

`onClick` wants a **function**, not a call. `onClick={setCount(5)}` runs during render,
which sets state, which re-renders, which runs it again. Infinite loop.

| You want | Write |
|---|---|
| call with no arguments | `onClick={handleClick}` |
| call with arguments | `onClick={() => remove(item.id)}` |
| read the event | `onChange={(e) => setText(e.target.value)}` |

---

## Controlled inputs

```tsx
<input value={text} onChange={(e) => setText(e.target.value)} />
```

The React state is the single source of truth for what is in the box. Both halves are
required:

- `value` without `onChange` makes the input read-only and React warns
- `onChange` without `value` means React never knows the current text

For a checkbox use `checked` and `e.target.checked` instead.

---

## Forms

```tsx
function handleSubmit(e: React.FormEvent) {
  e.preventDefault();
  // ...
}

<form onSubmit={handleSubmit}>
  <button type="submit" disabled={!valid}>Sign up</button>
</form>
```

`e.preventDefault()` is not optional. Without it the browser does a real form submission,
the page reloads, and every piece of state resets. It looks like your handler "did nothing".

Validation is just derived state:

```tsx
const emailOk = email.includes("@");
const valid = emailOk && password.length >= 6;
const showError = email.length > 0 && !emailOk;
```

Note `email.length > 0` in `showError`. Nobody wants a red error before they have typed
anything.

---

## Lists and the key prop

```tsx
<ul>
  {items.map((item) => (
    <li key={item.id}>{item.text}</li>
  ))}
</ul>
```

`key` is how React matches an element between renders to the one it drew last time.

Use a **stable unique id**. The array index works only if the list never reorders and items
are never removed from the middle. With index keys, deleting the first row makes React reuse
the wrong DOM node, and the classic symptom is a checkbox or input value sticking to the
wrong row.

---

## Conditional rendering

```tsx
{error && <p>{error}</p>}
{items.length === 0 ? <Empty /> : <List items={items} />}
```

**The `&&` trap with numbers:**

```tsx
{items.length && <List />}   // renders "0" on screen when the list is empty
{items.length > 0 && <List />}  // correct
```

`0` is falsy, so `&&` returns `0`, and React renders the number 0. Compare explicitly.

---

## useEffect

For side effects: timers, subscriptions, manual DOM work, data fetching.

```tsx
useEffect(() => {
  const id = setInterval(() => setSeconds((s) => s + 1), 1000);
  return () => clearInterval(id);   // cleanup
}, [running]);
```

Three parts:

- **the body** runs after render
- **the returned function** is cleanup, run before the next effect and once on unmount
- **the dependency array** decides when it re-runs

| Deps | Runs |
|---|---|
| `[]` | once, after the first render |
| `[running]` | on mount and whenever `running` changes |
| omitted | after **every** render, usually a bug |

The cleanup is not decoration. Without `clearInterval`, every toggle leaves another interval
running and the counter starts jumping by 2, then 3.

---

## Routing

```tsx
import { BrowserRouter, Link, Route, Routes } from "react-router-dom";

<BrowserRouter>          {/* ONCE, at the top of the app */}
  <Link to="/about">About</Link>
  <Routes>
    <Route path="/" element={<Home />} />
    <Route path="/about" element={<About />} />
    <Route path="*" element={<NotFound />} />
  </Routes>
</BrowserRouter>
```

Two things to get right. Use `<Link>`, not `<a href>`, or the browser does a full page load
and throws away all your state. And put `<BrowserRouter>` at the very top only. Nesting a
second router inside a component breaks navigation silently, with no error.

---

## data-testid, and why it decides your score

Automated graders cannot see your screen. They find elements by attribute:

```tsx
<button data-testid="submit">Sign up</button>
```

```tsx
expect(screen.getByTestId("submit")).toBeDisabled();
```

If the spec says `data-testid="submit"` and you write `data-testid="submitBtn"`, your
component works perfectly when you click through it by hand and scores **zero**.

**Before writing any logic, read the spec's list of test ids and put every one of them into
your JSX.** Then fill in behaviour. This single habit fails more candidates than not knowing
React does.

The problems in this module all specify their test ids at the top, for exactly this reason.

---

## The practice set

```bash
cd 20_react_ts
npm install       # once
npm run react     # run all React problems
```

One at a time:

```bash
npx vitest run problems/react/01_counter
```

Watch mode, which re-runs on save:

```bash
npm run watch
```

See it in a browser (uncomment your problem in `src/App.tsx` first):

```bash
npm run dev
```

| File | Covers | Time |
|---|---|---|
| `00_drills.tsx` | **start here.** JSX, props, conditionals, lists, events, state, one idea per drill | 60 min |
| `01_counter.tsx` | useState, props, event handlers | 15 min |
| `02_list.tsx` | .map(), key, conditional rendering | 20 min |
| `03_form.tsx` | controlled inputs, validation, preventDefault | 40 min |
| `04_todo.tsx` | array state, immutable updates, child callbacks | 45 min |
| `05_search.tsx` | derived state, the most common cert question | 30 min |
| `06_effect.tsx` | useEffect, dependencies, cleanup | 30 min |
| `07_router.tsx` | Link, Routes, catch-all | 20 min |

That is about four hours. Then do the part that actually matters: **delete your answers to
04 and 05 and write them again from an empty file, timed at 25 minutes each.** The first
pass teaches you the pattern. The rebuild is what makes it available under a clock.
