Google plus API
===============

.. code-block:: bash

    pip install --upgrade google-api-python-client

`Google python api <https://developers.google.com/api-client-library/python/start/get_started>`__

Google +api activation:
https://code.google.com/apis/console/#project:981839348215:services

https://developers.google.com/console/help/#WhatIsKey :
> An API key is a unique key that you generate using the Console. When your application needs to call an API that's enabled in this project, the application passes this key into all API requests as a key=API_key parameter. Use of this key does not require any user action or consent, does not grant access to any account information, and is not used for authorization.


Generating an api key:
https://code.google.com/apis/console/#project:981839348215:access


API usage examples:
http://code.google.com/p/google-api-python-client/wiki/SampleApps#Google+_API
http://code.google.com/p/google-api-python-client/source/browse/samples/django_sample/plus/views.py

Google+ api description:
https://developers.google.com/resources/api-libraries/documentation/plus/v1/python/latest/

API response:
def main():
    url = 'https://www.googleapis.com/plus/v1/people/101474655262166054110/'
    service = build('plus', 'v1')
    # print service.people().get(userId='101474655262166054110', key=API_KEY).execute()
    activities = service.activities()
    activities_list = activities.list(collection='public', userId='108114175145093679567', key=API_KEY).execute()
    for act in activities_list['items'][0]:
        print '>>>', act, activities_list['items'][0][act]

>>> kind plus#activity
>>> provider {u'title': u'Community'}
>>> title Линкдамп после сегодняшней тусовки (добавляйте, если что забыл):

https://github.com/troolee/cncdonetsk...
>>> url https://plus.google.com/108114175145093679567/posts/HuehnNYPtnk
>>> object {u'resharers': {u'totalItems': 0, u'selfLink': u'https://www.googleapis.com/plus/v1/activities/z134xpcautrpix2n523ygdv4gz2hhlcew/people/resharers'}, u'attachments': [{u'url': u'https://github.com/troolee/cncdonetsk/blob/gh-pages/_posts/2013-09-21-vagrant-chef-devops-hadoop-douhack.textile', u'image': {u'url': u'https://lh6.googleusercontent.com/proxy/HXa3YsniUc8vczq91QirQ0Ch4CYBa8mzbdwgvIYvtf-1XwqCPcJT44eYaXWKF9RgCTG5ZDCBqme3-zmj0qTQ6Utq_7A2J3lhTFbicYTK_DMUbElyDMsFJtoa=w120-h120', u'width': 120, u'type': u'image/jpeg', u'height': 120}, u'fullImage': {u'url': u'https://github.global.ssl.fastly.net/images/modules/logos_page/Octocat.png', u'type': u'image/jpeg'}, u'displayName': u'cncdonetsk', u'objectType': u'article'}], u'url': u'https://plus.google.com/108114175145093679567/posts/HuehnNYPtnk', u'content': u'\u041b\u0438\u043d\u043a\u0434\u0430\u043c\u043f \u043f\u043e\u0441\u043b\u0435 \u0441\u0435\u0433\u043e\u0434\u043d\u044f\u0448\u043d\u0435\u0439 \u0442\u0443\u0441\u043e\u0432\u043a\u0438 (\u0434\u043e\u0431\u0430\u0432\u043b\u044f\u0439\u0442\u0435, \u0435\u0441\u043b\u0438 \u0447\u0442\u043e \u0437\u0430\u0431\u044b\u043b):<br /><br /><a href="https://github.com/troolee/cncdonetsk/blob/gh-pages/_posts/2013-09-21-vagrant-chef-devops-hadoop-douhack.textile" class="ot-anchor" rel="nofollow">https://github.com/troolee/cncdonetsk/blob/gh-pages/_posts/2013-09-21-vagrant-chef-devops-hadoop-douhack.textile</a>', u'plusoners': {u'totalItems': 0, u'selfLink': u'https://www.googleapis.com/plus/v1/activities/z134xpcautrpix2n523ygdv4gz2hhlcew/people/plusoners'}, u'replies': {u'totalItems': 0, u'selfLink': u'https://www.googleapis.com/plus/v1/activities/z134xpcautrpix2n523ygdv4gz2hhlcew/comments'}, u'objectType': u'note'}
>>> updated 2013-09-21T17:27:51.063Z
>>> actor {u'url': u'https://plus.google.com/108114175145093679567', u'image': {u'url': u'https://lh4.googleusercontent.com/--jrbMBc2DBs/AAAAAAAAAAI/AAAAAAAAC2E/le0QX-d_1yQ/photo.jpg?sz=50'}, u'displayName': u'Artem Dudarev', u'id': u'108114175145093679567'}
>>> access {u'items': [{u'type': u'public'}], u'kind': u'plus#acl', u'description': u'Coffee&code Donetsk (\u041e\u0431\u0449\u0435\u0435)'}
>>> verb post
>>> etag "FS8hSDZUt39rsvp2gH0cFIHdkm8/PahGh4RPWYbLm-Z-BZMqMy13Pww"
>>> published 2013-09-21T17:27:51.063Z
>>> id z134xpcautrpix2n523ygdv4gz2hhlcew
