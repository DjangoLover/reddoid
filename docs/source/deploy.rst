.. reddoid project deploy

Deploy on `Heroku <https://www.heroku.com/>`__
==============================================

Clone the repository::

    git clone https://github.com/dudarev/reddoid.git
    cd reddoid

Create a new Heroku app and choose the name you'd like::

    heroku create
    heroku apps:rename newname

Set up the database (for more details see `Heroku documentation <https://devcenter.heroku.com/articles/heroku-postgresql>`__)::

    heroku addons:add heroku-postgresql:dev
    heroku pg:promote YOUR_DATABSE_URL (generated and shown during previous step)

Add necessary settings to environment variables::

    heroku config:add PYTHONPATH=/reddoid
    heroku config:add DJANGO_SETTINGS_MODULE=reddoid.settings.heroku

Set up an app at `Twitter developers page <https://dev.twitter.com/apps/new>`__.
Specify the following parameters there: 
``WEBSITE URL: http://your-app-name.herokuapp.com/`` 
and ``REDIRECT URI: http://your-app-name.herokuapp.com/social/complete/twitter``.
It's better to select "Allow this application to be used to Sign in with Twitter",
so that users do not have to confirm login every time.
Click button create access token, reload the page and get your access tokens::

    heroku config:set SOCIAL_AUTH_TWITTER_KEY=YOUR_SOCIAL_AUTH_TWITTER_KEY
    heroku config:set SOCIAL_AUTH_TWITTER_SECRET=YOUR_SOCIAL_AUTH_TWITTER_SECRET
    heroku config:set TWITTER_ACCESS_TOKEN=YOUR_TWITTER_ACCESS_TOKEN
    heroku config:set TWITTER_ACCESS_TOKEN_SECRET=YOUR_TWITTER_ACCESS_TOKEN_SECRET

Push code to heroku::

    git push heroku master

Sync the database::

    heroku run reddoid/manage.py syncdb
    heroku run reddoid/manage.py migrate

(This commands are saved in `Makefile` targets `heroku_syncdb` and `heroku_migrate`.) 
Create admin user that you will use while you are doit this.

You may now launch the application::
    
    heroku open

Navigate to `admin <http://djangistnews.herokuapp.com/admin/sources/source/>`__ and add some sources. 
The format of URLs is a what points to the person. For example, https://twitter.com/dudarev or 
https://plus.google.com/108114175145093679567/posts.

