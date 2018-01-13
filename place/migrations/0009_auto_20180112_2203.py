# Generated by Django 2.0 on 2018-01-12 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0008_auto_20180112_2203'),
        ('place', '0007_auto_20171227_1226'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='location',
            name='place',
        ),
        migrations.AddField(
            model_name='place',
            name='address',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Адрес'),
        ),
        migrations.AddField(
            model_name='place',
            name='coordinates',
            field=models.CharField(default='', max_length=150, verbose_name='Координаты'),
        ),
        migrations.AddField(
            model_name='place',
            name='worktime',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Время работы'),
        ),
        migrations.DeleteModel(
            name='Location',
        ),
    ]
