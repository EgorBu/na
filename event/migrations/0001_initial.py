# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-09 11:45
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion
import event.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('image', models.ImageField(upload_to=event.models.image_path, verbose_name='Изображение')),
                ('date', models.DateTimeField(blank=True, null=True, verbose_name='Дата и время начала')),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, verbose_name='Цена')),
                ('socials', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True, verbose_name='Социальные ссылки')),
                ('published', models.BooleanField(default=True, verbose_name='Активно')),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Организатор')),
            ],
            options={
                'verbose_name': 'События',
                'verbose_name_plural': 'События',
                'ordering': ['date', 'title'],
            },
        ),
    ]
