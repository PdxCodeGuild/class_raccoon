# Generated by Django 3.0.4 on 2020-03-23 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0002_auto_20200323_1413'),
    ]

    operations = [
        migrations.AddField(
            model_name='word',
            name='counter',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]