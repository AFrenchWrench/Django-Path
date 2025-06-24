from django.http import HttpResponse


def make_sad(request, name):
    return HttpResponse(f"Nobody likes you, {name}!")


def make_happy(request, name, times):
    return HttpResponse(f"You are great, {name} :)<br>" * times)
