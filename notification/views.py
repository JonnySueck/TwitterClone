from django.shortcuts import render
from django.db.models.signals import post_save
from tweet.models import Tweet
from twitteruser.models import TwitterUser
from notifications.signals import notify
from notifications import notify

# Create your views here.
def notification(request):
    notifications = 0
    user = request.user
    tweets = Tweet.objects.all()
    for tweet in tweets:
        if f'@{ user }' in tweet:
            notifications += 1

