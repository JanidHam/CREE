# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BarreraArquitectonicaVivienda',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('barrera', models.CharField(max_length=255)),
                ('tipo', models.CharField(max_length=15)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
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
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ClasificacionEconomica',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('clasificacion', models.CharField(max_length=20)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ComponenteVivienda',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('componente', models.CharField(max_length=255)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ConstruccionVivienda',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('componente', models.CharField(max_length=255)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Escolaridad',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.CharField(max_length=255)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.CharField(max_length=255)),
                ('is_active', models.BooleanField(default=True)),
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
                ('escolaridad', models.ForeignKey(related_name='estructurafamiliar_escolaridad', to='preconsulta.Escolaridad')),
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
                ('clasificacion', models.ForeignKey(related_name='estudiosocioe1_estadoprocedente', to='preconsulta.ClasificacionEconomica')),
                ('escolaridad', models.ForeignKey(related_name='estudiosocioe1_escolaridad', to='preconsulta.Escolaridad')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EstudioSocioE2',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('deficit', models.IntegerField()),
                ('excedente', models.IntegerField()),
                ('datosignificativo', models.TextField()),
                ('diagnosticoplansocial', models.TextField()),
                ('barreravivienda', models.ManyToManyField(related_name='estudiosocioe2_barrera', to='preconsulta.BarreraArquitectonicaVivienda')),
                ('componentevivienda', models.ManyToManyField(related_name='estudiosocioe2_componente', to='preconsulta.ComponenteVivienda')),
                ('construccionvivienda', models.ManyToManyField(related_name='estudiosocioe2_construccion', to='preconsulta.ConstruccionVivienda')),
                ('estudiose', models.ForeignKey(related_name='estudiosocioe2_estadoprocedente', to='preconsulta.EstudioSocioE1')),
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
                ('fechaalta', models.DateField(auto_now=True)),
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
                ('psicologia', models.TextField()),
                ('diagnosticonosologico2', models.TextField()),
                ('canalizacion', models.TextField()),
                ('fechacreacion', models.DateField(auto_now=True)),
                ('edad', models.IntegerField()),
                ('doctor', models.ForeignKey(related_name='hojaprevaloracion_doctor', to='userprofiles.UserProfile')),
                ('escolaridad', models.ForeignKey(related_name='paciente_escolaridad', to='preconsulta.Escolaridad')),
                ('expediente', models.ForeignKey(related_name='hojaprevaloracion_expediente', to='preconsulta.Expediente')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MotivoEstudioSE',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('motivoestudio', models.CharField(max_length=255)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Municipio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.CharField(max_length=255)),
                ('estado', models.ForeignKey(related_name='estado_municipio', to='preconsulta.Estado')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Ocupacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.CharField(max_length=255)),
                ('is_active', models.BooleanField(default=True)),
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
                ('telefonocasa', models.IntegerField(blank=True)),
                ('telefonocelular', models.IntegerField(blank=True)),
                ('calle', models.CharField(max_length=200)),
                ('entrecalles', models.CharField(max_length=200, blank=True)),
                ('colonia', models.CharField(max_length=200)),
                ('numerocasa', models.CharField(max_length=20, blank=True)),
                ('codigopostal', models.IntegerField()),
                ('creadopor', models.CharField(max_length=255)),
                ('fechacreacion', models.DateField(auto_now=True)),
                ('estadoprocedente', models.ForeignKey(related_name='paciente_estadoprocedente', blank=True, to='preconsulta.Estado')),
                ('municipio', models.ForeignKey(related_name='paciente_municipio', blank=True, to='preconsulta.Municipio')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProgramaCree',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('programa', models.CharField(max_length=150)),
                ('is_active', models.BooleanField(default=True)),
                ('fechabaja', models.DateField(auto_now=True)),
                ('usuariobaja', models.ForeignKey(related_name='programa_usuario', to='userprofiles.UserProfile')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Referidopor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.CharField(max_length=255)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ServicioCree',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('servicio', models.CharField(max_length=150)),
                ('is_active', models.BooleanField(default=True)),
                ('fechabaja', models.DateField(auto_now=True)),
                ('usuariobaja', models.ForeignKey(related_name='serivicio_usuario', to='userprofiles.UserProfile')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ServicioVivienda',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('servicio', models.CharField(max_length=255)),
                ('is_active', models.BooleanField(default=True)),
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
        migrations.CreateModel(
            name='TenenciaVivienda',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tenencia', models.CharField(max_length=255)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TipoVivienda',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('vivienda', models.CharField(max_length=255)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='hojaprevaloracion',
            name='ocupacion',
            field=models.ForeignKey(related_name='paciente_ocupacion', to='preconsulta.Ocupacion'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='hojaprevaloracion',
            name='psicologo',
            field=models.ForeignKey(related_name='hojaprevaloracion_psicologo', to='userprofiles.UserProfile'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='hojaprevaloracion',
            name='referidopor',
            field=models.ForeignKey(related_name='paciente_referidopor', to='preconsulta.Referidopor'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='historiaclinica',
            name='ocupacion',
            field=models.ForeignKey(related_name='historiaclinica_servicio', to='preconsulta.ServicioCree'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='expediente',
            name='paciente',
            field=models.ForeignKey(related_name='expediente_paciente', to='preconsulta.Paciente'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='estudiosocioe2',
            name='serviciovivienda',
            field=models.ManyToManyField(related_name='estudiosocioe2_servicio', to='preconsulta.ServicioVivienda'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='estudiosocioe2',
            name='tenenciavivienda',
            field=models.ManyToManyField(related_name='estudiosocioe2_tenencia', to='preconsulta.TenenciaVivienda'),
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
            field=models.ForeignKey(related_name='estudiosocioe2_vivienda', to='preconsulta.TipoVivienda'),
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
            field=models.ForeignKey(related_name='estudiosocioe1_escolaridad', to='preconsulta.MotivoEstudioSE'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='estudiosocioe1',
            name='ocupacion',
            field=models.ForeignKey(related_name='estudiosocioe1_ocupacion', to='preconsulta.Ocupacion'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='estudiosocioe1',
            name='servicio',
            field=models.ForeignKey(related_name='estudiosocioe1_escolaridad', to='preconsulta.ServicioCree'),
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
            field=models.ForeignKey(related_name='estructurafamiliar_ocupacion', to='preconsulta.Ocupacion'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cartaconsetimiento',
            name='estadoprocedente',
            field=models.ForeignKey(related_name='cartaconsentimiento_estadoprocedente', to='preconsulta.Estado'),
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
            field=models.ForeignKey(related_name='cartaconsentimiento_municipio', to='preconsulta.Municipio'),
            preserve_default=True,
        ),
    ]
