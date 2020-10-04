from django.contrib import admin
from tweets.models import Tweet,TweetLikes

class TweetLikesAdmin(admin.TabularInline):
    model = TweetLikes

class TweetAdmin(admin.ModelAdmin):
    inlines = [TweetLikesAdmin]
    list_display = ['id','content','user']
    search_fields = ['content','user__username']
    class Meta:
        model = Tweet


admin.site.register(Tweet,TweetAdmin)
