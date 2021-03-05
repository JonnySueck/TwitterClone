from tweet.models import Tweet
from django.shortcuts import render, HttpResponseRedirect
from .forms import TweetForm
from django.contrib.auth.decorators import login_required


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
    users_tweets = Tweet.objects.filter(user=user_id)
    num_tweets = len(users_tweets)
    return render(request, 'detail/user.html', {
        'tweets': users_tweets,
        'num': num_tweets})
