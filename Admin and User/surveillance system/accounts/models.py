from django.db import models

# imports here
from django.contrib.auth.models import AbstractUser


# write your models here
class User(AbstractUser):
    national_code = models.CharField(max_length=10, unique=True)
    height = models.IntegerField()
    father_name = models.CharField(max_length=50)
