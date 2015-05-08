# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
        ('dish', '0005_cookingmethod'),
    ]

    operations = [
        migrations.CreateModel(
            name='Additional',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('item_no', models.IntegerField()),
                ('item_description', models.CharField(max_length=100)),
                ('price', models.FloatField(default=0.0)),
            ],
        ),
        migrations.AddField(
            model_name='dish',
            name='order',
            field=models.ForeignKey(default=None, to='order.Order'),
            preserve_default=False,
        ),
    ]
