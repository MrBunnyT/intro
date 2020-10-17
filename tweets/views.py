from django.shortcuts import render, redirect
from django.conf import settings
from django.http import HttpResponse, JsonResponse
from .models import Tweet
from .forms import PostTweet
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

# from rest_framework.authentication import SessionAuthentication


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


@api_view(["GET"])
def Tweet_List_View(request, *args, **kwargs):
    Tweets = Tweet.objects.all()
    Tweets_serialized = TweetSerializer(Tweets,many=True)
    response = Tweets_serialized.data
    return Response(response, status=200)


def HomeView(request, *args, **kwargs):
    return render(request, "Home.html", context={}, status=200)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
@vary.vary_on_headers("X-Requested-With")
def Tweet_Create_View(request, *args, **kwargs):
    is_ajax = request.META.get("HTTP_X_REQUESTED_WITH") == "XMLHttpRequest"
    created_tweet = TweetCreateSerializer(data=request.data)
    if created_tweet.is_valid(raise_exception=True):
        if is_ajax:
            created_tweet.save(user=request.user)
            return Response(created_tweet.data, status=201)
    return Response({}, status=400)


class Accounts:
    def login(request):
        return HttpResponse('login',status=200)


@permission_classes([IsAuthenticated])
@api_view(["DELETE", "POST"])
def Tweet_Delete_View(request, tweet_id, *args, **kwargs):
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


@api_view(["POST", "GET"])
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


@vary.vary_on_headers("X-Requested-With")
def Tweet_Create_View_pureDjango(request, *args, **kwargs):
    is_ajax = request.META.get("HTTP_X_REQUESTED_WITH") == "XMLHttpRequest"
    user = request.user
    if not request.user.is_authenticated:
        user = None
        if is_ajax:
            return JsonResponse(
                {"errors": "You are not logged in", "url": settings.LOGIN_URL},
                status=401,
            )
        return redirect(settings.LOGIN_URL)

    if request.method == "POST":
        form = PostTweet(request.POST)
        if is_ajax and form.is_valid():
            obj = form.save(commit=False)
            # sort form and put according to time or other logic
            obj.user = user
            obj.save()
            return JsonResponse(
                obj.serialize(), status=201
            )  # status 201 = created item in our case loaded tweets
        else:
            if is_ajax:
                return JsonResponse(form.errors, status=400)
    form = PostTweet
    context = {"form": form}
    return render(request, "Form.html", context)


@api_view(["GET"])
def ListView_pureDjango(request, *args, **kwargs):
    tweets = Tweet.objects.all()
    serialized_tweets = TweetSerializer(tweets, many=True)
    response = {
        "response": serialized_tweets.data,
    }
    return Response(response)


def Tweet_Detail_View_pureDjango(request, tweet_id, *args, **kwargs):
    """
    REST API VIEW
    Consume by Javascript or Swift/Java/iOS/Android
    return jsondata
    """
    tweets = Tweet.objects.all()
    data = {
        "id": tweet_id,
    }
    status = 200
    try:
        data["content"] = tweets.get(id=tweet_id).content
    except:
        data["message"] = "Not Found"
        status = 404
    return JsonResponse(data, status=status)
