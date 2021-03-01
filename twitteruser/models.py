from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class MyCustomUser(AbstractUser):
    username = models.CharField(
    max_length=40,
    null=True,
    unique = True)