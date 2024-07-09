import React from "react";
import ReactDOM from "react-dom/client";
import App from "./App";
import "./styles.css";

const root = ReactDOM.createRoot(document.getElementById("root"));

// Initial render: Render the app using the root's render method.
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
