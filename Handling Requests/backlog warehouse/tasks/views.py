from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from tasks.models import Task


@csrf_exempt
def delete_task(request, task_id):
    if request.method == "DELETE":
        try:
            task = Task.objects.get(pk=task_id)
            name = task.name
            task.delete()
            return HttpResponse(f"Task Done: '{name}'")
        except Task.DoesNotExist:
            return HttpResponse(f"There isn't any task with id '{task_id}'")
