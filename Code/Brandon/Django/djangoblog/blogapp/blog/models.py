from django.db import models

# Create your models here.

class blogPost (models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=200)
    date = models.DateTimeField()

    def __str__(self):
        return self.title

