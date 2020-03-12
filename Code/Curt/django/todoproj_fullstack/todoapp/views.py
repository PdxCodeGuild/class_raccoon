from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.db.models import F
import json

from .models import TodoItem

def index(request):
    context = {
        'title': "Toto's Todo's",
        'todo_items': TodoItem.objects.all()
    }
    return render(request, 'todoapp/index.html', context)

def savetodo(request):
    save_json = json.loads(request.body)
    todo_text = save_json['todo_text']
    due_date = save_json['due_date']
    if save_json['priority'] == 'low':
        priority = '0'
    elif save_json['priority'] == 'medium':
        priority = '1'
    else:
        priority = '2'
    todo_item = TodoItem(text=todo_text, due_date=due_date, priority=priority)
    todo_item.save()

    return HttpResponseRedirect(reverse('todoapp:index'))

def entries(request):
    entries = TodoItem.objects.order_by('-priority', F('due_date').asc(nulls_last=True))
    data = []
    priority_list = ["Low","Medium","High"]
    for entry in entries:
        priority = priority_list[int(entry.priority)]
        if entry.due_date:
            data.append({
                'text': entry.text,
                'due_date': entry.due_date.strftime('%m/%d/%Y'),
                'creation_date': entry.creation_date,
                'priority': priority,
                'completed': entry.completed,
            })
        else:
            data.append({
                'text': entry.text,
                'due_date': entry.due_date,
                'creation_date': entry.creation_date,
                'priority': priority,
                'completed': entry.completed
            })
    return JsonResponse({'todo_items': data})
