from django.db import models
from twitteruser.models import TwitterUser
from tweet.models import Tweet


class Notification(models.Model):
    recipient = models.ForeignKey(TwitterUser, on_delete=models.CASCADE)
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE)

    def __str__(self):
        return {self.recipient}
