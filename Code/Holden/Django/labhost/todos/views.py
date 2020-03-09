from django.shortcuts import render, reverse, redirect
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Todo
import json

@login_required
def index(request):
    user = request.user
    initialTodos = Todo.objects.filter(user=user, completed=False)
    initialCompleted = Todo.objects.filter(user=user, completed=True)
    initialTodosJS = "["
    for todo_item in initialTodos:
        initialTodosJS += '{"todo": "' + todo_item.todo + '", "id": ' + str(todo_item.id) + "},"
    initialTodosJS += "]"
    initialCompletedJS = "["
    for todo_item in initialCompleted:
        initialCompletedJS += '{"todo": "' + todo_item.todo + '", "id": ' + str(todo_item.id) + "},"
    initialCompletedJS += "]"
    context = {
        'initialTodos': initialTodosJS,
        'initialCompleted': initialCompletedJS,
    }
    return render(request, 'todos/index.html', context)

@login_required
def save(request):
    parsed = json.loads(request.body)
    if parsed['todo']:
        user = request.user
        new = Todo(todo=parsed['todo'], user=user)
        new.save()
        return HttpResponse(new.id)

@login_required
def complete(request):
    parsed = json.loads(request.body)
    user = request.user
    todo = Todo.objects.filter(id=parsed['id']).first()
    print(todo)
    if todo:
        if todo.user == user:
            if parsed['completed'] == 'true':
                todo.completed = True
                todo.save()
                return HttpResponse('')
            if parsed['completed'] == 'false':
                todo.completed = False
                todo.save()
                return HttpResponse('')
            return HttpResponse('Error: no operation specified')
    return HttpResponse('Error: specified todo does not exist')

@login_required
def delete(request):
    parsed = json.loads(request.body)
    user = request.user
    todo = Todo.objects.filter(id=parsed['id']).first()
    if todo:
        if todo.user == user:
            todo.delete()
            return HttpResponse('')
    return HttpResponse('Error: specified todo does not exist')
