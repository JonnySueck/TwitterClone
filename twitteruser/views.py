from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .forms import SignupForm
from .models import MyCustomUser


# Create your views here.
def homepage(request):
    return render(request, 'index.html', {})


def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_user = MyCustomUser.objects.create_user(
                password=data['password'],
                username=data['username'],

            )
            return HttpResponseRedirect('/')

    form = SignupForm()
    return render(request, 'registration/signup.html', {'form': form})

