from django.shortcuts import redirect, render
from django.db.models.signals import post_save
from tweet.models import Tweet
from twitteruser.models import TwitterUser
from notification.models import notification
import datetime
import time

# Create your views here.
def notifications(request):
    user = request.user
    mentioned_tweets = Tweet.objects.filter(text__contains=f'@{user}')
    len_mentioned = len(mentioned_tweets)
    print(len_mentioned)
    editable = notification()
    print(editable)
    sent_notification = []
    for tweet in mentioned_tweets:
        if tweet.id not in sent_notification:
            sent_notification.append(tweet.id)
            editable.notifications += 1
            editable.save()
        
    return render(request, 'index.html', {
            'notifications': editable,
            'mentioned': mentioned_tweets
        })
    

def clear_notifications(request):
    editable = notification()
    editable.notifications = 0
    editable.save()
    return render(request, 'index.html', {'editable': editable})