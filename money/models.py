# -*- coding: utf-8 -*-
'''
fo.money.views
'''

from __future__ import unicode_literals

from core.models import Account, Client

from django.db import models


class PayType(models.Model):
    id = models.PositiveSmallIntegerField(primary_key=True, verbose_name=u'id')
    sname = models.CharField(unique=True, max_length=16, verbose_name=u'Краткое наименование')
    fname = models.CharField(unique=True, max_length=254, verbose_name=u'Полное наименование')

    def _unicode_(self):
        return self.sname

    class Meta:
        db_table = 'paytype'
        verbose_name = u'Тип платежа'
        verbose_name_plural = u'Типы платежей'
        ordering = ('sname',)


class DocType(models.Model):
    sname = models.CharField(unique=True, max_length=16, verbose_name=u'Краткое наименование')
    fname = models.CharField(unique=True, max_length=254, verbose_name=u'Полное наименование')

    def _unicode_(self):
        return self.sname

    class Meta:
        db_table = 'doctype'
        verbose_name = u'Тип документа'
        verbose_name_plural = u'Типы документов'
        ordering = ('sname',)


class Payment(models.Model):
    date = models.DateField(db_index=True, verbose_name=u'Дата')
    our = models.ForeignKey(Account, db_index=True, related_name='pays_our', verbose_name=u'Наши')
    their = models.ForeignKey(Account, db_index=True, related_name='pays_their', verbose_name=u'Ваши')
    doctype = models.ForeignKey(DocType, db_index=True, verbose_name=u'Тип документа')
    docno = models.CharField(max_length=32, db_index=True, verbose_name=u'№ документа')
    sum = models.DecimalField(max_digits=12, decimal_places=2, db_index=True, verbose_name=u'Сумма')
    purpose = models.TextField(verbose_name=u'Назначение платежа')
    type = models.ForeignKey(PayType, db_index=True, verbose_name=u'Тип платежа')
    client = models.ForeignKey(Client, null=True, db_index=True, verbose_name=u'Клиент')

    def _unicode_(self):
        return '%s %s - %s: %s #%s = %d' % (self.date, self.our, self.their, self.doctype.sname, self.docno, self.sum)

    class Meta:
        db_table = 'payment'
        verbose_name = u'Строка выписки'
        verbose_name_plural = u'Строки выписки'
        ordering = ('date', 'our', 'their', 'doctype', 'docno')
        unique_together = (('date', 'our', 'their', 'doctype', 'docno'),)


class Cash(models.Model):
    date = models.DateField(db_index=True, verbose_name=u'Дата')
    client = models.ForeignKey(Client, db_index=True, verbose_name=u'Клиент')
    sum = models.DecimalField(max_digits=12, decimal_places=2, db_index=True, verbose_name=u'Сумма')
    purpose = models.TextField(verbose_name=u'Назначение платежа')
    done = models.BooleanField(default=False, verbose_name=u'Сделано')

    def _unicode_(self):
        return '%s %s = %d' % (self.date, self.client, self.sum)

    class Meta:
        db_table = 'cash'
        verbose_name = u'Касса'
        verbose_name_plural = u'Касса'
        ordering = ('date', 'client',)
        unique_together = (('date', 'client', 'sum',),)
