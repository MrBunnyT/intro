import React, { useState, useEffect } from "react";
import { loadTweets, handlePostForm, handleAction } from "../lookpups";
import "./components.css";

const TweetComponents = (props) => {
  return (
    <div className="tweets-container">
      <PostTweet />
    </div>
  );
};

const PostTweet = (props) => {
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
  function handlenewTweet(response){
    let temp;
    temp=[response,...tweets]
    setTweets(temp)
  }
  const textAreaRef = React.createRef();
  const postErrorRef = React.createRef();
  const handleSubmit = (event) => {
    event.preventDefault();
    const post = textAreaRef.current;
    handlePostForm(post.value, (response, status) => {
      if (status === 201) {
        postErrorRef.current.className = "d-display alert alert-success";
        postErrorRef.current.textContent = "Tweet Posted!";
        handlenewTweet(response)
      } else if (status === 400) {
        postErrorRef.current.className = "d-display alert alert-danger";
        postErrorRef.current.textContent = response.content[0];
      } else {
        alert("There was an error-Try Again");
      }
    });
    post.value = "";
  };
  return (
    <>
      <div className="col-12 mx-auto col-12" id="postForm">
        <div id="postTweetError" className="d-block" ref={postErrorRef}></div>
        <form onSubmit={handleSubmit} id="postTweet">
          <textarea
            type='text'
            required={true}
            className="col-12"
            id="postContent"
            name="content"
            // onKeyPress={()=>{console.log(this.style.width)}}
            placeholder="Share Your Tweet!!"
            ref={textAreaRef}
          />
          <div>
            <button type="submit" className="btn-lg btn-success my-4">
              POST
            </button>
          </div>
        </form>
      </div>
      <TweetsList tweets={tweets} handleChange={handlenewTweet}/>
    </>
  );
};

const TweetsList = (props) => {
  return props.tweets.map((item, index) => {
    return <Tweet tweet={item} key={`${index}-${item.id}`} handleChange={props.handleChange} />;
  });
};

function ActioBtn(props) {
  const { tweet, perform, action } = props;
  const actionHandler = (id, type) => {
    const data = {
      id: id,
      action: type,
    };
    handleAction(data, (response, status) => {
      if (status === 200) {
        perform(response);
      }
      if (status === 201) {
        perform(response)
      }
    });
  };
  if (action.type === "count") {
    return <button className="btn btn-light btn-sm">{tweet.likes}</button>;
  }
  const button = (
    <button
      className="btn btn-light btn-sm"
      onClick={() => actionHandler(tweet.id, action.type)}
    >
      {action.display}
    </button>
  );
  return button;
}

const ParentTweet = (props) => {
  const { parent } = props;
  return (
    <div className="retweet row col-11 mx-auto mb-2">
      <a className="link" href="www.google.com">
        {parent.user}
      </a>
      <div className="col-12 px-2">
        <div className="p-2">{parent.content}</div>
      </div>
      <a
        href={`http://127.0.0.1:8000/api/tweets/${parent.id}`}
        className="stretched-link"
      ></a>
    </div>
  );
};

const Tweet = (props) => {
  const [tweet, setTweet] = useState(props.tweet);
  const parent = tweet.parent_tweet;
  const className = "tweet bg-light mt-3 p-1";
  const contentClass = "p-2";
  function didaction(tweet) {
    setTweet(tweet);
  }
  return (
    <>
      <div className={className}>
        <div className="Profile">
        <a className="link" href="www.google.com">
          {tweet.user}
        </a>
        </div>
        <div className="tweet-content">
          <div className={contentClass}>{tweet.content}</div>
          {parent && <ParentTweet parent={parent} />}
        </div>
        <a
            className="stretched-link"
            href={`http://127.0.0.1:8000/api/tweets/${tweet.id}/`}
          ></a>
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
          <ActioBtn
            tweet={tweet}
            perform={props.handleChange}
            action={{ type: "retweet", display: "Retweet" }}
          />
        </div>
      </div>
    </>
  );
};

export { TweetsList, PostTweet, TweetComponents };
