# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-15 21:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reports',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=5000)),
                ('writer', models.CharField(max_length=5000)),
                ('text', models.CharField(max_length=5000)),
            ],
        ),
    ]
