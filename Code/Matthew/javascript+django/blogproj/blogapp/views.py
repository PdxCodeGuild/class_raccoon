from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.core.paginator import Paginator
from django.utils import timezone
import json

from .models import BlogPost

def index(request):
    return render(request, 'blogapp/index.html')

def posts(request):
    posts = BlogPost.objects.order_by('-created_date')
    paginator = Paginator(posts, 10)
    page = request.GET.get('page', 1)
    posts = paginator.get_page(page)
    data = []
    for post in posts:
        data.append({
            'id': post.id,
            'title': post.title,
            'body': post.body,
            'created_date': post.created_date.strftime('%m/%d/%Y')
        })
    return JsonResponse({'num_pages': paginator.num_pages, 'blog_posts': data})


def create_post(request):
    data = json.loads(request.body)
    title = data['title']
    body = data['body']
    if title == '' or body == '':
        return HttpResponse('not ok')
    blog_post = BlogPost(title=title, body=body, created_date=timezone.now())
    blog_post.save()
    return HttpResponse('ok')