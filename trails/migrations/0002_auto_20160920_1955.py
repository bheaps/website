# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-20 19:55
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('trails', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='trail',
            old_name='text',
            new_name='details',
        ),
        migrations.AddField(
            model_name='trail',
            name='directions',
            field=models.TextField(default=datetime.datetime(2016, 9, 20, 19, 55, 18, 250900, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
