from django.contrib import admin
from twitteruser.models import TwitterUser


class AdminState(admin.ModelAdmin):
    list_display = ('username',)
# Register your models here.
admin.site.register(TwitterUser, AdminState)