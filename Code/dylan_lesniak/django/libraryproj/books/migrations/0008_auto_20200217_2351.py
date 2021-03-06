# Generated by Django 3.0.2 on 2020-02-17 23:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0007_bookcheckout'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bookcheckout',
            options={'ordering': ['book']},
        ),
        migrations.RemoveField(
            model_name='book',
            name='checked_out_by',
        ),
        migrations.AlterField(
            model_name='bookcheckout',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='checkouts', to='books.Book'),
        ),
    ]
