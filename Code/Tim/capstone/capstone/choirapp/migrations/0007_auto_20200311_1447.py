# Generated by Django 3.0.4 on 2020-03-11 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('choirapp', '0006_auto_20200310_1624'),
    ]

    operations = [
        migrations.AlterField(
            model_name='composition',
            name='turn_in_date',
            field=models.DateField(blank=True),
        ),
    ]
