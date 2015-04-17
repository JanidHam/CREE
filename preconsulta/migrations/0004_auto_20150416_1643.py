# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('preconsulta', '0003_remove_estudiosocioe2_usuariocreacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estudiosocioe1',
            name='motivoclasificacion',
            field=models.TextField(max_length=200, blank=True),
            preserve_default=True,
        ),
    ]
