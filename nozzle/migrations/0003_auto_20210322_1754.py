# Generated by Django 3.1.7 on 2021-03-22 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nozzle', '0002_nozzle_magazine'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nozzle',
            name='Magazine',
        ),
        migrations.AddField(
            model_name='nozzle',
            name='magazine',
            field=models.ManyToManyField(to='nozzle.Magazine'),
        ),
    ]
