# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('preconsulta', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='paciente',
            name='correspondio',
            field=models.NullBooleanField(),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='paciente',
            name='escolaridad',
            field=models.ForeignKey(related_name='paciente_escolaridad', default=1, to='preconsulta.Escolaridad'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='paciente',
            name='ocupacion',
            field=models.ForeignKey(related_name='paciente_ocupacion', default=1, to='preconsulta.Ocupacion'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='paciente',
            name='referidopor',
            field=models.ForeignKey(related_name='paciente_referidopor', default=1, to='preconsulta.Referidopor'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='hojaprevaloracion',
            name='escolaridad',
            field=models.ForeignKey(related_name='hojaprevaloracion_escolaridad', to='preconsulta.Escolaridad'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='hojaprevaloracion',
            name='ocupacion',
            field=models.ForeignKey(related_name='hojaprevaloracion_ocupacion', to='preconsulta.Ocupacion'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='hojaprevaloracion',
            name='referidopor',
            field=models.ForeignKey(related_name='hojaprevaloracion_referidopor', to='preconsulta.Referidopor'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='paciente',
            name='estadoprocedente',
            field=models.ForeignKey(related_name='paciente_estadoprocedente', to='preconsulta.Estado'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='paciente',
            name='municipio',
            field=models.ForeignKey(related_name='paciente_municipio', to='preconsulta.Municipio'),
            preserve_default=True,
        ),
    ]
