# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-06-03 14:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import epidemicanvas.models


class Migration(migrations.Migration):

    dependencies = [
        ('epidemicanvas', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contributions',
            options={'verbose_name': 'Contribution', 'verbose_name_plural': 'Contributions'},
        ),
        migrations.AddField(
            model_name='artist',
            name='email',
            field=models.EmailField(default='i.elouafiq@gmail.com', max_length=254, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contributions',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contributions',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='session',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
        migrations.AddField(
            model_name='session',
            name='updated',
            field=epidemicanvas.models.AutoDateTimeField(default=django.utils.timezone.now),
        ),
    ]
