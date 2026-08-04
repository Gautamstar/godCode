import { Link, Route, Routes } from "react-router-dom";

export default function Nav() {
  return (
    <div>
      <nav>
        {/* <Link> instead of <a href>. An anchor triggers a full page reload,
            which throws away all React state. */}
        <Link data-testid="link-home" to="/">
          Home
        </Link>{" "}
        <Link data-testid="link-about" to="/about">
          About
        </Link>
      </nav>

      <Routes>
        <Route path="/" element={<p data-testid="page">Home</p>} />
        <Route path="/about" element={<p data-testid="page">About</p>} />
        {/* "*" is the catch-all and must be present or an unknown URL renders
            nothing at all, silently. */}
        <Route path="*" element={<p data-testid="page">Not Found</p>} />
      </Routes>
    </div>
  );
}
