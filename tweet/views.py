from tweet.models import Tweet
from django.shortcuts import render, HttpResponseRedirect
from .forms import TweetForm
from django.contrib.auth.decorators import login_required


# Create your views here.
@ login_required
def add_tweet(request):
    if request.method == 'POST':
        # create an instance and fill with request data
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


def users_tweets(request, user_id):
    user_tweets = Tweet.objects.all()
    print(users_tweets)
    return render(request, 'detail/user.html', {'tweets': user_tweets})
