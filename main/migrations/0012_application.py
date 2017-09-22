# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-22 13:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_event_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phonenumber', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('name', models.CharField(max_length=100)),
                ('answer_1', models.TextField()),
                ('answer_2', models.TextField()),
                ('answer_3', models.TextField()),
                ('answer_4', models.TextField()),
            ],
        ),
    ]