from twitteruser.views import user_detail
from tweet.models import Tweet
from django.shortcuts import render, HttpResponseRedirect
from .forms import TweetForm
from django.contrib.auth.decorators import login_required
from twitteruser.models import TwitterUser

def update_tweets(user_id):
    editable = TwitterUser.objects.get(id=user_id)
    editable.tweets += 1
    editable.save()
    return user_id


# Create your views here.
@ login_required
def add_tweet(request):
    if request.method == 'POST':
        # create an instance and fill with request data
        form = TweetForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user_id = request.user.id
            update_tweets(user_id)
            Tweet.objects.create(
                text=data['text'],
                user=request.user
            )
            
            return HttpResponseRedirect('/')

    form = TweetForm()
    return render(request, 'tweet.html', {'form': form})
