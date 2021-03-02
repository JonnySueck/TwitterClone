from django.forms import models
from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .forms import SignupForm
from .models import MyCustomUser
from django.contrib.auth.models import AbstractUser


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


@ login_required
def user_detail(request, user_id):
    user_obj = MyCustomUser.objects.get(id=user_id)
    return render(request, 'detail/user.html', {
        "user": user_obj,
    })