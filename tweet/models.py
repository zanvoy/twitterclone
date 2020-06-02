from django.db import models
from django.utils import timezone
from twitteruser.models import SomeUser

class Tweet(models.Model):
    body = models.TextField(max_length=140)
    date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(SomeUser, on_delete=models.CASCADE)
