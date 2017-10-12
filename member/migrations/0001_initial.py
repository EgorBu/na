# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-11 08:14
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion
import member.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserExtend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(upload_to=member.models.avatar_path, verbose_name='Аватар')),
                ('socials', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True, verbose_name='Социальные ссылки')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alert_comment', models.BooleanField(default=False, verbose_name='Уведомлять об ответах на комментарии')),
                ('alert_blog', models.BooleanField(default=False, verbose_name='Уведомлять о новых коментарии к постам')),
                ('alert_rating', models.BooleanField(default=False, verbose_name='Уведомлять об оценках записей')),
                ('alert_link', models.BooleanField(default=False, verbose_name='Уведомлять при прикреплении к месту или событию')),
                ('deleted', models.BooleanField(default=False, verbose_name='Пользователь удален')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]