from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect

from .models import TodoItem


def index(request):
    context = {
        'title': 'Todo List',
        'todo_items': TodoItem.objects.order_by('text')
    }
    return render(request, 'todoapp/index.html', context)

def savetodo(request):
    todo_text = request.POST['todo_text']
    todo_item = TodoItem(text=todo_text)
    todo_item.save()

    # return HttpResponse('ok')
    return HttpResponseRedirect(reverse('todoapp:index'))

def about(request):
    return render(request, 'todoapp/about.html')