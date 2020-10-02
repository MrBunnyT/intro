from django import forms
from .models import Tweet
from django.core.validators import MaxLengthValidator

MAX_TWEET_LENGTH = 250
MIN_TWEET_LENGTH = 2

class PostTweet(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['content', 'image']

    def clean_content(self):
        content = self.cleaned_data.get('content')
        print(len(content),'---',content,'---')
        if len(content) > MAX_TWEET_LENGTH or len(content) < MIN_TWEET_LENGTH or content== None:
            raise forms.ValidationError(f"Post must Be Shorter Than {MAX_TWEET_LENGTH} characters and Longer than {MIN_TWEET_LENGTH} characters")
        return content
