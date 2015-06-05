# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogos', '0004_mensajescartaconsentimiento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mensajescartaconsentimiento',
            name='mensaje',
            field=models.TextField(),
            preserve_default=True,
        ),
    ]
