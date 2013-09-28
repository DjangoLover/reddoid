from django.conf.urls import patterns, include, url
from django.views.generic.base import TemplateView

from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns(
    'reddoid.views',
    url(r'^$', TemplateView.as_view(template_name='base.html'), name='home'),
    url(r'^load_source/$', 'load_source', name='load-source'),
)

urlpatterns += patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('',
    url('', include('social.apps.django_app.urls', namespace='social'))
)
