# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dish', '0002_auto_20150508_0630'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
