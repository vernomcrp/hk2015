# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='note',
            field=models.TextField(default=None, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='orderhistory',
            name='price_summary',
            field=models.FloatField(default=0.0),
            preserve_default=False,
        ),
    ]
