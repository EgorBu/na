"""Models for Bands app."""
import os
from uuid import uuid4

from django.contrib.auth.models import User
from django.contrib.postgres.fields import JSONField
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from uuslug import uuslug


def image_path(_instance, filename):
    """Path and name to logo file."""
    file_path = os.path.join('band_images', str(uuid4()))
    ext = filename.split('.')[-1]
    return '{}.{}'.format(file_path, ext)


class Band(models.Model):
    """Bands model."""

    name = models.CharField(max_length=200, verbose_name='Название')
    description = models.TextField(blank=True, null=True,
                                   verbose_name='Описание')
    image = models.ImageField(upload_to=image_path, verbose_name='Логотип')

    owner = models.ForeignKey(User, related_name='owner',
                              verbose_name='Организатор')
    members = models.ManyToManyField(User, related_name='members',
                                     verbose_name='Участники')

    socials = JSONField(blank=True, null=True,
                        verbose_name='Социальные ссылки')
    # tags = models.ManyToManyField(verbose_name='Тэги')

    published = models.BooleanField(default=True, verbose_name='Активно')
    slug = models.SlugField(max_length=200, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name', 'created_at']
        verbose_name = 'Коллектив'
        verbose_name_plural = 'Коллективы'


@receiver(pre_save, sender=Band)
def created_slug(sender, instance, **_):
    """Generate custom slug before save object"""
    instance.slug = uuslug(instance.name, instance=instance)