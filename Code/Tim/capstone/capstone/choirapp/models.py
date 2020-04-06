from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from datetime import datetime

class Composer(models.Model):
    comp_last = models.CharField(max_length=20, verbose_name='Last Name')
    comp_first = models.CharField(max_length=20, verbose_name='First Name', blank=True)
    class Meta:
        ordering = ['comp_last']
    def __str__(self):
        return str(self.comp_last) + ", " + str(self.comp_first)

class Composition(models.Model):
    cat_num = models.CharField(max_length=10, verbose_name='Catalog No.', blank=True)
    comp_last = models.ForeignKey(Composer, on_delete=models.PROTECT, related_name='composition', verbose_name='Composer')
    title = models.CharField(max_length=80)
    copies = models.IntegerField(null=True, blank=True)
    voicing = models.CharField(max_length=20, default='SATB', verbose_name='Voicing', null=True, blank=True)
    spec_notes = models.TextField(verbose_name='Special Notes', blank=True)
    location = models.CharField(max_length=30, default='Stacks', verbose_name='Location', blank=True)
    choristers = models.BooleanField(default=False)
    turn_in_date = models.DateField(null=True, blank=True)

    class Meta:
        ordering = ['comp_last']

    def __str__(self):

        return str(self.comp_last.comp_last) + ", " + str(self.comp_last.comp_first) + " - " + self.title

class Librarian(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='librarian')
    def __str__(self):
        return self.user.username

class Rehearsal(models.Model):
    notes = models.TextField(verbose_name='Notes', blank=True)
    pieces = models.CharField(max_length=2000)

    def __str__(self):

        return self.pieces
