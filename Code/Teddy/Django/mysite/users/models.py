from django.db import models
from django.contrib.auth.models import User

class UrlRedirect(models.Model):
    code = models.CharField(max_length=20)
    url = models.TextField()
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='urlredirects')
    counter = models.IntegerField()

    def __str__(self):
        return self.user.username + ' ' + self.code + ' ' + self.url
