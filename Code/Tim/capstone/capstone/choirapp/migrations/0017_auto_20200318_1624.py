# Generated by Django 3.0.4 on 2020-03-18 23:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('choirapp', '0016_auto_20200318_1621'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='rehearsal',
            options={},
        ),
        migrations.RenameField(
            model_name='rehearsal',
            old_name='piece',
            new_name='pieces',
        ),
        migrations.RemoveField(
            model_name='rehearsal',
            name='order',
        ),
    ]
