import React, { useState } from "react";
import { ActioBtn } from "./buttons";

const ParentTweet = (props) => {
  const { parent } = props;
  return (
    <div className="retweet row col-11 mx-auto mb-2">
      <a className="link" href="www.google.com">
        {parent.user}
      </a>
      <div className="col-12 px-2">
        <div className="p-2">
          <span className="content">{parent.content}</span>
        </div>
      </div>
    </div>
  );
};

const Tweet = (props) => {
  const { UpdateRequired, canTweet } = props;
  const [tweet, setTweet] = useState(props.tweet);
  const parent = tweet.parent_tweet;
  const tweetClassName = "tweet";
  function didaction(tweet) {
    setTweet(tweet);
  }
  return (
    <>
      <div className={tweetClassName}>
        <div className="Profile">
          <a className="link" href="www.google.com">
            {tweet.user}
          </a>
        </div>
        <div className="tweet-content p-2">
          <span className="content">{tweet.content}</span>
          {parent && <ParentTweet parent={parent} />}
        </div>
        <div className="btn-group justify-content-between col-12">
          <ActioBtn
            tweet={tweet}
            perform={didaction}
            action={{ type: "count" }}
          />
          <ActioBtn
            tweet={tweet}
            perform={didaction}
            action={{ type: "upvote", display: "Like!" }}
          />
          <ActioBtn
            tweet={tweet}
            perform={didaction}
            action={{ type: "downvote", display: "Dislike" }}
          />
          {canTweet && <ActioBtn
            tweet={tweet}
            perform={UpdateRequired}
            action={{ type: "retweet", display: "Retweet" }}
          />}
        </div>
      </div>
    </>
  );
};

export { Tweet, ParentTweet };
