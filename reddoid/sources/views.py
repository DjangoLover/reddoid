#
# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils import decorators
from django.views.decorators import csrf
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
