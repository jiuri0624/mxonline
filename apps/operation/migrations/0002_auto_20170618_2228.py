# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-18 22:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('operation', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usermessage',
            old_name='uesr',
            new_name='user',
        ),
    ]