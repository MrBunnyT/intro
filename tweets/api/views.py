from django.shortcuts import render, redirect
from django.conf import settings
from django.http import JsonResponse
from tweets.models import Tweet
from django.views.decorators import vary
from .serializers import (
    TweetCreateSerializer,
    TweetActionSerializer,
    TweetSerializer 
)
from rest_framework.response import Response
from rest_framework.decorators import (
    api_view,
    permission_classes,
    authentication_classes,
)
from rest_framework.permissions import IsAuthenticated

@api_view(["GET"])
def Tweet_Detail_View(request, tweet_id, *args, **kwargs):
    try:
        tweet = Tweet.objects.get(id=tweet_id)
    except:
        tweet = False
    if not tweet:
        return Response({"errors": "Tweet Not Found"}, status=404)
    serialized_tweet = TweetSerializer(tweet)
    return Response(serialized_tweet.data, status=200)

@api_view(["GET","POST"])
@vary.vary_on_headers("X-Requested-With")
def Tweet_List_View(request,*args,**kwargs):
    if request.method=='POST':
        is_ajax = request.META.get("HTTP_X_REQUESTED_WITH") == "XMLHttpRequest"
        created_tweet = TweetCreateSerializer(data=request.data)
        if created_tweet.is_valid(raise_exception=True):
            if is_ajax:
                created_tweet.save(user=request.user)
            return Response(created_tweet.data, status=201)
        return Response({}, status=400)
    if request.method=='GET':
        Tweets = Tweet.objects.all()
        username = request.GET.get('username')
        Tweet_Count = request.GET.get('tweetCount')
        if username!=None:
            Tweets = Tweets.filter(user__username__exact=username)
        if Tweet_Count:
            DBcount = Tweets.count()
            Tweet_Count = int(Tweet_Count)
            Tweets =Tweets[:DBcount-Tweet_Count]
        response = TweetSerializer(Tweets,many=True).data
        return Response(response,status=200)

@permission_classes([IsAuthenticated])
@api_view(["DELETE"])
def Tweet_Delete_View(request, *args, **kwargs):
    tweet_id = request.GET.get('id')
    tweets = Tweet.objects.filter(id=tweet_id)
    if not tweets.exists():
        return Response({"errors": "No Tweets found to delete"}, status=404)
    tweet = tweets.filter(user=request.user)
    if not tweet.exists():
        return Response(
            {"errors": "You are not authorized to delete this tweet"}, status=401
        )
    obj = tweet.first()
    obj.delete()
    return Response({"message": "The Tweet was deleted!!"}, status=200)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def Tweet_Action_View(request, *args, **kwargs):
    serialized_action = TweetActionSerializer(data=request.data)
    if serialized_action.is_valid(raise_exception=True):
        action_data = serialized_action.validated_data
        tweet_id = action_data.get("id")
        action = action_data.get("action")
        content = action_data.get('content')
        tweets = Tweet.objects.filter(id=tweet_id)
        if not tweets.exists():
            return Response({"errors", "No Such Tweet Found"}, status=404)
        tweet = tweets.first()
        if action == "upvote":
            tweet.likes.add(request.user)
            serialized_tweet = TweetSerializer(tweet)
            return Response(serialized_tweet.data, status=200)
        if action == "downvote":
            tweet.likes.remove(request.user)
            serialized_tweet = TweetSerializer(tweet)
            return Response(serialized_tweet.data, status=200)
        if action == "retweet":
            retweet = Tweet.objects.create(
                parent=tweet, user=request.user, content=content
            )
            serialized_retweet = TweetSerializer(retweet)
            if serialized_retweet.is_valid:
                return Response(serialized_retweet.data, status=201)
    return Response({"message": "---"}, status=200)


""" 
deprecated views below this line
-----------
-----------
-----------
----------
"""
