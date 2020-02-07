from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import TodoItem, TodoItemPriority
from django.utils import timezone
import random

def index(request):
    emoji = random.choice(['😀', '😁', '😴'])
    todo_items = TodoItem.objects.filter(completed_date__isnull=True)
    order = request.GET.get('order', 'priority')
    if order == 'alphabetical':
        todo_items = todo_items.order_by('text')
    elif order == 'priority':
        todo_items = todo_items.order_by('-priority__order')
    elif order == 'random':
        todo_items = list(todo_items.all())
        random.shuffle(todo_items)
    else:
        todo_items = todo_items.all()

    completed_items = TodoItem.objects.filter(completed_date__isnull=False)

    # todo_items = TodoItem.objects.all()
    # todo_items = todo_items.filter(text='wash the dog')
    # todo_items = todo_items.order_by('text')
    # print(todo_items)

    todo_priorities = TodoItemPriority.objects.order_by('-order')
    context = {
        'title': 'Todo List ' + emoji,
        'error': '',
        'todo_items': todo_items,
        'completed_items': completed_items,
        'todo_priorities': todo_priorities,
    }
    return render(request, 'todoapp/index.html', context)

def savetodo(request):
    print(request.POST)

    # get data out of dictionary
    todo_text = request.POST['todo_text']
    todo_priority_id = request.POST['todo_priority_id']

    # create an instance of our model
    # TodoItemPriority.objects.get(name='high')
    # todo_priority = TodoItemPriority.objects.get(id=todo_priority_id)
    # todo_item = TodoItem(text=todo_text, priority=todo_priority)

    todo_item = TodoItem(text=todo_text, priority_id=todo_priority_id)

    # save the instance
    todo_item.save()

    # redirect back to the index view
    return HttpResponseRedirect(reverse('todoapp:index'))


def completetodo(request):
    todo_item_id = request.POST['todo_item_id']
    todo_item = TodoItem.objects.get(id=todo_item_id)
    if todo_item.completed_date is None:
        todo_item.completed_date = timezone.now()
    else:
        todo_item.completed_date = None
    todo_item.save()
    return HttpResponseRedirect(reverse('todoapp:index'))


def deletetodo(request, todo_item_id):
    todo_item = TodoItem.objects.get(id=todo_item_id)
    todo_item.delete()
    return HttpResponseRedirect(reverse('todoapp:index'))
