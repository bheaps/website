# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-10-23 20:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0010_reports_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reports',
            name='image',
            field=models.FileField(blank=True, upload_to='documents/%Y/%m/%d'),
        ),
    ]
