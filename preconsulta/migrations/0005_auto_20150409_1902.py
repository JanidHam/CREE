# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('preconsulta', '0004_estructurafamiliaese1_estadocivil'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estudiosocioe2',
            name='deficit',
            field=models.IntegerField(blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='estudiosocioe2',
            name='excedente',
            field=models.IntegerField(blank=True),
            preserve_default=True,
        ),
    ]
