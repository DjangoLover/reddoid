from django.http import HttpResponse
from django.views.generic.base import TemplateView, View
from django.utils import timezone, simplejson


from sources.models import Post


class AjaxView(View):

    http_method_names = ['get']
    response_class = HttpResponse

    def render_to_response(self, context, **response_kwargs):
        """
        Returns a JSON response, transforming 'context' to make the payload.
        """
        response_kwargs['content_type'] = 'application/json'
        return self.response_class(simplejson.dumps(context), **response_kwargs)


class PostsView(AjaxView):

    def get(self, request, *args, **kwargs):
        posts = Post.objects.all()
        return self.render_to_response({'posts': posts})


class HomeView(TemplateView):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        return self.render_to_response()
