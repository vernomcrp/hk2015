# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dish', '0003_auto_20150508_0631'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CookMethod',
        ),
    ]
