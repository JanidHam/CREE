# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('preconsulta', '0027_auto_20150612_1505'),
    ]

    operations = [
        migrations.AddField(
            model_name='paciente',
            name='imprimir',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
