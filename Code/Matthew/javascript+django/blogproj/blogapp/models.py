from django.db import models



class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    created_date = models.DateTimeField()

    def __str__(self):
        return self.title

