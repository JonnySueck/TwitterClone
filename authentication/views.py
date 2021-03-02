from django.shortcuts import render, HttpResponseRedirect
from .forms import SignupForm
from twitteruser.views import TwitterUser


# Create your views here.
def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_user = TwitterUser.objects.create_user(
                password=data['password'],
                username=data['username'],

            )
            return render(request, 'index.html', {'user_new': new_user})

    form = SignupForm()
    return render(request, 'registration/signup.html', {'form': form})