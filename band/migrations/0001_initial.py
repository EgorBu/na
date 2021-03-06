# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-09 11:42
from __future__ import unicode_literals

import band.models
from django.conf import settings
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Band',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('image', models.ImageField(upload_to=band.models.image_path, verbose_name='Логотип')),
                ('socials', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True, verbose_name='Социальные ссылки')),
                ('published', models.BooleanField(default=True, verbose_name='Активно')),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('members', models.ManyToManyField(related_name='members', to=settings.AUTH_USER_MODEL, verbose_name='Участники')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owner', to=settings.AUTH_USER_MODEL, verbose_name='Организатор')),
            ],
            options={
                'verbose_name': 'Коллектив',
                'verbose_name_plural': 'Коллективы',
                'ordering': ['name', 'created_at'],
            },
        ),
    ]
