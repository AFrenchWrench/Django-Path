from django.http import HttpResponse
from django.shortcuts import render

from .forms import PersonalInformation
from .models import Person


def show_people(request):
    if request.method == "GET":
        persons = Person.objects.all()
        context = {"persons": persons}
        return render(request, "show_people.html", context)


def submit_person(request):
    if request.method == "GET":
        return render(request, "new_person.html", {"form": PersonalInformation()})
    elif request.method == "POST":
        form = PersonalInformation(request.POST)
        if form.is_valid():
            person = Person.objects.create(**form.cleaned_data)
            return HttpResponse(person, status=201)
        return HttpResponse("Error", status=400)
