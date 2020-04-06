from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='todos')
    todo = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.user.username + "-" + self.todo
