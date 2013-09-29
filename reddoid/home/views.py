import datetime

from django.http import HttpResponse, Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.urlresolvers import reverse
from django.views.generic.base import TemplateView, View
from django.utils import timezone, simplejson


from sources.models import Post
from entities.models import Link
from votes.models import LinkVote


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
        if not request.user.is_authenticated():
            raise Http404
        try:
            lv, created = LinkVote.objects.get_or_create(
                        user=request.user,
                        link=Link.objects.get(url=request.POST.get('entiti')),
                        defaults={'value': int(request.POST.get('val'))})
            lv.value = int(request.POST.get('val'))
            lv.save()
            link = lv.link
            link.votes_count = link.get_votes_count()
            link.save()
        except:
            return self.render_to_response({'success': False})
        return self.render_to_response({'success': True, 'vote': lv.link.votes_count})


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
