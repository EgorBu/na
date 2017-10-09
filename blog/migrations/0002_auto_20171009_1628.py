# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-09 13:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('place', '0003_auto_20171009_1557'),
        ('event', '0001_initial'),
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='event',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='event.Event', verbose_name='Событие'),
        ),
        migrations.AddField(
            model_name='blog',
            name='place',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='place.Place', verbose_name='Место'),
        ),
    ]
