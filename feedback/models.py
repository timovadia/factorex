# encoding: utf-8

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone

# Create your models here.

class Feedback(models.Model):
    email = models.EmailField(
        max_length = 80,
        unique = True,
        verbose_name = _('email')
    )

    contact_phone = models.CharField(
        max_length=16,
        verbose_name=u'Контактный телефон'
    )

    name = models.CharField(
        max_length=255,
        verbose_name=u'Ваше имя'
    )

    message = models.TextField(
        max_length=255,
        verbose_name=u'Ваше сообщение',
    )

    date_feedback = models.DateTimeField(_('Date feedback'), default=timezone.now)

    class Meta:
        verbose_name = _('Feedback')
        verbose_name_plural = _('Feedbacks')

    def __unicode__(self):
        return self.email


