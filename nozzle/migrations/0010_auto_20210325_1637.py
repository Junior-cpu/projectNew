# Generated by Django 3.1.7 on 2021-03-25 19:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nozzle', '0009_auto_20210324_1911'),
    ]

    operations = [
        migrations.RenameField(
            model_name='machine',
            old_name='linhas',
            new_name='linha',
        ),
        migrations.RemoveField(
            model_name='machine',
            name='magazine',
        ),
        migrations.AddField(
            model_name='location',
            name='magazine',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='nozzle.magazine'),
            preserve_default=False,
        ),
    ]