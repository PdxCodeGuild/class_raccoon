from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import BlogPost, BlogPostType

def index(request):
    # return HttpResponse('hello world!')
    blog_posts = BlogPost.objects.order_by('date_published')
    blog_post_types = BlogPostType.objects.all()
    context = {
        'blog_posts': blog_posts,
        'blog_post_types': blog_post_types
    }
    return render(request, 'blogapp/index.html', context)