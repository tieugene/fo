# -*- coding: utf-8 -*-

from django.contrib import admin

import models


# 1. inlines
class AccountInLine(admin.TabularInline):
    model = models.Account
    extra = 1
    fields = ('org', 'bank', 'no')


class OrgAgentInLine(admin.TabularInline):
    model = models.OrgAgent
    extra = 1
    fields = ('name',)


# 2. odmins
class BankAdmin(admin.ModelAdmin):
    ordering = ('sname', 'fname')
    # list_display = ('id', 'name', 'size', 'md5')
    # exclude = ('name', 'size', 'md5', 'mime')
    inlines = (AccountInLine,)


class OrgAdmin(admin.ModelAdmin):
    ordering = ('sname', 'fname')
    inlines = (AccountInLine, OrgAgentInLine)


class AgentAdmin(admin.ModelAdmin):
    # list_display = ('id', 'inn', 'name', 'fullname')
    ordering = ('name',)
    inlines = (OrgAgentInLine)


admin.site.register(models.Bank,    BankAdmin)
admin.site.register(models.Org,     OrgAdmin)
admin.site.register(models.Agent,   AgentAdmin)
