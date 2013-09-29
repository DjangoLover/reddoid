.. social services integration

Social services integration
==============================

Google+
--------------

We obtains users activities (i.e. news feeds) using Google+ API.
google-api-python-client library allows to simplify using the api in Python app.

.. code-block:: bash

    pip install --upgrade google-api-python-client

See more: `Google python api <https://developers.google.com/api-client-library/python/start/get_started>`__

Next steps are necessary to activate api for the app:

    - Google+ API activation, `see <https://code.google.com/apis/console/#project:981839348215:services>`__
    - Generating API key, see `more <https://developers.google.com/console/help/#WhatIsKey>`__ . Unique key that you generate using the Console will be enough for our purposes (navigate to Google developer Console and select API Access tab).

It is easy to understand how api can be used by seeing following examples:

    - http://code.google.com/p/google-api-python-client/wiki/SampleApps#Google+_API
    - http://code.google.com/p/google-api-python-client/source/browse/samples/django_sample/plus/views.py

Here You can find what exactly data are contained in API response:

    - https://developers.google.com/resources/api-libraries/documentation/plus/v1/python/latest/

We store GOOGLE_PLUS_API_KEY in settings/google_plus.py on development machine and in environment variable on heroku server.

Twitter
-------

Set up new app at https://dev.twitter.com/apps/new

Copy `twitter.sample.py` to `twitter.py`. Add your credentials.

Click "Create Access Token" and save them in settings too.
