/**
 * PROBLEM : Rendering a List
 * TOPIC   : .map(), the key prop, conditional rendering
 * LEVEL   : Easy
 *
 * Render `items` as a <ul> of <li> elements.
 *
 * REQUIRED data-testid values:
 *   list   - the <ul>
 *   item   - EVERY <li> (yes, the same testid on each; tests use getAllByTestId)
 *   empty  - shown ONLY when items is empty, with the text "No items"
 *            When the list is empty, do not render the <ul> at all.
 *   count  - always shown, the number of items as text
 *
 * Each <li> must have a `key`. React warns loudly without it.
 *
 * Hint (only peek if you are stuck):
 *   {items.length === 0 ? <p data-testid="empty">No items</p> : <ul>...</ul>}
 *
 * HOW TO RUN:  npx vitest run problems/react/02_list
 */

interface ItemListProps {
  items: string[];
}

export default function ItemList({ items }: ItemListProps) {
  // YOUR CODE HERE
  return <div>replace me</div>;
}
