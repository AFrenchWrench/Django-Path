from django.db import models

COLOR_CHOICES = (
    ("b", "black"),
    ("w", "white"),
)


class Factory(models.Model):
    name = models.CharField(max_length=10)


class Car(models.Model):
    name = models.CharField(max_length=10)
    color = models.CharField(max_length=10, choices=COLOR_CHOICES)
    factory = models.ForeignKey(Factory, on_delete=models.CASCADE)
    price = models.IntegerField()
