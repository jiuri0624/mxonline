# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-03 22:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_course_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='tag',
            field=models.CharField(default='', max_length=10, verbose_name='标签'),
        ),
    ]