# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('preconsulta', '0023_auto_20150609_1501'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicioexpediente',
            name='clue',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
    ]
