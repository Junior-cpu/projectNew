# Generated by Django 3.1.7 on 2021-03-24 20:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nozzle', '0006_machine'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loc', models.CharField(max_length=1)),
            ],
        ),
        migrations.RemoveField(
            model_name='machine',
            name='nozzle',
        ),
        migrations.RemoveField(
            model_name='maquina',
            name='loc_1',
        ),
        migrations.RemoveField(
            model_name='maquina',
            name='loc_2',
        ),
        migrations.RemoveField(
            model_name='maquina',
            name='loc_3',
        ),
        migrations.RemoveField(
            model_name='maquina',
            name='loc_4',
        ),
        migrations.AddField(
            model_name='machine',
            name='maquina',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='nozzle.maquina'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='machine',
            name='loc',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='nozzle.location'),
            preserve_default=False,
        ),
    ]