from django.db import models

# Create your models here.

class Priority(models.Model):
    plevel = models.CharField(max_length=39)

    def __str__(self):
        return self.plevel

class TodoThing(models.Model):
    things = models.CharField(max_length=200)
    plevel = models.ForeignKey(Priority, on_delete=models.PROTECT, related_name='todothing')
    done = models.BooleanField(default=False)

    def __str__(self):
        return  self.things + ' (' + str(self.plevel) + ')'
