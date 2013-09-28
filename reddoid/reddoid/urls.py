from django.conf.urls import patterns, include, url
from django.views.generic.base import TemplateView

from django.contrib import admin
admin.autodiscover()

from entities.views import LinkListView

urlpatterns = patterns(
    'reddoid.views',
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='home'),
    url(r'^load_source/$', 'load_source', name='load-source'),
)

urlpatterns += patterns(
    'entities.views',
    url(r'^links/', LinkListView.as_view(), name='links'),
)

urlpatterns += patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns(
    '',
    url('', include('social.apps.django_app.urls', namespace='social'))
)
