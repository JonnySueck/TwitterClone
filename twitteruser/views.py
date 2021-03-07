from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import TwitterUser
from django.template import  RequestContext


# Create your views here.
@login_required
def homepage(request):
    return render(request, 'index.html', {})


def user_detail(request, user_id):
    requested_user = TwitterUser.objects.get(id=user_id)
    return requested_user


def following(request, user_id):
    user = TwitterUser.objects.get(id=user_id)
    following = len(user.following.all())
    return following


def follow(request, user_id):
    id = request.user.id
    editable = TwitterUser.objects.get(id=id)
    if request.method == 'GET':
        if request.user != user_id:
            editable.following.add(TwitterUser.objects.get(id=user_id))
            editable.save()
            return render(request, 'index.html', {})


def unfollow(request, user_id):
    id = request.user.id
    editable = TwitterUser.objects.get(id=id)
    if request.method == 'GET':
        if request.user != user_id:
            editable.following.remove(TwitterUser.objects.get(id=user_id))
            editable.save()
            return render(request, 'index.html', {})
