from django.shortcuts import render
from accounts.models import User
from django.db.models import Value, F
from django.db.models.functions import Concat


def about_us(request):
    names = (
        User.objects.only("first_name", "last_name")
        .annotate(full_name=Concat(F("first_name"), Value(" "), F("last_name")))
        .values_list("full_name", flat=True)
    )

    return render(request, "about_us.html", {"names": names})
