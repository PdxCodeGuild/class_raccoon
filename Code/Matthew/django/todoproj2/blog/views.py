from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('blog index view')

def detail(request, blog_post_id):
    return HttpResponse('blog post detail view of blog post with id ' + str(blog_post_id))