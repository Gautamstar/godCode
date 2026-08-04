interface ItemListProps {
  items: string[];
}

export default function ItemList({ items }: ItemListProps) {
  return (
    <div>
      <p data-testid="count">{items.length}</p>

      {items.length === 0 ? (
        <p data-testid="empty">No items</p>
      ) : (
        <ul data-testid="list">
          {items.map((item) => (
            // `key` must be stable and unique among siblings. The array index
            // works only if the list never reorders or gets items removed
            // from the middle. Here the strings are unique, so use the value.
            <li key={item} data-testid="item">
              {item}
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}
