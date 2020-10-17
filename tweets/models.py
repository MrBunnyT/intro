from django.db import models
from django.conf import settings

USER = settings.AUTH_USER_MODEL

class TweetLikes(models.Model):
    user = models.ForeignKey(USER,on_delete=models.CASCADE)
    tweet =models.ForeignKey('Tweet',on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

class Tweet(models.Model):
    parent = models.ForeignKey('self',on_delete=models.SET_NULL,null=True)
    user = models.ForeignKey(USER,on_delete=models.SET('deleted_user'))
    content  = models.TextField(max_length=2500,blank=True,null=True)
    image = models.FileField(upload_to='images/',blank=True,null=True)
    likes = models.ManyToManyField(USER,related_name='user_tweet',blank=True,through=TweetLikes)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-id']

    @property
    def is_retweet(self):
        return self.parent!=None

    def serialize(self):
        return {
        'id':self.id,
        'content' : self.content,
        # 'image' : self.image,
        'likes' : self.likes,
        'user' : self.user,
        }