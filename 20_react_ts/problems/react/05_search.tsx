/**
 * PROBLEM : Searchable List
 * TOPIC   : derived state (the single most common React cert question)
 * LEVEL   : Medium
 *
 * A text box that filters a list as you type.
 *
 * REQUIRED data-testid values:
 *   search     - the text input
 *   item       - EVERY visible <li>
 *   count      - text showing how many items are currently visible
 *   noresults  - shown ONLY when the query matches nothing,
 *                with the text "No matches"
 *
 * Matching is case-insensitive and uses "contains", not "starts with".
 *
 * THE ONE THING TO GET RIGHT:
 *   Keep TWO pieces of state at most: the full `items` (here they arrive as a
 *   prop, so zero state) and the `query` string. Compute the filtered list
 *   during render:
 *       const visible = items.filter((i) => i.toLowerCase().includes(q));
 *   Storing a separate `filtered` state is the classic bug. It goes stale the
 *   moment either input changes, and cert tests are built to catch it.
 *
 * HOW TO RUN:  npx vitest run problems/react/05_search
 */
import { useState } from "react";

interface SearchableListProps {
  items: string[];
}

export default function SearchableList({ items }: SearchableListProps) {
  const [query, setQuery] = useState("")
  const visible = items.filter((i) => i.toLowerCase().includes(query.toLowerCase()));
  const count = visible.length
  const noResults = visible.length === 0
  return <div>
    <input data-testid="search" value={query} onChange={(e) => setQuery(e.target.value)} />
    <ul>
      {visible.map((v) => <li data-testid="item" key={v}>{v}</li>)}
    </ul>
    <p data-testid="count">{count}</p>
    {noResults && <p data-testid="noresults">No matches</p>}
  </div>;
}
