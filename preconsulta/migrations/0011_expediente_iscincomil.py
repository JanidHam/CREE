# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('preconsulta', '0010_pacientedataenfermeria'),
    ]

    operations = [
        migrations.AddField(
            model_name='expediente',
            name='iscincomil',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
