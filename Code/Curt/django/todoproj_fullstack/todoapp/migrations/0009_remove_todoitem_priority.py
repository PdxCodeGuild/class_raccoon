# Generated by Django 3.0.4 on 2020-03-05 23:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0008_todoitem_priority'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todoitem',
            name='priority',
        ),
    ]