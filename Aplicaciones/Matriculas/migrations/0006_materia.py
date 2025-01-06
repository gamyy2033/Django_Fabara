# Generated by Django 4.2.4 on 2024-12-08 18:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Matriculas', '0005_carrera'),
    ]

    operations = [
        migrations.CreateModel(
            name='Materia',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('creditos', models.IntegerField()),
                ('ciclo', models.IntegerField()),
                ('horario', models.CharField(max_length=100)),
                ('aula', models.CharField(max_length=100)),
                ('carrera', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Matriculas.carrera')),
            ],
        ),
    ]