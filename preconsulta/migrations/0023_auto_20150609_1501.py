# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogos', '0006_seguridadsocial'),
        ('preconsulta', '0022_auto_20150605_1850'),
    ]

    operations = [
        migrations.AddField(
            model_name='estudiosocioe1',
            name='seguridad_social',
            field=models.ForeignKey(related_name='estudiosocioe1_seguridadsocial', default=1, to='catalogos.SeguridadSocial'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cartaconsetimiento',
            name='fechacreacion',
            field=models.DateField(auto_now_add=True),
            preserve_default=True,
        ),
    ]
