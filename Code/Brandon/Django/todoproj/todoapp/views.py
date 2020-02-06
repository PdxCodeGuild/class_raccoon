from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import TodoItem

# Create your views here.


def index(request):
    context = {
        'title': 'To Do',
        'todo_items': TodoItem.objects.all().order_by('text')
    }
    return render(request,'todoapp/index.html',context)

def savetodo(request):
    todo_text = request.POST['todo_text']
    todo_item = TodoItem(text=todo_text)
    todo_item.save()

    return HttpResponseRedirect(reverse('todoapp:index'))

def about(request):
    return render(request,'todoapp/about.html')
