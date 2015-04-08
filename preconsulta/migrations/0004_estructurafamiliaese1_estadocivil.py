# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('preconsulta', '0003_auto_20150330_1626'),
    ]

    operations = [
        migrations.AddField(
            model_name='estructurafamiliaese1',
            name='estadocivil',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]
