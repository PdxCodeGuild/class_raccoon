# Generated by Django 3.0.3 on 2020-02-18 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0004_auto_20200217_1348'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='url',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]