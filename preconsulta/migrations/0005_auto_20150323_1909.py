# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('preconsulta', '0004_auto_20150323_1735'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BarreraArquitectonicaVivienda',
        ),
        migrations.DeleteModel(
            name='ComponenteVivienda',
        ),
        migrations.DeleteModel(
            name='ConstruccionVivienda',
        ),
        migrations.RemoveField(
            model_name='municipio',
            name='estado',
        ),
        migrations.DeleteModel(
            name='ProgramaCree',
        ),
        migrations.DeleteModel(
            name='ServicioVivienda',
        ),
        migrations.DeleteModel(
            name='TenenciaVivienda',
        ),
        migrations.AlterField(
            model_name='cartaconsetimiento',
            name='estadoprocedente',
            field=models.ForeignKey(related_name='cartaconsentimiento_estadoprocedente', to='catalogos.Estado'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cartaconsetimiento',
            name='municipio',
            field=models.ForeignKey(related_name='cartaconsentimiento_municipio', to='catalogos.Municipio'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='estructurafamiliaese1',
            name='escolaridad',
            field=models.ForeignKey(related_name='estructurafamiliar_escolaridad', to='catalogos.Escolaridad'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='estructurafamiliaese1',
            name='ocupacion',
            field=models.ForeignKey(related_name='estructurafamiliar_ocupacion', to='catalogos.Ocupacion'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='estudiosocioe1',
            name='clasificacion',
            field=models.ForeignKey(related_name='estudiosocioe1_estadoprocedente', to='catalogos.ClasificacionEconomica'),
            preserve_default=True,
        ),
        migrations.DeleteModel(
            name='ClasificacionEconomica',
        ),
        migrations.AlterField(
            model_name='estudiosocioe1',
            name='escolaridad',
            field=models.ForeignKey(related_name='estudiosocioe1_escolaridad', to='catalogos.Escolaridad'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='estudiosocioe1',
            name='motivoestudio',
            field=models.ForeignKey(related_name='estudiosocioe1_escolaridad', to='catalogos.MotivoEstudioSE'),
            preserve_default=True,
        ),
        migrations.DeleteModel(
            name='MotivoEstudioSE',
        ),
        migrations.AlterField(
            model_name='estudiosocioe1',
            name='ocupacion',
            field=models.ForeignKey(related_name='estudiosocioe1_ocupacion', to='catalogos.Ocupacion'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='estudiosocioe1',
            name='servicio',
            field=models.ForeignKey(related_name='estudiosocioe1_escolaridad', to='catalogos.ServicioCree'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='estudiosocioe2',
            name='barreravivienda',
            field=models.ManyToManyField(related_name='estudiosocioe2_barrera', to='catalogos.BarreraArquitectonicaVivienda'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='estudiosocioe2',
            name='componentevivienda',
            field=models.ManyToManyField(related_name='estudiosocioe2_componente', to='catalogos.ComponenteVivienda'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='estudiosocioe2',
            name='construccionvivienda',
            field=models.ManyToManyField(related_name='estudiosocioe2_construccion', to='catalogos.ConstruccionVivienda'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='estudiosocioe2',
            name='serviciovivienda',
            field=models.ManyToManyField(related_name='estudiosocioe2_servicio', to='catalogos.ServicioVivienda'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='estudiosocioe2',
            name='tenenciavivienda',
            field=models.ManyToManyField(related_name='estudiosocioe2_tenencia', to='catalogos.TenenciaVivienda'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='estudiosocioe2',
            name='vivienda',
            field=models.ForeignKey(related_name='estudiosocioe2_vivienda', to='catalogos.TipoVivienda'),
            preserve_default=True,
        ),
        migrations.DeleteModel(
            name='TipoVivienda',
        ),
        migrations.AlterField(
            model_name='expediente',
            name='fechaalta',
            field=models.DateField(blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='historiaclinica',
            name='ocupacion',
            field=models.ForeignKey(related_name='historiaclinica_servicio', to='catalogos.ServicioCree'),
            preserve_default=True,
        ),
        migrations.DeleteModel(
            name='ServicioCree',
        ),
        migrations.AlterField(
            model_name='hojaprevaloracion',
            name='escolaridad',
            field=models.ForeignKey(related_name='hojaprevaloracion_escolaridad', to='catalogos.Escolaridad'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='hojaprevaloracion',
            name='ocupacion',
            field=models.ForeignKey(related_name='hojaprevaloracion_ocupacion', to='catalogos.Ocupacion'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='hojaprevaloracion',
            name='psicologia',
            field=models.TextField(blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='hojaprevaloracion',
            name='referidopor',
            field=models.ForeignKey(related_name='hojaprevaloracion_referidopor', to='catalogos.Referidopor'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='paciente',
            name='escolaridad',
            field=models.ForeignKey(related_name='paciente_escolaridad', to='catalogos.Escolaridad'),
            preserve_default=True,
        ),
        migrations.DeleteModel(
            name='Escolaridad',
        ),
        migrations.AlterField(
            model_name='paciente',
            name='estadoprocedente',
            field=models.ForeignKey(related_name='paciente_estadoprocedente', to='catalogos.Estado'),
            preserve_default=True,
        ),
        migrations.DeleteModel(
            name='Estado',
        ),
        migrations.AlterField(
            model_name='paciente',
            name='municipio',
            field=models.ForeignKey(related_name='paciente_municipio', to='catalogos.Municipio'),
            preserve_default=True,
        ),
        migrations.DeleteModel(
            name='Municipio',
        ),
        migrations.AlterField(
            model_name='paciente',
            name='ocupacion',
            field=models.ForeignKey(related_name='paciente_ocupacion', to='catalogos.Ocupacion'),
            preserve_default=True,
        ),
        migrations.DeleteModel(
            name='Ocupacion',
        ),
        migrations.AlterField(
            model_name='paciente',
            name='referidopor',
            field=models.ForeignKey(related_name='paciente_referidopor', to='catalogos.Referidopor'),
            preserve_default=True,
        ),
        migrations.DeleteModel(
            name='Referidopor',
        ),
    ]
