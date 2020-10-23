import React, { useState } from "react";
import "./components.css";
import { DetailTweet } from "./detail";
import { PostTweet } from "./post";
import { TweetsList } from "./list";

const TweetComponents = (props) => {
  console.log(props)
  const canTweet = props.canTweet === "True" ? true : false;
  const [newTweets, setNewTweets] = useState(true);
  return (
    <>
      {canTweet && <PostTweet {...props} setNewTweets={setNewTweets} />}
      <div id="tweets-container">
        <TweetsList
          newTweets={newTweets}
          setNewTweets={setNewTweets}
          canTweet={canTweet}
          {...props}
        />
        </div>
        <div id="detail-tweet-container" className="d-none">
          <DetailTweet
            tweetId={tweetId}
            canTweet={canTweet}
            UpdateRequired={newTweets}
          />
        </div>
    </>
  );
};

export {TweetComponents}