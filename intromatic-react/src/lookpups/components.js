

function loadTweets(call) {
    var req = new XMLHttpRequest();
    const method = "GET";
    const url = "http://127.0.0.1:8000/api/tweets/list/tweets/";
    const responseType = "json";
    req.responseType = responseType;
    req.open(method, url);
    req.send();
    req.onload = function () {
      call(this.response, this.status);
    };
  }

export {loadTweets}