# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofiles', '0002_auto_20150323_1642'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='userame',
            new_name='username',
        ),
    ]
