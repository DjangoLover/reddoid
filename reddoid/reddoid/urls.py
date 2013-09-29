from django.conf.urls import patterns, include, url
from django.contrib import admin

from home.views import HomeView, PostsView, VoteView
from entities.views import LinksHtmlView, LinksAjaxView
from sources.views import SourcesView


admin.autodiscover()


urlpatterns = patterns(
    '',
    url(r'^$', LinksHtmlView.as_view(), name='home'),
    url(r'^links/$', LinksHtmlView.as_view(), name='links'),
    url(r'^links/(?P<year>\d{4})/(?P<month>[\d{1,2}]+)/(?P<day>\d{1,2})/$',
            LinksHtmlView.as_view(), name='links'),
    url(r'^feed/$', HomeView.as_view(), name='feed'),
    url(r'^feed/(?P<year>\d{4})/(?P<month>[\d{1,2}]+)/(?P<day>\d{1,2})/$',
            HomeView.as_view(), name='feed'),
    url(r'^posts/$', PostsView.as_view(), name='posts'),
    url(r'^json/links/$', LinksAjaxView.as_view(), name='json-links'),
    url(r'^vote/$', VoteView.as_view(), name='vote'),
    url(r'^sources/$', SourcesView.as_view(), name='sources')
)

urlpatterns += patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}, name='logout')
)

urlpatterns += patterns(
    '',
    url('', include('social.apps.django_app.urls', namespace='social'))
)
