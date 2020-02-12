from django.db import models

from django.utils import timezone

from datetime import date


class Contact(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    birthday = models.DateField()
    phone_number = models.CharField(max_length=200)
    comments = models.TextField()

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    def age(self):
        born = self.birthday
        today = date.today()
        return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

    def formatted_birthday(self):
        return self.birthday.strftime('%Y-%m-%d')


