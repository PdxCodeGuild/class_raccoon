from django.db import models

class ToDoItem(models.Model):
    text = models.TextField()
    #priority = models.IntegerField()

    def __str__(self):
        return self.text + '!!'


