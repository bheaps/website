# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-10-29 22:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('imageotd', '0002_auto_20161029_2253'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='report',
            new_name='imageotd',
        ),
    ]
