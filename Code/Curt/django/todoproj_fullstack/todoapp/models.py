from django.db import models

class TodoItem(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text
