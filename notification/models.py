from django.db import models
from twitteruser.models import TwitterUser
from tweet.models import Tweet


class Notification(models.Model):
    follow_target = models.ForeignKey(TwitterUser, on_delete=models.CASCADE)
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE)
    viewed = models.BooleanField(default=False)
