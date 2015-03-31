# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogos', '0003_auto_20150325_1538'),
        ('preconsulta', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServicioExpediente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_active', models.BooleanField(default=True)),
                ('fechaBaja', models.DateField(blank=True)),
                ('expediente', models.ForeignKey(to='preconsulta.Expediente')),
                ('hojaPrevaloracion', models.ForeignKey(to='preconsulta.HojaPrevaloracion')),
                ('servicio', models.ForeignKey(to='catalogos.ServicioCree')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='expediente',
            name='servicios',
            field=models.ManyToManyField(to='catalogos.ServicioCree', through='preconsulta.ServicioExpediente'),
            preserve_default=True,
        ),
    ]
