# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-25 02:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trails', '0004_auto_20160925_0149'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='report',
            new_name='trail',
        ),
    ]