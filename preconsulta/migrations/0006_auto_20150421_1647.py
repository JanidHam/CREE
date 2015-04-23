# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogos', '0001_initial'),
        ('preconsulta', '0005_auto_20150416_1653'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProgramaExpediente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_active', models.BooleanField(default=True)),
                ('fechaBaja', models.DateField(blank=True)),
                ('expediente', models.ForeignKey(to='preconsulta.Expediente')),
                ('hojaPrevaloracion', models.ForeignKey(to='preconsulta.HojaPrevaloracion')),
                ('programa', models.ForeignKey(to='catalogos.ProgramaCree')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='expediente',
            name='programas',
            field=models.ManyToManyField(to='catalogos.ProgramaCree', through='preconsulta.ProgramaExpediente'),
            preserve_default=True,
        ),
    ]
