Twitter
----------

https://dev.twitter.com/apps/new

http://127.0.0.1/login/twitter

Copy `twitter.sample.py` to `twitter.py`. Add your credentials.

:: 

    
    {% url "social:begin" "twitter" %}

if using 

::

    urlpatterns += patterns('',
        url('', include('social.apps.django_app.urls', namespace='social'))
    )
