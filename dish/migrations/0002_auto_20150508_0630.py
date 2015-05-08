# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dish', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='basedish',
            name='price',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='cookmethod',
            name='price',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='ingredient',
            name='price',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='meat',
            name='price',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='dish',
            name='created_at',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='dish',
            name='price',
            field=models.FloatField(default=0.0),
        ),
    ]
