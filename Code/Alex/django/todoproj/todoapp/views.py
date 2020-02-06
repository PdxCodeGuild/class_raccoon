from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import ToDoItem



def index(request):
    #return HttpResponse('ok')
    context = {
    'title': 'ToDo',
    #'todo_items': ToDoItem.objects.all()
    'todo_items': ToDoItem.objects.order_by('text')
    }
    return render(request, 'todoapp/index.html', context)



def savetodo(request):
    #print(request.POST)
    todo_text = request.POST['todo_text']
    todo_item = ToDoItem(text=todo_text)
    todo_item.save()
    #return HttpResponse('ok')
    return HttpResponseRedirect(reverse('todoapp:index'))


def about(request):
    return render(request, 'todoapp/about.html')



def blog(request):
    return HttpResponse('blog page')