# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('preconsulta', '0026_auto_20150610_1452'),
    ]

    operations = [
        migrations.AddField(
            model_name='paciente',
            name='fechavisita',
            field=models.DateField(default=datetime.datetime(2015, 6, 12, 20, 5, 29, 288442, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='historiaclinica',
            name='fechacreacion',
            field=models.DateTimeField(auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tarjetonterapia',
            name='fechacreacion',
            field=models.DateTimeField(auto_now_add=True),
            preserve_default=True,
        ),
    ]
