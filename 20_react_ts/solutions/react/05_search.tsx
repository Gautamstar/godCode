import { useState } from "react";

interface SearchableListProps {
  items: string[];
}

export default function SearchableList({ items }: SearchableListProps) {
  // ONE piece of state. The filtered list is computed, never stored.
  const [query, setQuery] = useState("");

  const q = query.toLowerCase();
  // includes() = "contains anywhere". startsWith() would fail the "rry" test.
  const visible = items.filter((item) => item.toLowerCase().includes(q));

  return (
    <div>
      <input
        data-testid="search"
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        placeholder="search"
      />

      <p data-testid="count">{visible.length}</p>

      {visible.length === 0 ? (
        <p data-testid="noresults">No matches</p>
      ) : (
        <ul>
          {visible.map((item) => (
            <li key={item} data-testid="item">
              {item}
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}

/*
 * WHY NOT STORE THE FILTERED LIST
 *
 * The tempting version:
 *
 *   const [visible, setVisible] = useState(items);
 *   onChange={(e) => { setQuery(e.target.value); setVisible(items.filter(...)); }}
 *
 * It looks fine and passes a click-through by hand. It breaks the moment the
 * `items` prop changes, because nothing recomputes `visible`. You now hold two
 * sources of truth that can disagree. Derive during render and the bug cannot
 * exist.
 */
