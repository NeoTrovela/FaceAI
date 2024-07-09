export default function Navbar() {
  return (
    <nav className="nav">
      <a href="/" className="site-title">
        FaceAI
      </a>
      <ul>
        <CustomLink href="/Upload-Pictures">Upload Pictures</CustomLink>
        <CustomLink href="/Your-Pictures">Your Pictures</CustomLink>
        <CustomLink href="/Friends">Friends</CustomLink>
        <CustomLink href="/Sign-Up-Login">Sign Up / Login</CustomLink>
        <CustomLink href="/Profile">Profile</CustomLink>
        <CustomLink href="/Settings">Settings</CustomLink>
      </ul>
    </nav>
  );
}

function CustomLink({ href, children, ...props }) {
  const path = window.location.pathname;
  return (
    <li className={path === href ? "active" : ""}>
      <a href={href}>{children}</a>
    </li>
  );
}
