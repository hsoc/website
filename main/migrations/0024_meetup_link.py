# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-15 13:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0023_auto_20170915_1307'),
    ]

    operations = [
        migrations.AddField(
            model_name='meetup',
            name='link',
            field=models.URLField(default='http://okthess.gr/'),
            preserve_default=False,
        ),
    ]
