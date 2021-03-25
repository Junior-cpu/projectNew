# Generated by Django 3.1.7 on 2021-03-24 21:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nozzle', '0007_auto_20210324_1701'),
    ]

    operations = [
        migrations.CreateModel(
            name='Linha',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('linha', models.CharField(max_length=2)),
            ],
        ),
        migrations.AddField(
            model_name='machine',
            name='linha',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='nozzle.linha'),
            preserve_default=False,
        ),
    ]