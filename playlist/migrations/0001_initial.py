# Generated by Django 2.0 on 2018-01-20 16:20
from __future__ import unicode_literals

import playlist.models
from django.db import migrations, models
from django.conf import settings
import django.db.models.deletion

class Migration(migrations.Migration):

	initial = True

	dependencies = [
		migrations.swappable_dependency(settings.AUTH_USER_MODEL),
	]

	operations = [
		migrations.CreateModel(
			name='Playlist',
			fields=[
				('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
				('name', models.CharField(max_length=200, verbose_name='Название')),
				('annotation', models.TextField(verbose_name='Аннотация')),
				('content', models.TextField(verbose_name='Содержание')),
				('image', models.ImageField(upload_to=playlist.models.image_path, verbose_name='Титульное изображение')),
				('published', models.BooleanField(default=False, verbose_name='Активно')),
				('slug', models.SlugField(max_length=200, unique=True)),
				('created_at', models.DateTimeField(auto_now_add=True)),
				('updated_at', models.DateTimeField(auto_now=True)),
				('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Создатель')),
			],
			options={
				'verbose_name': 'Плейлист',
				'verbose_name_plural': 'Плейлисты',
				'ordering': ['created_at', 'name', 'creator'],
			},
		)
	]
