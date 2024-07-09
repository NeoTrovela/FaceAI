import React from "react";
import Navbar from "./Navbar";
import Upload from "./Upload";
import YourPics from "./YourPics";
import Friends from "./Friends";
import Login from "./Login";
import Profile from "./Profile";
import Settings from "./Settings";
import Home from "./home";

function App() {
  let Component;
  console.log(window.location);
  switch (window.location.pathname) {
    case "/":
      Component = Home;
      break;
    case "/Upload-Pictures":
      Component = Upload;
      break;
    case "/Your-Pictures":
      Component = YourPics;
      break;
    case "/Friends":
      Component = Friends;
      break;
    case "/Sign-Up-Login":
      Component = Login;
      break;
    case "/Profile":
      Component = Profile;
      break;
    case "/Settings":
      Component = Settings;
      break;
    default:
      Component = () => <div>404 Not Found</div>;
  }
  return (
    <>
      <Navbar />;
      <div className="container">
        <Component />
      </div>
    </>
  );
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
