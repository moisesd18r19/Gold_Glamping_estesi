# Generated by Django 4.2.7 on 2024-03-02 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservas_cabañas', '0003_rename_reservas_cabañas_reserva_cabaña'),
    ]

    operations = [
        migrations.AddField(
            model_name='reserva_cabaña',
            name='precio',
            field=models.IntegerField(null=True),
        ),
    ]
