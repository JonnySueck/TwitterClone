from twitteruser.views import user_detail
from tweet.models import Tweet
from django.shortcuts import render, HttpResponseRedirect
from .forms import TweetForm
from django.contrib.auth.decorators import login_required
from twitteruser.models import TwitterUser


# Create your views here.
@ login_required
def add_tweet(request):
    if request.method == 'POST':
        # create an instance and fill with request data
        form = TweetForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user_id = request.user.id
            Tweet.objects.create(
                text=data['text'],
                user=request.user
            )
            
            return HttpResponseRedirect('/')

    form = TweetForm()
    return render(request, 'tweet.html', {'form': form})


def users_tweets(request, user_id):
    tweets = Tweet.objects.all(user=user_id)
    return render(request, 'detail/user.html', {'tweets': tweets})
