# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-25 01:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trails', '0003_trail_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='trail',
            name='dislikes',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='trail',
            name='likes',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='comment',
            name='report',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trails.Trail'),
        ),
    ]