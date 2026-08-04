/**
 * PLAYGROUND
 *
 * The tests grade your code, but you should also SEE it running. Uncomment
 * whichever problem you are working on, then:  npm run dev
 *
 * Only one uncommented at a time.
 */
import Counter from "../problems/react/01_counter";
// import ItemList from "../problems/react/02_list";
// import SignupForm from "../problems/react/03_form";
// import TodoList from "../problems/react/04_todo";
// import SearchableList from "../problems/react/05_search";
// import Clock from "../problems/react/06_effect";
// import Nav from "../problems/react/07_router";

export default function App() {
  return (
    <main>
      <h1>godCode playground</h1>

      <Counter start={0} />

      {/* <ItemList items={["apple", "banana", "cherry"]} /> */}
      {/* <SignupForm /> */}
      {/* <TodoList /> */}
      {/* <SearchableList items={["apple", "banana", "cherry", "grape"]} /> */}
      {/* <Clock /> */}
      {/* <Nav /> */}
    </main>
  );
}
