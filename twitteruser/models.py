from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings



# Create your models here.
class TwitterUser(AbstractUser):
    following = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True)
