# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-01-10 00:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0002_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='note',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
