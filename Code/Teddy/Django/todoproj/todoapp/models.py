
from django.db import models

class TodoItemPriority(models.Model):
    name = models.CharField(max_length=50)
    order = models.IntegerField()

    def __str__(self):
        return str(self.order) + ') ' + self.name

    def get_class_name(self):
        return self.name.lower().replace(' ', '_')


class TodoItem(models.Model):
    text = models.CharField(max_length=500)
    priority = models.ForeignKey(TodoItemPriority, on_delete=models.PROTECT, related_name='todo_items')
    created_date = models.DateTimeField(auto_now_add=True)
    completed_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.text + ' (' + self.priority.name + ')'

    def is_completed(self):
        return self.completed_date is not None
