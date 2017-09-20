# -*- coding: utf-8 -*-
'''
fo.money.views
'''

# from django.shortcuts import render
from django.views.generic import DetailView, ListView

import models

PAGE_SIZE = 25


class PaymentList(ListView):
    model = models.Payment
    template_name = 'money/payment_list.html'
    paginate_by = PAGE_SIZE


class PaymentDetail(DetailView):
    model = models.Payment
    template_name = 'money/payment_view.html'


class CashList(ListView):
    model = models.Cash
    template_name = 'money/cash_list.html'
    paginate_by = PAGE_SIZE


class CashDetail(DetailView):
    model = models.Cash
    template_name = 'money/cash_view.html'
