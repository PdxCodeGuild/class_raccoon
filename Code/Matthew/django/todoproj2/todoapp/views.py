from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import random

def index(request):
    emoji = random.choice(['😀', '😁', '😴'])
    context = {'title': 'Todo List ' + emoji, 'error': 'An Error Occurred'}
    return render(request, 'todoapp/index.html', context)

def savetodo(request):
    return HttpResponse('you are at the savetodo view')

def api(request):
    data = {'foo': 'bar', 'hello': 'world', 'nums': [1, 2, 3]}
    return JsonResponse(data)

def other(request, path):
    return HttpResponse('you are at ' + path)