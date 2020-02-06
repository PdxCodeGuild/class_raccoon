# Generated by Django 3.0.2 on 2020-02-05 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('birthday', models.DateTimeField()),
                ('phone_number', models.CharField(max_length=12)),
                ('is_cell', models.BooleanField(default=True)),
            ],
        ),
    ]
