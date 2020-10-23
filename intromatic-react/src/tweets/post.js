import React from "react";
import {handlePostForm } from "./lookup";

const PostTweet = (props) => {
  const {setNewTweets} = props
  const textAreaRef = React.createRef();
  const postErrorRef = React.createRef();
  const handleSubmit = (event) => {
    event.preventDefault();
    const post = textAreaRef.current;
    handlePostForm(post.value, (response, status) => {
      if (status === 201) {
        postErrorRef.current.className = "d-display alert alert-success";
        postErrorRef.current.textContent = "Tweet Posted!";
        console.log("enters 201")
        setNewTweets(true)
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
            type="text"
            required={true}
            className="col-12"
            id="postContent"
            name="content"
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
    </>
  );
};

export { PostTweet };
