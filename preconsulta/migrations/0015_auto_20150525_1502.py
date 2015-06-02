# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('preconsulta', '0014_hojareferencia_folio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='fechacreacion',
            field=models.DateField(auto_now_add=True),
            preserve_default=True,
        ),
    ]
