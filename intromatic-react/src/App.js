import React from "react";
import "bootstrap/dist/css/bootstrap.css";
import { TweetComponents } from "./tweets";

function App() {
  return (
    <div className="App">
      <div className="col-12 col-md-8 mx-auto">
        <TweetComponents />
      </div>
    </div>
  );
}

export default App;
