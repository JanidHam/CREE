# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('preconsulta', '0005_auto_20150323_1909'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartaconsetimiento',
            name='municipio',
        ),
    ]
