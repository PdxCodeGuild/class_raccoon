from django.shortcuts import render, reverse
from django.http import HttpResponse, JsonResponse
import json
from .models import Priority, TodoThing

def index(request):
    tasks = TodoThing.objects.all()
    context = {
    'tasks': tasks
    }
    return render(request, 'vuetodo/index.html', context)

def create_post(request):
    data = json.loads(request.body)
    things = data['things']
    plevel = data['plevel']
    if things == '' or plevel == '':
        return HttpResponse('not ok')
    todo_post = TodoThing(things=things, plevel=plevel)
    todo_post.save()
    return HttpResponse('ok')


def post(request):
    tasks = TodoThing.objects.all()
    data = []
    for task in tasks:
        data.append({
            'id': post.id,
            'things': post.things,
            'plevel': post.plevel,
            'done': post.done,
        })
    return JsonResponse({data})
