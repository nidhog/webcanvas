# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-06-05 11:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('epidemicanvas', '0007_auto_20170605_1048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='action',
            name='endX',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='action',
            name='endY',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='action',
            name='startX',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='action',
            name='startY',
            field=models.FloatField(default=0),
        ),
    ]
