# -*- coding: utf-8 -*-

from django.contrib import admin

import models


# 2. odmins
class PayTypeAdmin(admin.ModelAdmin):
    ordering = ('sname',)
    # list_display = ('id', 'name', 'size', 'md5')
    # exclude = ('name', 'size', 'md5', 'mime')


class DocTypeAdmin(admin.ModelAdmin):
    ordering = ('sname',)


class PaymentAdmin(admin.ModelAdmin):
    ordering = ('date', 'our', 'their', 'doctype', 'docno')


class CashAdmin(admin.ModelAdmin):
    ordering = ('date', 'client', 'sum')


admin.site.register(models.PayType, PayTypeAdmin)
admin.site.register(models.DocType, DocTypeAdmin)
admin.site.register(models.Payment, PaymentAdmin)
admin.site.register(models.Cash,    CashAdmin)
