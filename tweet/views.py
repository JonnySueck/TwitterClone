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
                user=request.user.author,
                date_posted=data['date_posted']
            )
            return HttpResponseRedirect('/')

    form = TweetForm()
    return render(request, 'index.html', {'form': form})
