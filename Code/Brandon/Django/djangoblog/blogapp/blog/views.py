from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse

from .models import blogPost


def index(request):

    return render(request,'blog/index.html')

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