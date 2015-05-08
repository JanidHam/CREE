# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('preconsulta', '0006_auto_20150421_1647'),
    ]

    operations = [
        migrations.AddField(
            model_name='estructurafamiliaese1',
            name='edad',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
