import React, { useState, useEffect } from "react";
import { handleUpdate } from "./lookup";
import { Tweet } from "./tweet";

function UpdaterCaller(setTweets, tweets, setNewTweets, username) {
  const TweetCount = tweets.length;
  username = username ? username : null;
  const Updater = (response, status) => {
    if (status === 200) {
      const newUpdate = [...response, ...tweets];
      setTweets(newUpdate);
      setNewTweets(false);
    } else {
      alert(`Something went wrong STATUS:\n[Server ERROR:${status}]`);
    }
  };
  handleUpdate(username, TweetCount, Updater);
}

const TweetsList = (props) => {
  const { username, newTweets, setNewTweets,canTweet } = props;
  const [tweets, setTweets] = useState([]);

  useEffect(() => {
    if (newTweets === true) {
      console.log("newTweets", newTweets);
      UpdaterCaller(setTweets, tweets, setNewTweets, username);
    }
    //eslint-disable-next-line
  }, [newTweets, username, setNewTweets]);
  return tweets.map((item, index) => {
    return (
      <Tweet
        tweet={item}
        key={`${index}-${item.id}`}
        UpdateRequired={setNewTweets}
        canTweet={canTweet}
      />
    );
  });
};

export { TweetsList };
