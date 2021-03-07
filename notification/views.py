from django.shortcuts import redirect, render
from django.db.models.signals import post_save
from tweet.models import Tweet
from twitteruser.models import TwitterUser
from notification.models import notification
import schedule
import datetime
import time

def check_for_new(request):
    print('checking for changes')
    user = request.user
    num_tweets = Tweet.objects.filter(text__contains=f'@{user}')
    check_len = len(num_tweets)
    schedule.every(30).seconds.do(check_for_new)
    return render(request, 'index.html', {'following': check_len})


# Create your views here.
def notifications(request):
    user = request.user
    mentioned_tweets = Tweet.objects.filter(text__contains=f'@{user}')
    len_mentioned = len(mentioned_tweets)
    editable = notification
    while len_mentioned == check_for_new(request):
        check_for_new(request)
        time.sleep(5)
    if check_for_new(request) > len_mentioned:
        print('_____changes found_____')
        editable.notifications = 1
        editable.save()
        
    return render(request, 'index.html', {
            'notifications': editable,
            'mentioned': mentioned_tweets
        })
    

