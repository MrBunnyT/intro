import React from "react";
import "bootstrap/dist/css/bootstrap.css";
import {TweetsList} from './tweets'

function App() {

  return (
    <div className="App">
      <h1 className="alert-danger col-10 mx-auto">This is check for bootstrap</h1>
      <div className="col-10 mx-auto">
        <ul className="bg-grey">
          <TweetsList />
        </ul>
      </div>
    </div>
  );
}

export default App;
