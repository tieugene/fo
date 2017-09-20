# -*- coding: utf-8 -*-
'''
fo.core.views
'''

# from django.shortcuts import render
from django.views.generic import DetailView, ListView

# import forms

import models

PAGE_SIZE = 25


class BankList(ListView):
    model = models.Bank
    template_name = 'core/bank_list.html'
    paginate_by = PAGE_SIZE


class BankDetail(DetailView):
    model = models.Bank
    template_name = 'core/bank_view.html'


class OrgList(ListView):
    model = models.Org
    template_name = 'core/org_list.html'
    paginate_by = PAGE_SIZE


class OrgDetail(DetailView):
    model = models.Org
    template_name = 'core/bank_view.html'


class AgentList(ListView):
    model = models.Agent
    template_name = 'core/agent_list.html'
    paginate_by = PAGE_SIZE


class AgentDetail(DetailView):
    model = models.Agent
    template_name = 'core/agent_view.html'
