# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofiles', '0002_auto_20150413_1920'),
        ('preconsulta', '0009_paciente_localidad'),
    ]

    operations = [
        migrations.CreateModel(
            name='PacienteDataEnfermeria',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('edad', models.IntegerField()),
                ('peso', models.CharField(max_length=10)),
                ('talla', models.CharField(max_length=20)),
                ('f_c', models.CharField(max_length=20)),
                ('t_a', models.CharField(max_length=20)),
                ('glucosa', models.CharField(max_length=20)),
                ('cintura', models.CharField(max_length=20)),
                ('fechacreacion', models.DateField(auto_now=True)),
                ('mensaje_informativo', models.CharField(max_length=255)),
                ('enfermera', models.ForeignKey(related_name='dataenfermeria_usuario', to='userprofiles.UserProfile')),
                ('paciente', models.ForeignKey(related_name='dataenfermeria_paciente', to='preconsulta.Paciente')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
