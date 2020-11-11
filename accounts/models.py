# encoding: utf-8

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils import timezone


# Create your models here.

class FexUserManager(BaseUserManager):
    def create_user(self, email, password = None, **kwargs):
        if not email:
            raise ValueError(_('Users must have an email address'))

        user = self.model(
            email = FexUserManager.normalize_email(email),
            **kwargs
        )

        user.set_password(password)
        user.save(using = self._db)
        return user

    def create_superuser(self, email, password, **kwargs):
        user = self.create_user(email,
            password = password,
            **kwargs
        )
        user.is_admin = True
        user.save(using = self._db)
        return user

class FexUser(AbstractBaseUser):
    email = models.EmailField(
        max_length = 80,
        unique = True,
        verbose_name = _('email'),
        help_text = _('Example: email@example.com')
    )

    is_active = models.BooleanField(
        default = True,
        verbose_name = _('is active')
    )

    is_admin = models.BooleanField(
        default = False,
        verbose_name = _('is admin')
    )

    USERNAME_FIELD = 'email'

    objects = FexUserManager()

    def get_short_name(self):
        return self.email

    def __unicode__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')

class Invite(models.Model):
    TYPE_CHOICES = (
        ('f', u'Фактор (инвестор)'),
        ('c', u'Поставщик (контрактор)'),
    )
    """
    A model which implements the invite record.
    Email field is used for sending the mail.
    """
    email = models.EmailField(
        max_length = 80,
        unique = True,
        verbose_name = _('email')
    )

    user_role = models.CharField(choices=TYPE_CHOICES, max_length=25, verbose_name=u'Кто вы?')

    contact_phone = models.CharField(
        max_length=18,
        verbose_name=u'Ваш номер телефона'
    )

    name = models.CharField(
        max_length=25,
        verbose_name=u'Ваше имя'
    )

    date_requested = models.DateTimeField(_('Date requested'), default=timezone.now)

    is_active = models.BooleanField(_('Is active'), default=True)

    class Meta:
        verbose_name = _('Invite')
        verbose_name_plural = _('Invites')

    def __unicode__(self):
        return self.email

