# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-21 23:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0024_auto_20170421_1544'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='watchlist',
            name='movies',
        ),
        migrations.RemoveField(
            model_name='watchlist',
            name='user',
        ),
        migrations.DeleteModel(
            name='WatchList',
        ),
    ]