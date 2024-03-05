# Generated by Django 4.2.7 on 2024-03-05 14:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('servicios', '0001_initial'),
        ('reservas', '0007_rename_valor_reserva_precio'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reserva_servicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('precio_S', models.IntegerField()),
                ('id_reserva', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='reservas.reserva')),
                ('id_servicio', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='servicios.servicio')),
            ],
        ),
    ]
