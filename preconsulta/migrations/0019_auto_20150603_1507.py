# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('preconsulta', '0018_auto_20150601_1609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estructurafamiliaese1',
            name='estudiose',
            field=models.ForeignKey(related_name='estructurafamiliar_estudiosocioe1', to='preconsulta.EstudioSocioE1'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='estudiosocioe2',
            name='estudiose',
            field=models.ForeignKey(related_name='estudiosocioe2_estudiosocioe1', to='preconsulta.EstudioSocioE1'),
            preserve_default=True,
        ),
    ]
