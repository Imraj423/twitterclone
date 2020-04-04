from django.db import models
from django.utils import timezone
from twitteruser.models import TwitterUser


class Tweet(models.Model):
    body = models.CharField(max_length=140)
    time = models.DateTimeField(default=timezone.now)
    twitter_user = models.ForeignKey(TwitterUser, default=None,
                                     on_delete=models.CASCADE)

    def __str__(self):
        return self.body
