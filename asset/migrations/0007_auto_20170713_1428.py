# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-13 06:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asset', '0006_auto_20170713_1427'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asset',
            name='instance',
            field=models.CharField(blank=True, default='', max_length=128, null=True, verbose_name='实例ID'),
        ),
    ]
