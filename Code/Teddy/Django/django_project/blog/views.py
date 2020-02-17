from django.shortcuts import render

posts = [
    {
        'author': 'Teddy',
        'title': 'Blog post 1',
        'content': 'First content',
        'date_posted': 'Aug 27, 2018'
    },
    {
        'author': 'Photo',
        'title': 'Blog post 2',
        'content': 'Second content',
        'date_posted': 'Aug 28, 2018'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
