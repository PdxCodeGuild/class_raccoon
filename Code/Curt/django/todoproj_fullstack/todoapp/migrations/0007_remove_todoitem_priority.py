# Generated by Django 3.0.4 on 2020-03-05 23:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0006_auto_20200305_1527'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todoitem',
            name='priority',
        ),
    ]
