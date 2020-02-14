# Generated by Django 3.0.2 on 2020-02-13 23:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urlshortener', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shortener',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=6)),
                ('url', models.CharField(max_length=2048)),
            ],
        ),
        migrations.DeleteModel(
            name='PostType',
        ),
    ]
