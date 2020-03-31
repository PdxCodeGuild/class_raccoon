# Generated by Django 3.0.4 on 2020-03-12 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('choirapp', '0009_auto_20200312_1102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='composition',
            name='copies',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='composition',
            name='voicing',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Voicing'),
        ),
    ]