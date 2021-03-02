from django.forms import models
from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import TwitterUser
from django.contrib.auth.models import AbstractUser


# Create your views here.
def homepage(request):
    return render(request, 'index.html', {})


@ login_required
def user_detail(request, user_id):
    user_obj = TwitterUser.objects.get(id=user_id)
    return render(request, 'detail/user.html', {
        "user": user_obj,
    })
