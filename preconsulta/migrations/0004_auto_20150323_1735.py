# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('preconsulta', '0003_auto_20150323_1735'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='programacree',
            name='usuariobaja',
        ),
        migrations.RemoveField(
            model_name='serviciocree',
            name='usuariobaja',
        ),
    ]
