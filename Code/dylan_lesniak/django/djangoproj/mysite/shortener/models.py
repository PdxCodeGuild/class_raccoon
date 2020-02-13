from django.db import models

# Create your models here.
class Short(models.Model):
    longform = models.CharField(max_length=2000)
    shortform = models.CharField(max_length=100)
    name = models.CharField(max_length=200, default="N/A")
    

    def __str__(self):
        return f"Name: {self.name} | ID: {self.id} | Shortform: {self.shortform}"

        