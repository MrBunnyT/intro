import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import * as serviceWorker from './serviceWorker';
import App from './App';
import {TweetComponents} from './tweets'
import "bootstrap/dist/css/bootstrap.css";

const e = React.createElement

const Main_App = document.getElementById('Main_App')
if(Main_App){
ReactDOM.render(
  <App />,Main_App
);
}

const Main_Tweets = document.getElementById('Main_Tweets')
if(Main_Tweets){
  ReactDOM.render(
    <div className="mx-auto">{e(TweetComponents,Main_Tweets.dataset)}</div>,Main_Tweets)
}

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
serviceWorker.unregister();
