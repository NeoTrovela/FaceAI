import React from "react";
import Navbar from "./Navbar";

function App() {
  return <Navbar></Navbar>;
}

export default App;
//have to link where we want the data to go to here.
<form className="new-info-form">
  <div className="form-row">
    <label htmlfor="fname">First Name </label>
    <input type="text" id="fname" name="fname"></input>
    <br></br>
    <label htmlfor="lname">Last Name </label>
    <input type="text" id="lname" name="lname"></input>
    <br></br>
    <input type="submit" value="Submit"></input>
  </div>
</form>;
