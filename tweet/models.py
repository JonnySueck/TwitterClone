from django.db import models
from twitteruser.views import TwitterUser
from django.utils import timezone
from django.contrib.auth.models import User



# Create your models here.
class Tweet(models.Model):
    text = models.CharField(max_length=140)
    date_posted = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(TwitterUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.text