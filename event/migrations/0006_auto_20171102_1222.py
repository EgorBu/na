# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-02 09:22
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('event', '0005_auto_20171018_1539'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=250, verbose_name='Содержание')),
                ('published', models.BooleanField(default=True, verbose_name='Активно')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.Event', verbose_name='Запись')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='event_commentator', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Комментарий',
                'verbose_name_plural': 'Комментарии',
                'ordering': ['created_at', 'user'],
            },
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField(verbose_name='Оценка')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.Event', verbose_name='Запись')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='event_voted', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='rating',
            unique_together=set([('event', 'user')]),
        ),
    ]
