from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
import json
from .models import ListItem, ItemPriority



def index(request):
    return render(request, 'todolist/index.html')



def listtodos(request):
    todos = ListItem.objects.all()
    data = []
    for todo in todos:
        data.append({
            'todoitem': todo.to_do_item,
            'priority': str(todo.priority)
        })
    return JsonResponse({'data': data})



def addtodos(request):
    pass