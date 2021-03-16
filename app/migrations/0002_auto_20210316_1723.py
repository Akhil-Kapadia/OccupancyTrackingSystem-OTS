# Generated by Django 3.1.6 on 2021-03-16 22:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='occupancy',
            name='CurrentOccupancy',
        ),
        migrations.RemoveField(
            model_name='occupancy',
            name='Date',
        ),
        migrations.RemoveField(
            model_name='occupancy',
            name='Time',
        ),
        migrations.AddField(
            model_name='occupancy',
            name='TimeStamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
