from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class TwitterUser(AbstractUser):
    followers = models.IntegerField(default=0)
    following = models.IntegerField(default=0)
    tweets = models.IntegerField(default=0)