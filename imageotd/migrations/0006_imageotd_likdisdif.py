# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-11-02 01:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imageotd', '0005_auto_20161030_1659'),
    ]

    operations = [
        migrations.AddField(
            model_name='imageotd',
            name='likdisdif',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
