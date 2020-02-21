# Generated by Django 3.0.2 on 2020-02-14 21:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='library.Author'),
        ),
        migrations.CreateModel(
            name='Book_checkout',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('checout_date', models.DateTimeField()),
                ('checkin_date', models.DateField(null=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='library.Books')),
                ('checked_out_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]