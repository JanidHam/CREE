# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('preconsulta', '0019_auto_20150603_1507'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estudiosocioe1',
            name='clasificacion',
            field=models.ForeignKey(related_name='estudiosocioe1_clasificacion', to='catalogos.ClasificacionEconomica'),
            preserve_default=True,
        ),
    ]
