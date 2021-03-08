from tweet.models import Tweet
from django.shortcuts import render, HttpResponseRedirect
from .forms import TweetForm
from django.contrib.auth.decorators import login_required
from twitteruser.views import user_detail, following
from notification.models import notification
from notification.views import notifications


# Create your views here.
@ login_required
def add_tweet(request):
    if request.method == 'POST':
        form = TweetForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Tweet.objects.create(
                text=data['text'],
                user=request.user
            )
            return HttpResponseRedirect('/')

    form = TweetForm()
    return render(request, 'tweet.html', {'form': form})


def tweet_detail(request, post_id):
    tweet = Tweet.objects.get(id=post_id)
    return render(request, 'detail/tweet.html', {'tweet': tweet})


def users_tweets(request, user_id):
    user = user_detail(request, user_id)
    follow = following(request, user_id)
    users_tweets = Tweet.objects.filter(user=user_id)
    num_tweets = len(users_tweets)
    return render(request, 'detail/user.html', {
        'tweets': users_tweets,
        'num': num_tweets,
        'id': user_id,
        'requser': user,
        'following': follow
        })


def newsfeed(request):
    print(notifications)
    notify = notification()
    notify = notify.notifications
    tweets = Tweet.objects.all()
    ordered_tweets = reversed(tweets)
    return render(request, 'index.html', {
        'news': ordered_tweets,
        'notifications': notify
        })
