// UTILS
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

function AJAXLookup(method, endpoint, call, data) {
  let jsondata;
  if (data) {
    jsondata = JSON.stringify(data);
  }
  const url = `http://127.0.0.1:8000${endpoint}`;
  var req = new XMLHttpRequest();
  req.open(method, url);
  req.responseType = "json";
  if (method === "POST") {
    const csrftoken = getCookie("csrftoken");
    req.setRequestHeader("content-type", "application/json");
    req.setRequestHeader("x-csrftoken", csrftoken);
    req.setRequestHeader("X-Requested-With", "XMLHttpRequest");
    req.send(jsondata);
  } else {
    req.send();
  }
  req.onload = function () {
    call(this.response, this.status);
  };
}

export { AJAXLookup };
