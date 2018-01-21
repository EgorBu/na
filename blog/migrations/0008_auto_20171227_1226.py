# Generated by Django 2.0 on 2017-12-27 09:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20171102_1222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='event',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='event.Event', verbose_name='Событие'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='place',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='place.Place', verbose_name='Место'),
        ),
    ]
