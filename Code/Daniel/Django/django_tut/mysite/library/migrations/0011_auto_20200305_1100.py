# Generated by Django 3.0.2 on 2020-03-05 19:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0010_auto_20200305_1053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book_checkout',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='records', to='library.Books'),
        ),
        migrations.AlterField(
            model_name='books',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='library.Author'),
        ),
    ]
