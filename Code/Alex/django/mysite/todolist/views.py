from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
import json
from .models import ListItem, ItemPriority



def index(request):
    return render(request, 'todolist/index.html')



def listtodos(request):
    todos = ListItem.objects.all()
    data = []
    priorities = ItemPriority.objects.all()
    priority_data = []
    for todo in todos:
        data.append({
            'todoitem': todo.to_do_item,
            'priority': str(todo.priority)
        })
    for priority in priorities:
        priority_data.append({
            'priority': priority.priority,
        })
    return JsonResponse({'data': data, 'priorities':priority_data})



def addtodos(request):
    data = json.loads(request.body)
    to_do_item = data['item']
    priority = data['priority']
    if to_do_item == '' or priority == '':
        return HttpResponse('error')
    priority = ItemPriority.objects.get(priority=priority['priority']['priority'])
    todo_post = ListItem(to_do_item=to_do_item, priority=priority)
    todo_post.save()
    return HttpResponse('Item Saved')