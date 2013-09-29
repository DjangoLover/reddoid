from django.conf.urls import patterns, include, url
from django.contrib import admin

from home.views import HomeView, PostsView, VoteView
from entities.views import LinkListView


admin.autodiscover()


urlpatterns = patterns(
    '',
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^(?P<year>\d{4})/(?P<month>[\d{1,2}]+)/(?P<day>\d{1,2})/$',
            HomeView.as_view(), name='home'),
    url(r'^posts/$', PostsView.as_view(), name='posts'),
    url(r'^links/$', LinkListView.as_view(), name='links'),
    url(r'^vote/$', VoteView.as_view(), name='vote'),
)

urlpatterns += patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns(
    '',
    url('', include('social.apps.django_app.urls', namespace='social'))
)
