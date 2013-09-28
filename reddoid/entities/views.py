# Create your views here.
from django.utils import decorators
from django.views.decorators import csrf
from django.views.generic import ListView

from entities.models import Link
 
# https://github.com/mitar/django-missing/blob/master/missing/views.py#L7
class EnsureCsrfCookieMixin(object):
    """
    Mixin for Django class-based views which forces a view to send the CSRF cookie.
    """
    @decorators.method_decorator(csrf.ensure_csrf_cookie)
    def dispatch(self, *args, **kwargs):
        return super(EnsureCsrfCookieMixin, self).dispatch(*args, **kwargs)


class LinkListView(EnsureCsrfCookieMixin, ListView):
    model = Link 
    queryset = Link.objects.all()
    # TODO:(dudarev) move to settings
    paginate_by = 100
