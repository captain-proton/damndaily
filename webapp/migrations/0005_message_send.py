# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-25 08:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0004_auto_20170824_1230'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='send',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
