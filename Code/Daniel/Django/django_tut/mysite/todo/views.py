from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.utils import timezone
from .models import Tasks, Priority
import json

def index(request):
    return render(request, 'todo/index.html')

def tasks(request):
    task = Tasks.objects.order_by('-created_date')
    priorities = Priority.objects.all()
    data=[]
    priority_levels=[]
    for tasks in task:
        data.append({
            'id': tasks.id,
            'task': tasks.task,
            'created_date': tasks.created_date.strftime('%m/%d/%Y'),
            'priority': str(tasks.priority),
            'complete': tasks.complete,
    })
    for priority in priorities:
        priority_levels.append({
            'priority_level': priority.priority
        })
    return JsonResponse({'todo_tasks': data, 'priority_level':priority_levels})

def create_task(request):
    data = json.loads(request.body)
    task = data['task']
    priority = data['priority']
    print(data)
    new_todo = Tasks(task=task, priority=Priority.objects.get(priority=priority), created_date=timezone.now(), complete=False)
    new_todo.save()
    return HttpResponse('complete')