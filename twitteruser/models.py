from django.db import models
from django.contrib.auth.models import AbstractUser


class TwitterUser(AbstractUser):
   
    display_name = models.CharField("Handle", null=True, max_length=20)
    age = models.IntegerField(null=True, blank=True)
    following = models.ManyToManyField('self', symmetrical=False)
    REQUIRED_FIELDS = ['age']
