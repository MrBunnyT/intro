from django import forms
from .models import Tweet
from django.core.validators import MaxLengthValidator
from django.conf import settings

MAX_TWEET_LENGTH = settings.MAX_TWEET_LENGTH
MIN_TWEET_LENGTH = settings.MIN_TWEET_LENGTH

class PostTweet(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['content', 'image']

    def clean_content(self):
        content = self.cleaned_data.get('content')
        if len(content) > MAX_TWEET_LENGTH or len(content) < MIN_TWEET_LENGTH or content== None:
            raise forms.ValidationError(f'Post must Be Shorter Than {MAX_TWEET_LENGTH} characters and Longer than {MIN_TWEET_LENGTH} characters')
        return content