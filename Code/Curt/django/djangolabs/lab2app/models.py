from django.db import models

class Contact(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    birthday = models.DateField()
    phone_number = models.CharField(max_length=200)
    is_cell = models.BooleanField()

    def __str__(self):
        cellstat = self.cellstat()
        return self.last_name + ', ' + self.first_name + ' | ' + str(self.birthday) + ' | ' + self.phone_number + ' | Cell Phone: ' + str(cellstat)

    def cellstat(self):
        if self.is_cell:
            cellstat = "Yes"
        else:
            cellstat = "No"
        return cellstat

    def formatted_birthday(self):
        return self.birthday.strftime('%Y/%m/%d')