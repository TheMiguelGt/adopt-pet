from django.urls import path
from core import views 
from .views import HomePageView

urlpatterns = [
    #core paths
    path('',HomePageView.as_view(),name="home"),
]
