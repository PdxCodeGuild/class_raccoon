from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
import json
from .models import Priority, TodoThing

def index(request):
    posts = TodoThing.objects.all()
    context = {
    'posts': posts
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
    title = data['title']
    body = data['body']
    if title == '' or body == '':
        return HttpResponse('not ok')
    blog_post = BlogPost(title=title, body=body, created_date=timezone.now())
    blog_post.save()
    return HttpResponse('ok')
