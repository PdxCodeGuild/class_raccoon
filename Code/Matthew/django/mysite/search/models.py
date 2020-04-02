from django.db import models

class Word(models.Model):
  word = models.CharField(max_length=100)
  definition = models.TextField()
  counter = models.IntegerField()

  class Meta:
    ordering = ['-counter', 'word']

  def __str__(self):
    return str(self.counter) + ' ' + self.word