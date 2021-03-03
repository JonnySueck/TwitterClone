from django.contrib import admin
from twitteruser.models import TwitterUser


class AdminState(admin.ModelAdmin):
    list_display = ('username', 'followers', 'following', 'tweets')
# Register your models here.
admin.site.register(TwitterUser, AdminState)