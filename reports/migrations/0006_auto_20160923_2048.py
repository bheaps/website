# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-23 20:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0005_auto_20160922_1846'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participant',
            name='report',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reports.Reports'),
        ),
    ]