import React from "react";
import "./Login.css"; // Import your CSS file for styling

function Login() {
  return (
    <div>
      <h1>Sign Up / Login</h1>
      <form action="/action_page.php" method="post">
        <div className="imgcontainer">
          <img
            src={process.env.PUBLIC_URL + "/LOGO.png"}
            alt="Avatar"
            className="avatar"
          />
        </div>

        <div className="container">
          <label htmlFor="uname">
            <b>Username</b>
          </label>
          <input
            type="text"
            placeholder="Enter Username"
            name="uname"
            required
          />

          <label htmlFor="psw">
            <b>Password</b>
          </label>
          <input
            type="password"
            placeholder="Enter Password"
            name="psw"
            required
          />

          <button type="submit">Login</button>
          <label>
            <input type="checkbox" defaultChecked name="remember" /> Remember me
          </label>
        </div>

        <div className="container">
          <button type="button" className="cancelbtn">
            Cancel
          </button>
          <span className="SignUp">
            <a href="#">Sign Up</a>
          </span>
          <span className="psw">
            <a href="#">Forgot password?</a>
          </span>
        </div>
      </form>
    </div>
  );
}

export default Login;
