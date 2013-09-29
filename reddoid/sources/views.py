#
# -*- coding: utf-8 -*-
import datetime

from django.views.generic import ListView

from models import Source


class SourcesView(ListView):
    model = Source

    def get_context_data(self, **kwargs):
        context = super(SourcesView, self).get_context_data(**kwargs)
        context['date'] = datetime.datetime.now()
        context['entities_name'] = 'links'
        return context
