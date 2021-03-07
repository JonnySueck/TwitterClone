from django.db import models
from django.db.models.fields import IntegerField
from tweet.models import Tweet

# Create your models here.
class notification(models.Model):
    notifications = models.IntegerField(default=0)

