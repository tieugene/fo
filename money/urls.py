# -*- coding: utf-8 -*-
'''
fo.money.urls
'''

from django.conf.urls import url
# from django.contrib.auth.decorators import login_required

from . import views

urlpatterns = (
    url(r'^p/$',                    views.PaymentList.as_view(), name='payment_list'),
    url(r'^p/(?P<pk>\d+)/r/$',      views.PaymentDetail.as_view(), name='payment_view'),
    url(r'^c/$',                    views.CashList.as_view(), name='cash_list'),
    url(r'^c/(?P<pk>\d+)/r/$',      views.CashDetail.as_view(), name='cash_view'),
)
