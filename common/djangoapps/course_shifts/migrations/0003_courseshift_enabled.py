# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-02-21 12:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_shifts', '0002_courseshift_studio_version'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseshift',
            name='enabled',
            field=models.BooleanField(default=False, verbose_name=b'Course shifts are enabled for course'),
        ),
    ]
