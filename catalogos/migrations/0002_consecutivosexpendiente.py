# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConsecutivosExpendiente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('consecutivo', models.IntegerField()),
                ('anio_actual', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
