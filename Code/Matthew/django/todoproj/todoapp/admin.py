from django.contrib import admin

from .models import TodoItem, TodoItemPriority

admin.site.register(TodoItem)
admin.site.register(TodoItemPriority)



