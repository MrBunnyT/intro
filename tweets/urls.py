from django.urls import path
from .views import (
    HomeView,
    Tweet_Detail_View,
    ListView,Tweet_Create_View,
    Tweet_Delete_View,
    Tweet_Action_View,
    Accounts
)
from django.conf import settings

urlpatterns = [
    path('list/tweets/',ListView),
    path('',HomeView),
    path('post/',Tweet_Create_View),
    path('<int:tweet_id>/',Tweet_Detail_View),
    path('action/',Tweet_Action_View),
    path('<int:tweet_id>/delete/',Tweet_Delete_View),
    path(settings.LOGIN_URL,Accounts.login),
]
