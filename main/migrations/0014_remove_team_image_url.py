# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-14 13:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_auto_20170914_1303'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='image_url',
        ),
    ]
