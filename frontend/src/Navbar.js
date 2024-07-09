export default function Navbar() {
  return (
    <nav className="nav">
      <a href="/" className="site-title">
        FaceAI
      </a>
      <ul>
        <li>
          <a href="/Upload pictures">Upload pictures</a>
        </li>
        <li>
          <a href="/Your Pictures">Your Pictures</a>
        </li>
        <li>
          <a href="/Friends">Friends</a>
        </li>
        <li>
          <a href="/Sign Up / Login">Sign Up / Login</a>
        </li>
        <li>
          <a href="/Profile">Profile</a>
        </li>
        <li>
          <a href="/Settings">Settings</a>
        </li>
      </ul>
    </nav>
  );
}
