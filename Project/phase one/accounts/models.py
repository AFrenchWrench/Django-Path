from django.contrib.auth.models import AbstractUser
from django.db import models

GENDER_CHOICES = [("F", "Female"), ("M", "Male")]


class User(AbstractUser):
    address = models.TextField(null=True, blank=True)
    age = models.PositiveSmallIntegerField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    gender = models.CharField(
        max_length=1, choices=GENDER_CHOICES, null=True, blank=True
    )
    phone = models.CharField(max_length=15, null=True, blank=True)
