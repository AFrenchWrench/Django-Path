from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=10)
    rate = models.IntegerField(default=0)
    free = models.BooleanField(default=True)
