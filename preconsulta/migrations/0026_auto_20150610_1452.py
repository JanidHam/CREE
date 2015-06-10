# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('preconsulta', '0025_auto_20150609_1809'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='servicioexpediente',
            name='clue',
        ),
        migrations.AddField(
            model_name='expediente',
            name='clue',
            field=models.CharField(max_length=10, blank=True),
            preserve_default=True,
        ),
    ]
