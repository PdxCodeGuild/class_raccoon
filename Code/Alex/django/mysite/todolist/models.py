from django.db import models



class ItemPriority(models.Model):
    priority = models.CharField(max_length=20)

    def __str__(self):
        return self.priority



class ListItem(models.Model):
    to_do_item = models.CharField(max_length=200)
    priority = models.ForeignKey(ItemPriority, on_delete=models.PROTECT)

    def __str__(self):
        return self.to_do_item

