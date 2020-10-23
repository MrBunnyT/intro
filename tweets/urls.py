from django.urls import path,include
from .views import (
    HomeView,
)
from django.conf import settings

urlpatterns = [
    path('',HomeView),
    path('',include('tweets.api.urls')),
]