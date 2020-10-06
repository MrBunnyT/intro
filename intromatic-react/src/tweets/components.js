import React, { useState, useEffect } from "react";
import { loadTweets } from "../lookpups";

const PostTweet = (props) => {
  return (
    <div className="row">
      <div className="col-md-4 mx-auto col-8">
        <div id="post-tweet-error"></div>
        <form action="/post/" method="POST" id="postTweet">
          <input type="hidden" value="/" name="forward_url" />
          <textarea
            required="required"
            class="form-control"
            name="content"
            placeholder="Your Tweet!!"
          ></textarea>
          <button type="submit" class="btn-lg btn-success my-4">
            POST
          </button>
        </form>
      </div>
    </div>
  );
};

const TweetsList = (props) => {
  const [tweets, setTweets] = useState([]);
  useEffect(() => {
    const call = (response, status) => {
      if (status === 200) {
        setTweets(response);
      } else {
        alert(`Something went wrong STATUS:${status}`);
      }
    };
    loadTweets(call);
  }, []);
  return tweets.map((item, index) => {
    return <Tweet tweet={item} key={`${index}-${item.id}`} />;
  });
};

function Likes(tweet) {
  return (
    <button className="btn btn-outline-primary btn-sm">{tweet.likes}</button>
  );
}

function ActioBtn(props) {
  const { tweet, action } = props;
  if (action.type === "upvote")
    return <button className="btn btn-primary btn-sm">{action.display}</button>;
  else if (action.type === "downvote")
    return <button className="btn btn-primary btn-sm">{action.display}</button>;
  return <button className="btn btn-primary btn-sm">{action.display}</button>;
}
const Tweet = (props) => {
  const { tweet } = props;
  const className = "mx-auto bg-light text-center my-3 p-4";
  const contentClass = "p-2";
  return (
    <div className={className}>
      <div className={contentClass}>{tweet.content}</div>
      <div className="btn-group">
        {Likes(tweet)}
        <ActioBtn tweet={tweet} action={{ type: "upvote", display: "Like!" }} />
        <ActioBtn
          tweet={tweet}
          action={{ type: "downvote", display: "Dislike" }}
        />
        <ActioBtn
          tweet={tweet}
          action={{ type: "retweet", display: "Retweet" }}
        />
      </div>
    </div>
  );
};

export { TweetsList,PostTweet };
