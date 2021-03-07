from django.shortcuts import redirect, render
from django.db.models.signals import post_save
from tweet.models import Tweet
from twitteruser.models import TwitterUser
from notification.models import notification

# Create your views here.
def notifications(request):
    notifications = notification
    user = request.user
    tweets = Tweet.objects.all()
    # for tweet in tweets:
    #     if f'@{ user }' in tweet.text:
    #         # notifications.notifications += 1
    #         notifications.save()
    return render(request, 'index.html', {'notifications': notifications})
    

