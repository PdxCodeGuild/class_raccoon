from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect

from .models import TodoItem

def index(request):
    context = {
        'message': "Witches be strippin'!",
        'todo_items': TodoItem.objects.all()
    }
    return render(request, 'todoapp/index.html', context)

def savetodo(request):
    todo_text = request.POST['todo_text']
    todo_item = TodoItem(text=todo_text)
    todo_item.save()

    return HttpResponseRedirect(reverse('todoapp:index'))
