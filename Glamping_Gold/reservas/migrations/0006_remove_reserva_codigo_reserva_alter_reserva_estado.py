# Generated by Django 4.2.7 on 2024-02-17 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservas', '0005_rename_coder_reserva_codigo_reserva_reserva_estado'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reserva',
            name='codigo_reserva',
        ),
        migrations.AlterField(
            model_name='reserva',
            name='estado',
            field=models.CharField(default='Reservado', max_length=20),
        ),
    ]
