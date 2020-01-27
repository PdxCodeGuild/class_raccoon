
from django.http import HttpResponse
from django.shortcuts import render

from .models import BlogPost, BlogPostType

def index(request):
    # return HttpResponse('hello world!')

    # context = {
    #     'message': 'hello world!',
    #     'names': ['jack', 'jill', 'jane']
    # }
    # return render(request, 'blogapp/index.html', context)

    blog_posts = BlogPost.objects.all()
    blog_post_types = BlogPostType.objects.all()
    context = {
        'blog_posts': blog_posts,
        'blog_post_types': blog_post_types
    }
    return render(request, 'blogapp/index.html', context)

