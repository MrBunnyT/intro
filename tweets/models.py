from django.db import models

class Tweet(models.Model):
    content  = models.TextField(max_length=2500,blank=True,null=True)
    image = models.FileField(upload_to='images/',blank=True,null=True)
    likes = models.BigIntegerField(default=0,blank=True,null=True)
