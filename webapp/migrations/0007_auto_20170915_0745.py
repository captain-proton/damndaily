# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-15 07:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0006_generatedusername'),
    ]

    operations = [
        migrations.AlterField(
            model_name='generatedusername',
            name='username',
            field=models.CharField(max_length=128, unique=True),
        ),
    ]
