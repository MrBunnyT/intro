import {AJAXLookup} from '../lookpups'

function handlePostForm(newTweet, call) {
    AJAXLookup("POST", "/api/tweets/list/", call, { content: newTweet });
}

function handleAction(data, call) {
    AJAXLookup("POST", "/api/tweets/action/", call, data);
}

function handleDetail(id,call){
    AJAXLookup("GET",`/api/tweets/${id}/`,call)
}

function handleUpdate(username,tweetCount,call){
    let endPoint = `/api/tweets/list/`
    if(username){
        endPoint += `?username=${username}`
        if(tweetCount){
            endPoint += `&tweetCount=${tweetCount}`
        }
    }
    // dev-start
    else if(tweetCount){
        endPoint += `?tweetCount=${tweetCount}`
    }
    // dev-end
    AJAXLookup("GET",endPoint,call)
}

export {handleAction,handlePostForm,handleDetail,handleUpdate}