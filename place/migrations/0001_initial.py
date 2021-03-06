# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-09 12:23
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion
import place.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('maps', models.CharField(max_length=100, verbose_name='Координаты на карте')),
                ('address', models.CharField(max_length=255, verbose_name='Адрес')),
                ('worktime', models.TextField(verbose_name='Информация о работе')),
            ],
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('image', models.ImageField(upload_to=place.models.image_path, verbose_name='Логотип')),
                ('icon', models.ImageField(upload_to=place.models.icon_path, verbose_name='Иконка')),
                ('socials', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True, verbose_name='Социальные ссылки')),
                ('published', models.BooleanField(default=False, verbose_name='Активно')),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('musicians', models.ManyToManyField(related_name='musicians', to=settings.AUTH_USER_MODEL, verbose_name='Музыканты заведения')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='manager', to=settings.AUTH_USER_MODEL, verbose_name='Владелец')),
            ],
            options={
                'verbose_name': 'Место',
                'verbose_name_plural': 'Места',
                'ordering': ['title', 'created_at'],
            },
        ),
        migrations.AddField(
            model_name='location',
            name='place',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='place.Place', verbose_name='Заведение'),
        ),
    ]
