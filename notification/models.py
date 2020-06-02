from django.db import models
from twitteruser.models import SomeUser
from tweet.models import Tweet
from twitteruser.models import SomeUser

class Notification(models.Model):
    notifyee = models.ForeignKey(SomeUser, on_delete=models.CASCADE)
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE)
