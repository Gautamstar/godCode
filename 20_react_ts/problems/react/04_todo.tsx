/**
 * PROBLEM : To-do List
 * TOPIC   : state as an array, immutable updates, child callbacks
 * LEVEL   : Medium
 *
 * The classic. Add, toggle done, delete.
 *
 * REQUIRED data-testid values:
 *   input   - the text box for a new todo
 *   add     - button that adds the current text as a new todo
 *   todo    - EVERY todo row
 *   text    - the label inside a row (tests read textContent)
 *   toggle  - button inside a row, flips done
 *   delete  - button inside a row, removes it
 *   remaining - text showing how many are NOT done
 *
 * Rules:
 *   - Adding clears the input.
 *   - Adding empty or whitespace-only text does nothing.
 *   - A done todo's `text` element must have className "done".
 *
 * Hint (only peek if you are stuck):
 *   NEVER mutate. todos.push(x) does nothing visible.
 *     add:    setTodos([...todos, newTodo])
 *     delete: setTodos(todos.filter((t) => t.id !== id))
 *     toggle: setTodos(todos.map((t) => t.id === id ? { ...t, done: !t.done } : t))
 *
 * HOW TO RUN:  npx vitest run problems/react/04_todo
 */
import { useState } from "react";

interface Todo {
  id: number;
  text: string;
  done: boolean;
}

export default function TodoList() {
  // YOUR CODE HERE
  return <div>replace me</div>;
}
