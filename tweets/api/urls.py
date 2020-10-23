from django.urls import path
from .views import (
    Tweet_Detail_View,
    Tweet_Delete_View,
    Tweet_Action_View,
    Tweet_List_View,
)
from django.conf import settings

urlpatterns = [
    path('list/',Tweet_List_View),
    path('<int:tweet_id>/',Tweet_Detail_View),
    path('action/',Tweet_Action_View),
    path('delete/',Tweet_Delete_View)
]
