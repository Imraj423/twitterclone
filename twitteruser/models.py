from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    first_name = models.CharField(null=True, max_length=20)
    display_name = models.CharField(null=True, max_length=20)
    email = models.CharField(null=True, max_length=20)

    REQUIRED_FIELDS = ['email', 'display_name', 'first_name']
