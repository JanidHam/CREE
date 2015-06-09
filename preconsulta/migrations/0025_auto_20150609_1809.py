# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('preconsulta', '0024_servicioexpediente_clue'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicioexpediente',
            name='clue',
            field=models.CharField(max_length=10, blank=True),
            preserve_default=True,
        ),
    ]
