from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Other required imports here
from tasks.models import Task


@csrf_exempt
def list_create_tasks(request):
    if request.method == "POST":
        task = request.POST.get("task")
        task = Task.objects.create(name=task)
        return HttpResponse(f"Task Created: '{task.name}'")
