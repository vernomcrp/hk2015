# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dish', '0004_delete_cookmethod'),
    ]

    operations = [
        migrations.CreateModel(
            name='CookingMethod',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('item_no', models.IntegerField()),
                ('item_description', models.CharField(max_length=100)),
                ('price', models.FloatField(default=0.0)),
            ],
        ),
    ]
