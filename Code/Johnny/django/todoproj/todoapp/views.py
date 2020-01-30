from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import TodoItem
# Create your views here.

def index(request):
    context = {
    'title': 'Todo',
    'todo_items': TodoItem.objects.all(),
    # 'todo_items': TodoItem.objects.order_by('text') orders by key
    }
    return render(request, 'todoapp/index.html', context)

def savetodo(request):
    # print(request.post)
    todo_text = request.POST['todo_text']
    todo_item = TodoItem(text=todo_text)
    todo_item.save()

    return HttpResponseRedirect(reverse('todoapp:index'))


def about(request):
 return render(request, 'todoapp/about.html')
