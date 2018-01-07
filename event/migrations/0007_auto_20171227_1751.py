# Generated by Django 2.0 on 2017-12-27 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tag', '0001_initial'),
        ('event', '0006_auto_20171102_1222'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='tags',
            field=models.ManyToManyField(related_name='event_tags', related_query_name='event_tag', to='tag.Tag', verbose_name='Тэги'),
        ),
    ]