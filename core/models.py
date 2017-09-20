# -*- coding: utf-8 -*-
'''
PositiveSmallField: 32767 (4 digits)
PositiveIntegerField: 2147483647 (9 digits)
BigIntegerField: 9223372036854775807 (19 digits, 8 bytes)
'''

from __future__ import unicode_literals

from django.db import models


class Bank(models.Model):
    bik = models.BigIntegerField(db_index=True, verbose_name=u'БИК')
    ks = models.DecimalField(db_index=True, max_digits=20, decimal_places=0, verbose_name=u'КС')
    sname = models.CharField(unique=True, null=True, max_length=32, verbose_name=u'Краткое наименование')
    fname = models.CharField(db_index=True, max_length=254, verbose_name=u'Полное наименование')
    our = models.BooleanField(default=False, db_index=True, verbose_name='Наше')

    def _unicode_(self):
        return self.sname or self.fname

    class Meta:
        # unique_together = (('shipper', 'billno', 'billdate'),)
        db_table = 'bank'
        verbose_name = u'Банк'
        verbose_name_plural = u'Банки'
        ordering = ('sname',)


class Org(models.Model):
    inn = models.BigIntegerField(unique=True, verbose_name=u'ИНН')
    sname = models.CharField(unique=True, null=True, max_length=32, verbose_name=u'Краткое наименование')
    fname = models.CharField(db_index=True, max_length=254, verbose_name=u'Полное наименование')
    our = models.BooleanField(default=False, db_index=True, verbose_name='Наше')

    def _unicode_(self):
        return self.sname or self.fname

    class Meta:
        db_table = 'org'
        verbose_name = u'Организация'
        verbose_name_plural = u'Организации'
        ordering = ('sname',)


class Agent(models.Model):
    name = models.CharField(unique=True, max_length=32, verbose_name=u'Наименование')

    def _unicode_(self):
        return self.name

    class Meta:
        db_table = 'agent'
        verbose_name = u'Агент'
        verbose_name_plural = u'Агенты'
        ordering = ('name',)

# M2Ms

class Account(models.Model):
    org = models.ForeignKey(Org, null=True, db_index=True, verbose_name=u'Организация')
    bank = models.ForeignKey(Bank, db_index=True, verbose_name=u'Банк')
    no = models.DecimalField(unique=True, max_digits=20, decimal_places=0, db_index=True, verbose_name=u'Счет')

    def _unicode_(self):
        return '%s - %s: %d' % (self.org, self.bank, self.no)

    class Meta:
        unique_together = (('org', 'bank'),)
        db_table = 'account'
        verbose_name = u'Расчетный счет'
        verbose_name_plural = u'Расчетные счета'
        ordering = ('org', 'bank')


class OrgAgent(models.Model):
    org = models.ForeignKey(Org, db_index=True, verbose_name=u'Организация')
    agent = models.ForeignKey(Agent, db_index=True, verbose_name=u'Агент')

    def _unicode_(self):
        return '%s: %s' % (self.org, self.agent)

    class Meta:
        db_table = 'orgagent'
        verbose_name = u'Организация Агента'
        verbose_name_plural = u'Организации Агентов'
        unique_together = (('org', 'agent'),)
