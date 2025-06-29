from .models import Book
from django.shortcuts import render


def booklist(request):
    context = {"books": Book.objects.all()}
    return render(request, "booklist.html", context=context)
