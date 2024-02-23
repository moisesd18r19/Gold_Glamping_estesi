# Generated by Django 4.2.7 on 2024-02-16 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservas', '0004_alter_reserva_cliente'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reserva',
            old_name='coder',
            new_name='codigo_reserva',
        ),
        migrations.AddField(
            model_name='reserva',
            name='estado',
            field=models.CharField(default='Reservado', max_length=30),
        ),
    ]