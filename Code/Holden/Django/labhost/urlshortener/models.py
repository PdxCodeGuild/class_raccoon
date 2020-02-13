from django.db import models

class ShortUrl(models.Model):
    code = models.CharField(max_length=80)
    url = models.CharField(max_length=2048)
    counter = models.IntegerField(default=0)

    def __str__(self):
        trunc_url = slice(20)
        elipses = ''
        if len(self.url) > 20:
            elipses = '...'
        return self.code + '/: ' + self.url[trunc_url] + elipses

# {{ short.url | truncatechars:20 }}
