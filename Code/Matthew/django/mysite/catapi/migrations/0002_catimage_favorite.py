# Generated by Django 3.0.2 on 2020-02-12 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catapi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='catimage',
            name='favorite',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
