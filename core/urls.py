# -*- coding: utf-8 -*-
'''
fo.core.urls
'''

from django.conf.urls import url
# from django.contrib.auth.decorators import login_required

from . import views

urlpatterns = (
    url(r'^b/$',                    views.BankList.as_view(), name='bank_list'),
    url(r'^b/(?P<pk>\d+)/r/$',      views.BankDetail.as_view(), name='bank_view'),
    url(r'^o/$',                    views.OrgList.as_view(), name='org_list'),
    url(r'^o/(?P<pk>\d+)/r/$',      views.OrgDetail.as_view(), name='org_view'),
    url(r'^a/$',                    views.AgentList.as_view(), name='agent_list'),
    url(r'^a/(?P<pk>\d+)/r/$',      views.AgentDetail.as_view(), name='agent_view'),
)
