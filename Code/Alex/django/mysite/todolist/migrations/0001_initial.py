# Generated by Django 3.0.2 on 2020-03-04 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ToDoList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('to_do_item', models.CharField(max_length=200)),
                ('priority', models.TextField()),
            ],
        ),
    ]
