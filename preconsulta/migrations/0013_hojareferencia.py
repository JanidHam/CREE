# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofiles', '0002_auto_20150413_1920'),
        ('preconsulta', '0012_paciente_foto_perfil'),
    ]

    operations = [
        migrations.CreateModel(
            name='HojaReferencia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=80)),
                ('apellidoP', models.CharField(max_length=80)),
                ('apellidoM', models.CharField(max_length=80, blank=True)),
                ('curp', models.CharField(max_length=50)),
                ('edad', models.IntegerField()),
                ('genero', models.IntegerField()),
                ('fechacreacion', models.DateField(auto_now=True)),
                ('diagnostico', models.TextField()),
                ('antecedentes', models.TextField()),
                ('padecimiento_actual', models.TextField()),
                ('tratamientos', models.TextField()),
                ('estudios_realizados', models.TextField()),
                ('usuario', models.ForeignKey(related_name='hojareferencia_usuario', to='userprofiles.UserProfile')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
