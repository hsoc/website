# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-26 15:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0034_auto_20170926_1552'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='title_el',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
