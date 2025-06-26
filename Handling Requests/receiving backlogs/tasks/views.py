# Needed imports here
from django.http import HttpResponse
from tasks.models import Task


def list_create_tasks(request):
    if request.method == "GET":
        all_tasks = Task.objects.values_list("name", flat=True).order_by("name")
        return HttpResponse("<br>".join(all_tasks))


def count_tasks(request):
    if request.method == "GET":
        all_tasks_count = Task.objects.count()
        return HttpResponse(f"You have '{all_tasks_count}' tasks to do")
