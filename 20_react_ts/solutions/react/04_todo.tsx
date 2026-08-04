import { useState } from "react";

interface Todo {
  id: number;
  text: string;
  done: boolean;
}

export default function TodoList() {
  const [todos, setTodos] = useState<Todo[]>([]);
  const [text, setText] = useState("");
  const [nextId, setNextId] = useState(1);

  function add() {
    const clean = text.trim();
    if (clean === "") return;
    // A NEW array. todos.push(...) mutates the existing one, React sees the
    // same reference, and nothing re-renders.
    setTodos([...todos, { id: nextId, text: clean, done: false }]);
    setNextId(nextId + 1);
    setText("");
  }

  function toggle(id: number) {
    // map returns a new array, and the matching item becomes a new object via
    // spread. Everything else keeps its identity.
    setTodos(todos.map((t) => (t.id === id ? { ...t, done: !t.done } : t)));
  }

  function remove(id: number) {
    setTodos(todos.filter((t) => t.id !== id));
  }

  const remaining = todos.filter((t) => !t.done).length;

  return (
    <div>
      <input
        data-testid="input"
        value={text}
        onChange={(e) => setText(e.target.value)}
        placeholder="new todo"
      />
      <button data-testid="add" onClick={add}>
        Add
      </button>

      <ul>
        {todos.map((t) => (
          // key is the stable id, never the array index. With index keys,
          // deleting the first row makes React reuse the wrong DOM node.
          <li key={t.id} data-testid="todo">
            <span data-testid="text" className={t.done ? "done" : ""}>
              {t.text}
            </span>
            {/* Arrow wrapper so the handler runs on click, not on render. */}
            <button data-testid="toggle" onClick={() => toggle(t.id)}>
              done
            </button>
            <button data-testid="delete" onClick={() => remove(t.id)}>
              x
            </button>
          </li>
        ))}
      </ul>

      <p data-testid="remaining">{remaining}</p>
    </div>
  );
}
