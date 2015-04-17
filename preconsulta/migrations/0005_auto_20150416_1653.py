# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('preconsulta', '0004_auto_20150416_1643'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estudiosocioe1',
            name='motivoclasificacion',
            field=models.TextField(blank=True),
            preserve_default=True,
        ),
    ]
