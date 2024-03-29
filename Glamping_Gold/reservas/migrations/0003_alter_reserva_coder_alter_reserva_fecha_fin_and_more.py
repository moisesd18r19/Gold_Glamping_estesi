# Generated by Django 4.2.7 on 2024-02-01 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservas', '0002_reserva_coder_alter_reserva_cliente_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva',
            name='coder',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='fecha_fin',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='fecha_inicio',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='fecha_reserva',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='valor',
            field=models.IntegerField(),
        ),
    ]
