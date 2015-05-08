# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_auto_20150508_1252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='note',
            field=models.TextField(max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='orderhistory',
            name='price_summary',
            field=models.FloatField(default=0.0),
        ),
    ]
