from django.shortcuts import redirect, render
from django.db.models.signals import post_save
from tweet.models import Tweet
from twitteruser.models import TwitterUser
from notification.models import notification
import schedule
import datetime
import time

read = []
# Create your views here.
def notifications(request):
    user = request.user
    mentioned_tweets = Tweet.objects.filter(text__contains=f'@{user}')
    len_mentioned = len(mentioned_tweets)
    editable = notification.notifications
    editable = len_mentioned
    print(editable)
    for tweet in mentioned_tweets:
        if tweet not in read:
            read.append(tweet.text)
        
    return render(request, 'index.html', {
            'notifications': editable,
            'mentioned': mentioned_tweets
        })
    

def clear_notifications(request):
    editable = notification
    editable.notifications = 0
    return render(request, 'index.html', {'editable': editable})