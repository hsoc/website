# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-15 13:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_auto_20170915_1253'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='image',
            field=models.ImageField(default='main/static/main/logo.png', max_length=250, upload_to='main/static/main/uploads/'),
        ),
    ]
