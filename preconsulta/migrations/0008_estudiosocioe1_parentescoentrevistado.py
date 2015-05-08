# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('preconsulta', '0007_estructurafamiliaese1_edad'),
    ]

    operations = [
        migrations.AddField(
            model_name='estudiosocioe1',
            name='parentescoentrevistado',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]
