# Generated by Django 2.2 on 2020-08-12 23:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipoPersona', models.CharField(max_length=30)),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('correo', models.CharField(max_length=30)),
                ('telefono', models.CharField(max_length=30)),
                ('numLibros', models.IntegerField()),
                ('adeudo', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('persona_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='biblioteca.Persona')),
                ('matricula', models.IntegerField()),
            ],
            bases=('biblioteca.persona',),
        ),
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('persona_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='biblioteca.Persona')),
                ('numEmpleado', models.IntegerField()),
            ],
            bases=('biblioteca.persona',),
        ),
    ]
