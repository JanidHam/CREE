# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogos', '0004_ingresosegresos'),
        ('preconsulta', '0002_auto_20150327_1708'),
    ]

    operations = [
        migrations.CreateModel(
            name='EstudioSocioE2IngresosServicios',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('monto', models.IntegerField()),
                ('estudio', models.ForeignKey(to='preconsulta.EstudioSocioE2')),
                ('ingreso_egreso', models.ForeignKey(to='catalogos.IngresosEgresos')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='estudiosocioe2',
            name='ingresos_egresos',
            field=models.ManyToManyField(to='catalogos.IngresosEgresos', through='preconsulta.EstudioSocioE2IngresosServicios'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='hojaprevaloracion',
            name='diagnosticonosologico2',
            field=models.TextField(blank=True),
            preserve_default=True,
        ),
    ]
