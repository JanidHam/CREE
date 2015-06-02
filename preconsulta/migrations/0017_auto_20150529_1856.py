# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('preconsulta', '0016_auto_20150525_1505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pacientedataenfermeria',
            name='fechacreacion',
            field=models.DateTimeField(auto_now_add=True),
            preserve_default=True,
        ),
    ]
