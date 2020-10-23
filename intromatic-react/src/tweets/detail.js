import React,{useState,useEffect} from "react";
import { Tweet } from "./tweet";
import { handleDetail } from "./lookup";

const DetailTweet=(props)=>{
  const {tweetId,canTweet}=props
  const [detailTweet,setDetailTweet] = useState(<h1 className='mx-auto'>loading...</h1>)
  useEffect(() => {
    handleDetail(tweetId, (response, status) => {
      if (status === 200) {
        const loadedDetailTweet = <Tweet tweet={response} canTweet={canTweet}/>
        setDetailTweet(loadedDetailTweet)
      }
      else{
        const errorLoadedDetailTweet = <h1 className='alert alert-danger mx-auto'>Sorry we couldn't find that Tweet</h1>
        setDetailTweet(errorLoadedDetailTweet)
      }
    });
  }, [tweetId,canTweet])
  return detailTweet
}

export { DetailTweet };
