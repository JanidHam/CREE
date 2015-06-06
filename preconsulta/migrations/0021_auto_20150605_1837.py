# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('preconsulta', '0020_auto_20150605_1750'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartaconsetimiento',
            old_name='apellidosponsable',
            new_name='apellidosresponsable',
        ),
        migrations.RenameField(
            model_name='cartaconsetimiento',
            old_name='parentesco',
            new_name='parentescoresponsable',
        ),
        migrations.RemoveField(
            model_name='cartaconsetimiento',
            name='calleresponsable',
        ),
        migrations.RemoveField(
            model_name='cartaconsetimiento',
            name='diagnostico',
        ),
        migrations.RemoveField(
            model_name='cartaconsetimiento',
            name='entrecallesresponsable',
        ),
        migrations.RemoveField(
            model_name='cartaconsetimiento',
            name='genero',
        ),
        migrations.RemoveField(
            model_name='cartaconsetimiento',
            name='numerocasaresponsable',
        ),
        migrations.AddField(
            model_name='cartaconsetimiento',
            name='domicilioresponsable',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cartaconsetimiento',
            name='generoresponsable',
            field=models.CharField(max_length=15, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cartaconsetimiento',
            name='telefonoresponsable',
            field=models.CharField(max_length=15, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cartaconsetimiento',
            name='codigopostalresponsable',
            field=models.CharField(max_length=15, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cartaconsetimiento',
            name='edadresponsable',
            field=models.CharField(max_length=15, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cartaconsetimiento',
            name='fechacreacion',
            field=models.DateTimeField(auto_now_add=True),
            preserve_default=True,
        ),
    ]
