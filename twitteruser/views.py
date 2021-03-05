from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import TwitterUser


# Create your views here.
@login_required
def homepage(request):
    return render(request, 'index.html', {})


def user_detail(request, user_id):
    user_obj = TwitterUser.objects.get(id=user_id)
    return render(request, 'detail/user.html', {"user": user_obj})


def follow(request, user_id):
    if request.user != user_id:
        user_to_follow = TwitterUser.objects.get(id=user_id)
        id = request.user.id
        editable = TwitterUser.objects.get(id=id)
        editable.following.add(TwitterUser.objects.get(id=user_id))
        editable.save()
        return redirect('/')

