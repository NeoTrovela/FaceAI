import React from "react";
import "./Login.css"; // Import your CSS file for styling

function Login() {
  return (
    <div>
      <h1>Sign Up / Login</h1>
      <form action="">
        <div>
          <label htmlFor="username">Username</label>
          <br></br>
          <input type="username" placeholder="Enter Username" />
          <br></br>
          <label htmlFor="password">Password</label>
          <br></br>
          <input type="password" placeholder="Enter Password" />
          <br></br>
          <button>Login / Sign Up</button>
          <br></br>
        </div>
      </form>
    </div>
  );
}

export default Login;
