# Generated by Django 3.0.4 on 2020-03-05 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0003_auto_20200305_1114'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todoitem',
            name='has_due',
        ),
        migrations.AlterField(
            model_name='todoitem',
            name='creation_date',
            field=models.DateField(auto_now=True),
        ),
    ]
