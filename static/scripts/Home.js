const tweetsContainer = document.getElementById('tweets')
window.onload = start(tweetsContainer)

function start(tweetsContainer) {
    var req = new XMLHttpRequest()
    const method = 'GET'
    const url = '/tweets'
    const responseType = 'json'

    req.responseType = responseType
    req.open(method, url)
    req.onload = function () {
        console.log(this.response)
        const serverResponse = this.response
        const listofitems = serverResponse.response
        console.log(listofitems)
        var resultTweets = ""
        var i
        for (i = 0; i < listofitems.length; i++) {
            resultTweets += formatTweet(listofitems[i])
        }
        tweetsContainer.innerHTML = resultTweets
    }
    req.send()

    function likebtn(tweet) {
        return "<button class='btn btn-primary btn-sm'>" + tweet.likes + " Likes</button>"
    }

    function formatTweet(tweet) {
        var format = "<div class='col-12 col-md-10 mx-auto border rounded py-3 mb-4 text-center'>" +
            "<div class='tweet' id='" + tweet.id + "'><p>" + tweet.content + "</p>" +
            "<div class='btn-group'>" + likebtn(tweet) + "</div></div></div>"
        return format
    }
}