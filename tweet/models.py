from django.db import models
from django.utils import timezone
from twitteruser.models import TwitterUser


class Tweet(models.Model):
    body = models.CharField(max_length=280)
    time = models.DateTimeField(default=timezone.now)
    twitter_user = models.ForeignKey(TwitterUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.body
