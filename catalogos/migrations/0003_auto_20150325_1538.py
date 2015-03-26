# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogos', '0002_consecutivosexpendiente'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ConsecutivosExpendiente',
            new_name='ConsecutivoExpendiente',
        ),
    ]
