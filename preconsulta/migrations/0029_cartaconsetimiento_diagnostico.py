# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('preconsulta', '0028_paciente_imprimir'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartaconsetimiento',
            name='diagnostico',
            field=models.TextField(blank=True),
            preserve_default=True,
        ),
    ]
