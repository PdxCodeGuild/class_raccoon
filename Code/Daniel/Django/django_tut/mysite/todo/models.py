from django.db import models

class Priority(models.Model):
    priority = models.CharField(max_length=30)

    def __str__(self):
        return self.priority

class Tasks(models.Model):
    task = models.CharField(max_length=100)
    created_date = models.DateTimeField()
    priority = models.ForeignKey(Priority, on_delete=models.PROTECT)
    complete = models.BooleanField()

    def __str__(self):
        return self.task

