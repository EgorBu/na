"""Models for Events app"""
import os
from uuid import uuid4

from ckeditor.fields import RichTextField
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from uuslug import uuslug

from event.models import Event
from place.models import Place


RUBRICS_LIST = (
    ('imho', 'Личное мнение'),
    ('festivals', 'Фестивали'),
    ('music', 'Музыка'),
)


def image_path(_instance, filename):
    """Path and name to image file."""
    file_path = os.path.join('blog_images', str(uuid4()))
    ext = filename.split('.')[-1]
    return '{}.{}'.format(file_path, ext)


class BlogManager(models.Manager):
    """Blog manager."""

    def last_published(self):
        """Last published blog."""
        result = Blog.objects.published()[:4]
        return result

    def published(self):
        """All published post."""
        result = Blog.objects.filter(published=True)
        result.order_by('rubric', 'created_at', 'title')
        return result


class Blog(models.Model):
    """Blogs model."""

    title = models.CharField(max_length=200, verbose_name='Заголовок')
    rubric = models.CharField(max_length=32, choices=RUBRICS_LIST,
                              default='imho', verbose_name='Рубрика')
    annotation = models.TextField(verbose_name='Аннотация')
    content = RichTextField(blank=True, null=True,
                            verbose_name='Содержание')
    image = models.ImageField(upload_to=image_path,
                              verbose_name='Титульное изображение')

    author = models.ForeignKey(User, verbose_name='Автор')
    event = models.ForeignKey(Event, blank=True, null=True,
                              verbose_name='Событие')
    place = models.ForeignKey(Place, blank=True, null=True,
                              verbose_name='Место')
    # tags = models.ManyToManyField(verbose_name='Тэги')
    # ratings = models.ManyToManyField(verbose_name='Рейтинг')

    published = models.BooleanField(default=False, verbose_name='Активно')
    slug = models.SlugField(max_length=200, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = BlogManager()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['created_at', 'title', 'author']
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'


class Rating(models.Model):
    blog = models.ForeignKey(Blog, verbose_name='Запись')
    user = models.ForeignKey(User, verbose_name='Пользователь')
    value = models.IntegerField(verbose_name='Оценка')


@receiver(pre_save, sender=Blog)
def created_slug(sender, instance, **_):
    """Generate custom slug before save object."""
    if instance.pk is None:
        instance.slug = uuslug(instance.title, instance=instance)
