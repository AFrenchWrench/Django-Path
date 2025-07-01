from django.shortcuts import render, HttpResponse
from django.views import View
from .models import Musician, Album


class Musician_list(View):
    # type your code here
    def get(self, request):
        return HttpResponse(
            Musician.objects.values_list("name", flat=True).order_by("name")
        )
