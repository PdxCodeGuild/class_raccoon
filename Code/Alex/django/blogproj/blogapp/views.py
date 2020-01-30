from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import BlogPost, BlogPostType


def index(request):
    #return HttpResponse('Hello World!')
    # context = {
    #     'message': 'Hello World!',
    #     'names': ['jack', 'jill', 'john']
    # }
    #
    # return render(request, 'blogapp/index.html', context)

    blog_posts = BlogPost.objects.all()
    blog_post_types = BlogPostType.objects.all()
    context = {
    'blog_posts': blog_posts,
    'blog_post_types': blog_post_types
    }
    return render(request, 'blogapp/index.html', context)