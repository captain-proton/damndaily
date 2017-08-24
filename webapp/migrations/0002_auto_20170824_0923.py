# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-24 09:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='today',
            name='at',
            field=models.DateTimeField(default=django.utils.timezone.now, null=True),
        ),
        migrations.AlterField(
            model_name='today',
            name='damn_daily',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.DamnDaily'),
        ),
    ]
