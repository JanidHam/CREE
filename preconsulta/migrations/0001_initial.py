# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogos', '__first__'),
        ('userprofiles', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartaConsetimiento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('edad', models.IntegerField()),
                ('fechacreacion', models.DateTimeField(auto_now=True)),
                ('diagnostico', models.TextField()),
                ('nombreresponsable', models.CharField(max_length=150)),
                ('apellidosponsable', models.CharField(max_length=150)),
                ('edadresponsable', models.IntegerField()),
                ('genero', models.IntegerField()),
                ('parentesco', models.CharField(max_length=50)),
                ('calleresponsable', models.CharField(max_length=200)),
                ('entrecallesresponsable', models.CharField(max_length=200)),
                ('coloniaresponsable', models.CharField(max_length=200)),
                ('numerocasaresponsable', models.CharField(max_length=20)),
                ('codigopostalresponsable', models.IntegerField()),
                ('calle', models.CharField(max_length=200)),
                ('entrecalles', models.CharField(max_length=200)),
                ('colonia', models.CharField(max_length=200)),
                ('numerocasa', models.CharField(max_length=20)),
                ('codigopostal', models.IntegerField()),
                ('doctor', models.ForeignKey(related_name='cartaconsentimiento_doctor', to='userprofiles.UserProfile')),
                ('estadoprocedente', models.ForeignKey(related_name='cartaconsentimiento_estadoprocedente', to='catalogos.Estado')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EstructuraFamiliaESE1',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombrefamiliar', models.CharField(max_length=200)),
                ('apellidosfamiliar', models.CharField(max_length=200)),
                ('parentesco', models.CharField(max_length=20)),
                ('estadocivil', models.CharField(max_length=20)),
                ('escolaridad', models.ForeignKey(related_name='estructurafamiliar_escolaridad', to='catalogos.Escolaridad')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EstudioSocioE1',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('edad', models.IntegerField()),
                ('estadocivil', models.CharField(max_length=20)),
                ('fechaestudio', models.DateField(auto_now=True)),
                ('consultorio', models.IntegerField()),
                ('nombreentevistado', models.CharField(max_length=200)),
                ('apellidosentevistado', models.CharField(max_length=200)),
                ('calle', models.CharField(max_length=200)),
                ('entrecalles', models.CharField(max_length=200)),
                ('colonia', models.CharField(max_length=200)),
                ('numerocasa', models.CharField(max_length=20)),
                ('codigopostal', models.IntegerField()),
                ('motivoclasificacion', models.CharField(max_length=200, blank=True)),
                ('clasificacion', models.ForeignKey(related_name='estudiosocioe1_estadoprocedente', to='catalogos.ClasificacionEconomica')),
                ('escolaridad', models.ForeignKey(related_name='estudiosocioe1_escolaridad', to='catalogos.Escolaridad')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EstudioSocioE2',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('deficit', models.IntegerField(blank=True)),
                ('excedente', models.IntegerField(blank=True)),
                ('datosignificativo', models.TextField()),
                ('diagnosticoplansocial', models.TextField()),
                ('cantidadbanios', models.IntegerField()),
                ('cantidadrecamaras', models.IntegerField()),
                ('barreravivienda', models.ManyToManyField(related_name='estudiosocioe2_barrera', to='catalogos.BarreraArquitectonicaVivienda')),
                ('componentevivienda', models.ManyToManyField(related_name='estudiosocioe2_componente', to='catalogos.ComponenteVivienda')),
                ('construccionvivienda', models.ManyToManyField(related_name='estudiosocioe2_construccion', to='catalogos.ConstruccionVivienda')),
                ('estudiose', models.ForeignKey(related_name='estudiosocioe2_estadoprocedente', to='preconsulta.EstudioSocioE1')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EstudioSocioE2IngresosEgresos',
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
        migrations.CreateModel(
            name='Expediente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('claveexpediente', models.CharField(unique=True, max_length=50)),
                ('is_active', models.BooleanField(default=True)),
                ('fechacreacion', models.DateField(auto_now=True)),
                ('fechaalta', models.DateField(blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='HistoriaClinica',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('edad', models.IntegerField()),
                ('fechacreacion', models.DateTimeField(auto_now=True)),
                ('interrogatorio', models.IntegerField()),
                ('motivoconsulta', models.TextField()),
                ('AHF', models.TextField()),
                ('APNP', models.TextField()),
                ('DPM', models.TextField()),
                ('APP', models.TextField()),
                ('PA', models.TextField()),
                ('EF', models.TextField()),
                ('estudiosdiagnostico', models.TextField()),
                ('diagnosticonosologico', models.TextField()),
                ('pronostico', models.TextField()),
                ('plantratamiento', models.TextField()),
                ('doctor', models.ForeignKey(related_name='historiaclinica_doctor', to='userprofiles.UserProfile')),
                ('expediente', models.ForeignKey(related_name='historiaclinica_expediente', to='preconsulta.Expediente')),
                ('ocupacion', models.ForeignKey(related_name='historiaclinica_servicio', to='catalogos.ServicioCree')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='HojaFrontal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('edad', models.IntegerField()),
                ('fechacreacion', models.DateField(auto_now=True)),
                ('diagnosticonosologico', models.TextField()),
                ('expediente', models.ForeignKey(related_name='hojafrontal_expediente', to='preconsulta.Expediente')),
                ('usuario', models.ForeignKey(related_name='hojafrontal_usuario', to='userprofiles.UserProfile')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='HojaPrevaloracion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('motivoconsulta', models.TextField()),
                ('diagnosticonosologico', models.TextField()),
                ('psicologia', models.TextField(blank=True)),
                ('diagnosticonosologico2', models.TextField(blank=True)),
                ('canalizacion', models.TextField()),
                ('fechacreacion', models.DateField(auto_now=True)),
                ('edad', models.IntegerField()),
                ('doctor', models.ForeignKey(related_name='hojaprevaloracion_doctor', to='userprofiles.UserProfile')),
                ('escolaridad', models.ForeignKey(related_name='hojaprevaloracion_escolaridad', to='catalogos.Escolaridad')),
                ('expediente', models.ForeignKey(related_name='hojaprevaloracion_expediente', to='preconsulta.Expediente')),
                ('ocupacion', models.ForeignKey(related_name='hojaprevaloracion_ocupacion', to='catalogos.Ocupacion')),
                ('psicologo', models.ForeignKey(related_name='hojaprevaloracion_psicologo', to='userprofiles.UserProfile')),
                ('referidopor', models.ForeignKey(related_name='hojaprevaloracion_referidopor', to='catalogos.Referidopor')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=80)),
                ('apellidoP', models.CharField(max_length=80)),
                ('apellidoM', models.CharField(max_length=80, blank=True)),
                ('curp', models.CharField(unique=True, max_length=50)),
                ('edad', models.IntegerField()),
                ('genero', models.IntegerField()),
                ('fechanacimiento', models.DateField()),
                ('telefonocasa', models.CharField(max_length=20, blank=True)),
                ('telefonocelular', models.CharField(max_length=20, blank=True)),
                ('calle', models.CharField(max_length=200)),
                ('entrecalles', models.CharField(max_length=200, blank=True)),
                ('colonia', models.CharField(max_length=200)),
                ('numerocasa', models.CharField(max_length=20, blank=True)),
                ('codigopostal', models.IntegerField()),
                ('correspondio', models.NullBooleanField()),
                ('creadopor', models.CharField(max_length=255)),
                ('fechacreacion', models.DateField(auto_now=True)),
                ('escolaridad', models.ForeignKey(related_name='paciente_escolaridad', to='catalogos.Escolaridad')),
                ('estadoprocedente', models.ForeignKey(related_name='paciente_estadoprocedente', to='catalogos.Estado')),
                ('municipio', models.ForeignKey(related_name='paciente_municipio', to='catalogos.Municipio')),
                ('ocupacion', models.ForeignKey(related_name='paciente_ocupacion', to='catalogos.Ocupacion')),
                ('referidopor', models.ForeignKey(related_name='paciente_referidopor', to='catalogos.Referidopor')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
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
        migrations.CreateModel(
            name='TarjetonTerapia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('edad', models.IntegerField()),
                ('fechacreacion', models.DateTimeField(auto_now=True)),
                ('fechaingresoterapias', models.DateField(auto_now=True)),
                ('diagnostico', models.TextField()),
                ('indicaciones', models.TextField()),
                ('doctor', models.ForeignKey(related_name='tarjetonterapia_doctor', to='userprofiles.UserProfile')),
                ('expediente', models.ForeignKey(related_name='tarjetonterapia_expediente', to='preconsulta.Expediente')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='expediente',
            name='paciente',
            field=models.ForeignKey(related_name='expediente_paciente', to='preconsulta.Paciente'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='expediente',
            name='servicios',
            field=models.ManyToManyField(to='catalogos.ServicioCree', through='preconsulta.ServicioExpediente'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='estudiosocioe2',
            name='ingresos_egresos',
            field=models.ManyToManyField(to='catalogos.IngresosEgresos', through='preconsulta.EstudioSocioE2IngresosEgresos'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='estudiosocioe2',
            name='serviciovivienda',
            field=models.ManyToManyField(related_name='estudiosocioe2_servicio', to='catalogos.ServicioVivienda'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='estudiosocioe2',
            name='tenenciavivienda',
            field=models.ManyToManyField(related_name='estudiosocioe2_tenencia', to='catalogos.TenenciaVivienda'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='estudiosocioe2',
            name='usuariocreacion',
            field=models.ForeignKey(related_name='estudiosocioe2_usuario', to='userprofiles.UserProfile'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='estudiosocioe2',
            name='vivienda',
            field=models.ForeignKey(related_name='estudiosocioe2_vivienda', to='catalogos.TipoVivienda'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='estudiosocioe1',
            name='expediente',
            field=models.ForeignKey(related_name='estudiosocioe1_expediente', to='preconsulta.Expediente'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='estudiosocioe1',
            name='motivoestudio',
            field=models.ForeignKey(related_name='estudiosocioe1_escolaridad', to='catalogos.MotivoEstudioSE'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='estudiosocioe1',
            name='ocupacion',
            field=models.ForeignKey(related_name='estudiosocioe1_ocupacion', to='catalogos.Ocupacion'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='estudiosocioe1',
            name='servicio',
            field=models.ForeignKey(related_name='estudiosocioe1_escolaridad', to='catalogos.ServicioCree'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='estudiosocioe1',
            name='usuariocreacion',
            field=models.ForeignKey(related_name='estudiosocioe1_usuario', to='userprofiles.UserProfile'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='estructurafamiliaese1',
            name='estudiose',
            field=models.ForeignKey(related_name='estructurafamiliar_estadoprocedente', to='preconsulta.EstudioSocioE1'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='estructurafamiliaese1',
            name='ocupacion',
            field=models.ForeignKey(related_name='estructurafamiliar_ocupacion', to='catalogos.Ocupacion'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cartaconsetimiento',
            name='expediente',
            field=models.ForeignKey(related_name='cartaconsentimiento_expediente', to='preconsulta.Expediente'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cartaconsetimiento',
            name='municipio',
            field=models.ForeignKey(related_name='cartaconsentimiento_municipio', to='catalogos.Municipio'),
            preserve_default=True,
        ),
    ]
