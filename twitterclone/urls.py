"""twitterclone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from twitteruser import views
from authentication.views import signup_view
from tweet.views import add_tweet, tweet_detail, users_tweets


urlpatterns = [
    path('', views.homepage, name='home'),
    path('tweet/new/', add_tweet, name='tweetnew'),
    path('tweet/<int:post_id>/', tweet_detail, name='tweetdetail'),
    path('accounts/<int:user_id>/', users_tweets, name='userdetail'),
    path('accounts/new/', signup_view, name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
]
