"""Message app"""
import os
from uuid import uuid4

from ckeditor.fields import RichTextField
from django.db import models
from django.db.models import Avg
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from uuslug import uuslug


class MessageManager(models.Manager):


    def unread(self, to_user):
        """All unread messages"""
        rows = Message.objects.select_related('from_user').\
            filter(read=False, deleted=False, to_user=to_user).\
            order_by('created_at')
        result = []

        for row in rows:
            result_row = {}
            result_row['dialog_id'] = row.dialog_id
            result_row['content'] = row.content
            result_row['from_user'] = row.from_user.username
            result_row['created_at'] = row.created_at
            result.append(result_row)      

        return result


    def dialog_history(self, dialog:int, offset:int=0):
        """History of dialog"""
        limit = 20
        rows = Message.objects.\
            filter(read=True, deleted=False, dialog_id=dialog).\
            order_by('created_at')[limit*offset:limit*(offset+1)]
        result = []
        for row in rows:
            result_row = {}
            result_row['id'] = row.id
            result_row['dialog_id'] = row.dialog_id
            result_row['from_user'] = row.from_user.username
            result_row['to_user'] = row.to_user.username
            result_row['read'] = row.read
            result_row['content'] = row.content
            result_row['created_at'] = row.created_at
            result.append(result_row)      

        return result 


    def dialogs(self, user):
        """Get user dialogs"""
        rows_to_user = Message.objects.filter(to_user=user, deleted=False).order_by('created_at').reverse()[:5]
        rows_from_user = Message.objects.filter(from_user=user, deleted=False).order_by('created_at').reverse()[:5]

        result = []

        for row in rows_to_user:
            result_row = {}
            result_row['id'] = row.id
            result_row['dialog_id'] = row.dialog_id
            result_row['from_user'] = row.from_user.username
            result_row['to_user'] = row.to_user.username
            result_row['read'] = row.read
            result_row['content'] = row.content
            result_row['created_at'] = row.created_at
            result.append(result_row)    
        for row in rows_from_user:
            result_row = {}
            result_row['id'] = row.id
            result_row['dialog_id'] = row.dialog_id
            result_row['from_user'] = row.from_user.username
            result_row['to_user'] = row.to_user.username
            result_row['read'] = row.read
            result_row['content'] = row.content
            result_row['created_at'] = row.created_at
            result.append(result_row)    

        dialog_unique = list({v['dialog_id']:v for v in result}.values())

        return result


class Message(models.Model):
    """Message model."""

    content = RichTextField(blank=True, null=True,
                            verbose_name='Содержание')
    from_user = models.ForeignKey(User, on_delete=models.CASCADE,
                                  verbose_name='Отправитель',
                                  related_name='from_user')
    to_user = models.ForeignKey(User, on_delete=models.CASCADE,
                                verbose_name='Получатель',
                                related_name='to_user')
    dialog_id = models.IntegerField(default=0, verbose_name='Диалог')
    deleted = models.BooleanField(default=False, verbose_name='Удалено')
    read = models.BooleanField(default=False, verbose_name='Прочитано')
    created_at = models.DateTimeField(auto_now_add=True)

    objects = MessageManager()

    class Meta:
        ordering = ['created_at', 'from_user']
        verbose_name = 'Сообщения'
        verbose_name_plural = 'Сообщения'
        get_latest_by = 'dialog_id'