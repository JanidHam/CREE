# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('preconsulta', '0017_auto_20150529_1856'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pacientedataenfermeria',
            name='fechacreacion',
            field=models.DateField(auto_now_add=True),
            preserve_default=True,
        ),
    ]
