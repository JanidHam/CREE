# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('preconsulta', '0013_hojareferencia'),
    ]

    operations = [
        migrations.AddField(
            model_name='hojareferencia',
            name='folio',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
