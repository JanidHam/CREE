# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('preconsulta', '0021_auto_20150605_1837'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartaconsetimiento',
            name='apellidosresponsable',
            field=models.CharField(max_length=150, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cartaconsetimiento',
            name='coloniaresponsable',
            field=models.CharField(max_length=200, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cartaconsetimiento',
            name='domicilioresponsable',
            field=models.CharField(max_length=255, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cartaconsetimiento',
            name='nombreresponsable',
            field=models.CharField(max_length=150, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cartaconsetimiento',
            name='parentescoresponsable',
            field=models.CharField(max_length=50, blank=True),
            preserve_default=True,
        ),
    ]
