# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('preconsulta', '0008_estudiosocioe1_parentescoentrevistado'),
    ]

    operations = [
        migrations.AddField(
            model_name='paciente',
            name='localidad',
            field=models.CharField(max_length=200, blank=True),
            preserve_default=True,
        ),
    ]
