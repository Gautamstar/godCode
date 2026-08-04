/**
 * PROBLEM : Basic Routing
 * TOPIC   : react-router-dom v6
 * LEVEL   : Easy
 *
 * Two pages plus a catch-all.
 *
 * REQUIRED data-testid values:
 *   link-home   - a <Link> to "/"
 *   link-about  - a <Link> to "/about"
 *   page        - one element whose text is the current page name:
 *                   "/"        -> "Home"
 *                   "/about"   -> "About"
 *                   anything else -> "Not Found"
 *
 * IMPORTANT: do NOT put a <BrowserRouter> inside this component. The router
 * lives above it (src/main.tsx wraps the app, and the tests supply their own).
 * Nesting routers is a very common mistake and breaks navigation silently.
 *
 * Hint (only peek if you are stuck):
 *   import { Link, Route, Routes } from "react-router-dom";
 *   <Routes>
 *     <Route path="/" element={<p data-testid="page">Home</p>} />
 *     <Route path="*" element={...} />
 *   </Routes>
 *
 * HOW TO RUN:  npx vitest run problems/react/07_router
 */

export default function Nav() {
  // YOUR CODE HERE
  return <div>replace me</div>;
}
