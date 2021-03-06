from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.utils import timezone
import json

from .models import blogPost

# Main view for single page app
def index(request):
    return render(request,'blog/index.html')

# Fetches the posts continuously or when ever called
def posts(request):
    posts = blogPost.objects.order_by('-date')
    data = []
    for post in posts:
        data.append({
            'id': post.id,
            'title': post.title,
            'content': post.content,
            'date': post.date.strftime('%m/%d/%Y')
        })
    return JsonResponse({'blog_posts': data})

# Creates and saves a new post to the blog
def create_post(request):
    print("hello")
    data = json.loads(request.body)
    title = data['title']
    body = data['content']
    if title == '' or body == '':
        return HttpResponse('not ok')
    blog_post = blogPost(title=title, content=body, date=timezone.now())
    blog_post.save()
    return HttpResponse('ok')