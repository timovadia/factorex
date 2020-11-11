# encoding: utf-8

from django.db import models
from accounts.models import FexUser
from django.core.exceptions import ValidationError
from customers.decorators import *

# Create your models here.

class CompanyInfo(models.Model):
    """Base class for customers models"""
    class Meta:
        abstract = True
        ordering = ["name"]

    ORG_TYPES = (
        (0, u'ОАО'),
        (1, u'ЗАО'),
        (2, u'ООО'),
        (3, u'ИП'),
    )

    inn = models.CharField(max_length=12, unique=True,
                           verbose_name=u'ИНН',
                           help_text=u'10 цифр для юр. лица или 12 цифр для ИП')
    org_type = models.IntegerField(
        choices=ORG_TYPES,
        verbose_name=u'Организационно-правовая форма'
    )
    name = models.CharField(
        max_length=255, unique=True,
        verbose_name=u'Полное наименование организации',
    )
    city = models.CharField(max_length=255,
                            verbose_name=u'Город')

    contact_person_name = models.CharField(
        max_length=255,
        verbose_name=u'ФИО контактного лица'
    )
    position_person = models.CharField(
        max_length=255,
        verbose_name=u'Должность контактного лица'
    )
    contact_phone = models.CharField(
        max_length=16,
        verbose_name=u'Контактный телефон'
    )
    contact_email = models.EmailField(verbose_name=u'Адрес электронной почты')

    title = models.TextField(
        max_length=255,
        verbose_name=u'Краткое описание вашей компании',
    )

    def __unicode__(self):
        return self.name

class Factor(CompanyInfo):
    class Meta:
        verbose_name = u'Фактор'
        verbose_name_plural = u'Факторы'

    OCCUPATION_CHOICES = (
        (0, u'Банк'),
        (1, u'Факторинговая компания'),
        (100, u'Инвестор'),
    )
    occupation = models.IntegerField(
        choices=OCCUPATION_CHOICES,
        verbose_name=u'Вид деятельности'
    )

class Contractor(CompanyInfo):
    class Meta:
        verbose_name = u'Контрактор'
        verbose_name_plural = u'Контракторы'

    OCCUPATION_CHOICES = (
        (0, u'Производство'),
        (1, u'Розничная торговля'),
        (2, u'Оптовая торговля'),
        (3, u'Сфера услуг'),
        (4, u'Строительство'),
        (5, u'Грузоперевозки'),
        (100, u'Другое'),
    )
    occupation = models.IntegerField(
        choices=OCCUPATION_CHOICES,
        verbose_name=u'Вид деятельности'
    )

class Buyer(models.Model):
    class Meta:
       verbose_name = u'Дебитор'
       verbose_name_plural = u'Дебиторы'
       ordering = ["name"]

    name = models.CharField(max_length=30)
    inn = models.CharField(max_length=10, unique=True, verbose_name=u'ИНН', help_text=u'Десять цифр')
    contractor = models.ManyToManyField(Contractor)

    def __unicode__(self):
       return self.name

class FactorUser(models.Model):
    user = models.OneToOneField(FexUser, related_name='factor_user')
    employer = models.ForeignKey(Factor, related_name='employees', null=True,
                                 blank=True)

    def __unicode__(self):
        return u'{}: {}'.format(self.employer, self.user)

class ContractorUser(models.Model):
    user = models.OneToOneField(FexUser, related_name='contractor_user')
    employer = models.ForeignKey(Contractor, related_name='employees', null=True,
                                 blank=True)

    def __unicode__(self):
        return u'{}: {}'.format(self.employer, self.user)


