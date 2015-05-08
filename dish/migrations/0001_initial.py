# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BaseDish',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('item_no', models.IntegerField()),
                ('item_description', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='CookMethod',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('item_no', models.IntegerField()),
                ('item_description', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.TextField(max_length=200)),
                ('price', models.FloatField()),
                ('qty', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('item_no', models.IntegerField()),
                ('item_description', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Meat',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('item_no', models.IntegerField()),
                ('item_description', models.CharField(max_length=100)),
            ],
        ),
    ]
