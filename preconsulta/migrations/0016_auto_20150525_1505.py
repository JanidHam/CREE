# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('preconsulta', '0015_auto_20150525_1502'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estudiosocioe1',
            name='fechaestudio',
            field=models.DateField(auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='expediente',
            name='fechacreacion',
            field=models.DateField(auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='hojafrontal',
            name='fechacreacion',
            field=models.DateField(auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='hojaprevaloracion',
            name='fechacreacion',
            field=models.DateField(auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='hojareferencia',
            name='fechacreacion',
            field=models.DateField(auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pacientedataenfermeria',
            name='fechacreacion',
            field=models.DateField(auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tarjetonterapia',
            name='fechaingresoterapias',
            field=models.DateField(auto_now_add=True),
            preserve_default=True,
        ),
    ]
