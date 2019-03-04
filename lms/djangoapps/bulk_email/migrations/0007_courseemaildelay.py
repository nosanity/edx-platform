# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bulk_email', '0006_course_mode_targets'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseEmailDelay',
            fields=[
                ('course_email', models.OneToOneField(related_name='delay', primary_key=True, serialize=False, to='bulk_email.CourseEmail')),
                ('when', models.DateTimeField()),
            ],
        ),
    ]
