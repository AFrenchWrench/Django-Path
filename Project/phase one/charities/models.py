from django.db import models

EXPERIENCE_CHOICES = [
    (0, "Beginner"),
    (1, "Intermediate"),
    (2, "Advanced"),
]

GENDER_CHOICES = [("F", "Female"), ("M", "Male")]

STATE_CHOICES = [("P", "Pending"), ("W", "Waiting"), ("A", "Assigned"), ("D", "Done")]


class Benefactor(models.Model):
    user = models.OneToOneField(
        "accounts.User", related_name="benefactor", on_delete=models.CASCADE
    )
    experience = models.SmallIntegerField(choices=EXPERIENCE_CHOICES, default=0)
    free_time_per_week = models.PositiveSmallIntegerField(default=0)


class Charity(models.Model):
    user = models.OneToOneField(
        "accounts.User", related_name="charity", on_delete=models.CASCADE
    )
    name = models.CharField(max_length=50)
    reg_number = models.CharField(max_length=10)


class Task(models.Model):
    assigned_benefactor = models.ForeignKey(
        Benefactor, null=True, on_delete=models.SET_NULL, related_name="tasks"
    )
    charity = models.ForeignKey(Charity, related_name="tasks", on_delete=models.CASCADE)
    age_limit_from = models.IntegerField(null=True, blank=True)
    age_limit_to = models.IntegerField(null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    gender_limit = models.CharField(
        max_length=1, choices=GENDER_CHOICES, null=True, blank=True
    )
    state = models.CharField(max_length=1, default="P")
    title = models.CharField(max_length=60)
