# Generated by Django 2.0 on 2018-01-12 19:34

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
        ('blog', '0008_auto_20171227_1226'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', related_name='blog_tags', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Тэги'),
        ),
    ]
