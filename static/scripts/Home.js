const tweetsContainer = document.getElementById("tweets");
window.onload = loadTweets(tweetsContainer);

// utils
function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== "") {
    const cookies = document.cookie.split(";");
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      // Does this cookie string begin with the name we want?
      if (cookie.substring(0, name.length + 1) === name + "=") {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}

function handlePostError(msg, show) {
  const postErrorsContainer = document.getElementById("post-tweet-error");
  postErrorsContainer.innerHTML = msg;
  if (show === true) {
    postErrorsContainer.setAttribute("class", "d-block alert alert-danger");
  } else {
    postErrorsContainer.setAttribute("class", "d-none alert alert-danger");
  }
}

function handlePostForm(event) {
  event.preventDefault();
  const form = event.target;
  const formData = new FormData(form);
  var req = new XMLHttpRequest();
  const url = '/api/tweets/list/'
  const method = form.getAttribute("method");
  req.open(method, url);
  req.setRequestHeader("HTTP_X_REQUESTED_WITH", "XMLHttpRequest");
  req.setRequestHeader("X-Requested-With", "XMLHttpRequest");
  req.responseType = "json";
  req.send(formData);
  req.onload = function () {
    var response = this.response;
    if (this.status === 400) {
      if (response) {
        var errors = [];
        for (var key in response) {
          errors.push(response[key]);
        }
        if (errors[0]) handlePostError(errors[0], true);
        else alert("You got an error in there");
      } else {
        alert("Some Error has occured");
      }
    } else if (this.status === 201) {
      handlePostError("", false);
      var newtweet = formatTweet(response);
      var prevTweets = tweetsContainer.innerHTML;
      tweetsContainer.innerHTML = newtweet + prevTweets;
      form.reset();
    } else if (this.status === 401) {
      console.log(response);
      handlePostError(response.errors, true);
      // setTimeout(window.location.href=response.url,10000)
    } else {
      alert("A server occured with STATUS : " + this.status);
    }
  };
}

const postForm = document.getElementById("postTweet");
postForm.addEventListener("submit", handlePostForm);

function handleTweetAction(tweet_id, action) {
  const url = "/api/tweets/action/";
  const method = "POST";
  data = JSON.stringify({
    id: tweet_id,
    action: action,
  });
  const csrftoken = getCookie("csrftoken");
  const req = new XMLHttpRequest();
  req.open(method, url);
  req.setRequestHeader("HTTP_X_REQUESTED_WITH", "XMLHttpRequest");
  req.setRequestHeader("X-Requested-With", "XMLHttpRequest");
  req.setRequestHeader("x-csrftoken", csrftoken);
  req.setRequestHeader("Content-Type", "application/json");
  req.send(data);
  req.onload = function () {
        if(this.status===200){
            loadTweets(tweetsContainer)
        }      
        else if(this.status===201){
            console.log(this.response)
        }
        else{
            alert('Our Server encountered some error STATUS : '+this.status)
        }
  };
}

function likeshandler(tweet) {
  return (
    "<button class='btn btn-outline-primary btn-sm' id='" +
    tweet.id +
    "')>" +
    tweet.likes +
    "</button>"
  );
}

function retweetbtn(id) {
  return (
    "<button class='btn btn-primary btn-sm' onclick=handleTweetAction(" +
    id +
    ",'retweet')>Retweet!</button>"
  );
}

function downvotebtn(id) {
  return (
    "<button class='btn btn-primary btn-sm' onclick=handleTweetAction(" +
    id +
    ",'downvote')>Dislike</button>"
  );
}

function upvotebtn(id) {
  return (
    "<button class='btn btn-primary btn-sm' onclick=handleTweetAction(" +
    id +
    ",'upvote')>Like</button>"
  );
}

function formatTweet(tweet) {
  var format =
    "<div class='col-12 col-md-10 mx-auto border rounded py-3 mb-4 text-center'>" +
    "<div class='tweet' id='" +
    tweet.id +
    "'><p>" +
    tweet.content +
    "</p>" +
    "<div class='btn-group'>" +
    likeshandler(tweet) +
    upvotebtn(tweet.id) +
    downvotebtn(tweet.id) +
    retweetbtn(tweet.id) +
    "</div></div></div>";
  return format;
}

function loadTweets(tweetsContainer) {
  var req = new XMLHttpRequest();
  const method = "GET";
  const url = "/api/tweets/list/";
  const responseType = "json";

  req.responseType = responseType;
  req.open(method, url);
  req.send();
  req.onload = function () {
    const serverResponse = this.response;
    const listofitems = serverResponse;
    var resultTweets = "";
    var i;
    for (i = 0; i < listofitems.length; i++) {
      resultTweets += formatTweet(listofitems[i]);
    }
    tweetsContainer.innerHTML = resultTweets;
  };
}
