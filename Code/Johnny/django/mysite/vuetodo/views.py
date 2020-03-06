from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
import json
from .models import Priority, TodoThing

def index(request):
    posts = TodoThing.objects.all()
    priority = Priority.objects.all()
    context = {
    'posts': posts,
    'priority': priority,
    }
    return render(request, 'vuetodo/index.html', context)

def posts(request):
    posts = TodoThing.objects.order_by('-id')
    data = []
    for post in posts:
        data.append({
            'id': post.id,
            'things': post.things,
            'plevel': str(post.plevel),
            'done': post.done
        })
    return JsonResponse({'todo_posts': data})

def create_post(request):
    data = json.loads(request.body)
    print(data)
    things = data['new_post_things']
    plevel = data['new_post_level']
    if things == '':
        return HttpResponse('not ok')
    todo_posts = TodoThing(things=things, plevel=Priority.objects.get(plevel=plevel))
    todo_posts.save()
    return HttpResponse('ok')
