#
# -*- coding: utf-8 -*-
import datetime

from django.views.generic import ListView
from django.views.generic.base import TemplateView, View
from django.utils import timezone, simplejson
from django.db.models import Count, Sum

from models import Source


class SourcesView(ListView):
    # template_name = 'list.html'
    model = Source

    def get_queryset(self):
        return Source.objects.annotate(num=Count('post')).order_by('-num')

    def get_context_data(self, **kwargs):
        context = super(SourcesView, self).get_context_data(**kwargs)
        context['date'] = datetime.datetime.now()
        context['entities_name'] = 'links'
        return context

