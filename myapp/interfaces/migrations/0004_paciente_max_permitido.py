# Generated by Django 2.0.6 on 2018-06-28 01:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interfaces', '0003_preparacion_hora_dia'),
    ]

    operations = [
        migrations.AddField(
            model_name='paciente',
            name='max_permitido',
            field=models.IntegerField(default=0),
        ),
    ]