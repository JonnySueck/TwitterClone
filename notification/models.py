from django.db import models

# Create your models here.
class notification(models.Model):
    notifications = models.IntegerField(default=0, null=True)

