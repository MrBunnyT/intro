from rest_framework import serializers
from .models import Tweet
from django.conf import settings
from django.contrib.auth import get_user_model
from django.utils import timezone
import datetime

MAX_TWEET_LENGTH = settings.MAX_TWEET_LENGTH
MIN_TWEET_LENGTH = settings.MIN_TWEET_LENGTH
TWEET_ACTIONS = settings.TWEET_ACTIONS
USER = get_user_model()


class TweetCreateSerializer(serializers.ModelSerializer):
    """
    for Serializing the tweets except likes which is according to the likes count
    """

    likes = serializers.SerializerMethodField(read_only=True)
    user = serializers.SerializerMethodField(read_only=True)
    datetime = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Tweet
        fields = ["content", "id", "likes", "user", "datetime"]

    def get_likes(self, obj):
        return obj.likes.count()

    def validate_content(self, value):
        if (
            len(value) > MAX_TWEET_LENGTH
            or len(value) < MIN_TWEET_LENGTH
            or value == None
        ):
            raise serializers.ValidationError(
                f"Post must Be Shorter Than {MAX_TWEET_LENGTH} characters and Longer than {MIN_TWEET_LENGTH} characters"
            )
        return value

    def get_user(self, obj):
        return obj.user.get_username()

    def get_datetime(self, obj):
        now = timezone.now()
        timestamp = obj.timestamp
        if now.date() != timestamp.date():
            return timestamp.date()
        current_time = now.replace(microsecond=0)
        tweet_time = timestamp.replace(microsecond=0)
        difference_time = current_time - tweet_time
        return (datetime.datetime.min + difference_time).time()


class TweetActionSerializer(serializers.Serializer):
    """
    for serializing the tweet actions
    """

    id = serializers.IntegerField()
    action = serializers.CharField()
    content = serializers.CharField(allow_blank=True, required=False)

    def validate_action(self, value):
        action = value.lower().strip()
        if not action in TWEET_ACTIONS:
            raise serializers.ValidationError("This is not a valid action for Tweet")
        return value


class TweetSerializer(serializers.ModelSerializer):
    """
    for Serializing the tweets except likes which is according to the likes count
    NOTE:this is a serializer which is read-only and for purpose other than creating a post
    """

    likes = serializers.SerializerMethodField(read_only=True)
    parent_tweet = TweetCreateSerializer(source="parent", read_only=True)
    user = serializers.SerializerMethodField(read_only=True)
    datetime = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Tweet
        fields = [
            "content",
            "user",
            "id",
            "likes",
            "is_retweet",
            "parent_tweet",
            "datetime",
        ]

    def get_likes(self, obj):
        return obj.likes.count()

    def get_user(self, obj):
        return obj.user.get_username()

    def get_datetime(self, obj):
        now = timezone.now()
        timestamp = obj.timestamp
        if now.date() != timestamp.date():
            return timestamp.date()
        current_time = now.replace(microsecond=0)
        tweet_time = timestamp.replace(microsecond=0)
        difference_time = current_time - tweet_time
        return (datetime.datetime.min + difference_time).time()
