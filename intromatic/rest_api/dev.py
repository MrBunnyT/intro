from rest_framework import authentication
from django.contrib.auth import get_user_model

USER = get_user_model()

class DevAuth(authentication.BasicAuthentication):
    def authenticate(self,request):
        query = USER.objects.all()
        user = query.order_by('-id').first()   
        return(user,None)