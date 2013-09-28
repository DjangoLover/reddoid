from django.conf.urls import patterns, include, url
from django.contrib import admin


from home.views import HomeView, PostsView


admin.autodiscover()

from entities.views import LinkListView

urlpatterns = patterns(
    '',
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^posts/$', PostsView.as_view(), name='posts'),
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
