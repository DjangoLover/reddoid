import datetime

from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.urlresolvers import reverse
from django.views.generic.base import TemplateView, View
from django.utils import timezone, simplejson


from sources.models import Post


class AjaxView(View):

    http_method_names = ['get']
    response_class = HttpResponse

    def render_to_response(self, context, **response_kwargs):
        response_kwargs['content_type'] = 'application/json'
        return self.response_class(simplejson.dumps(context), **response_kwargs)


class PostsView(AjaxView):

    def get(self, request, *args, **kwargs):
        page = request.GET.get('page')
        try:
            date = datetime.datetime.strptime(
                    request.GET.get('date'),
                    '%Y-%m-%d')
        except (ValueError, TypeError):
            date = datetime.datetime.now()
        paginator = Paginator(
                Post.objects.filter(
                        created_time__gte=date.replace(tzinfo=timezone.utc),
                        created_time__lt=(
                                date + datetime.timedelta(days=1)).replace(tzinfo=timezone.utc)),
                25, orphans=10)
        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            pass
        posts = [{'content': p.content} for p in posts]
        return self.render_to_response({'posts': posts})


class VoteView(AjaxView):

    http_method_names = ['post']

    def post(self, request, *args, **kwargs):
        return self.render_to_response({})


class HomeView(TemplateView):
    template_name = 'home/home.html'

    def get(self, request, *args, **kwargs):
        try:
            date = datetime.datetime(
                    year=int(kwargs['year']), month=int(kwargs['month']),
                    day=int(kwargs['day']))
        except (TypeError, ValueError, KeyError):
            date = datetime.datetime.now()
        return self.render_to_response({'date': date})
