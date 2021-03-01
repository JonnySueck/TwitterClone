from django.contrib import admin
from twitteruser.models import MyCustomUser


class AdminState(admin.ModelAdmin):
    list_display = ('username', 'followers', 'following')
# Register your models here.
admin.site.register(MyCustomUser, AdminState)