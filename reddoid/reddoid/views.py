from twython import Twython

from django.http import HttpResponse
from django.conf import settings


def load_source(request):
    """
    Loads some source.
    """
    APP_KEY = settings.SOCIAL_AUTH_TWITTER_KEY
    APP_SECRET = settings.SOCIAL_AUTH_TWITTER_SECRET
    twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
    ACCESS_TOKEN = twitter.obtain_access_token()
    print ACCESS_TOKEN
    twitter = Twython(APP_KEY, access_token=ACCESS_TOKEN)
    statuses = twitter.get_list_statuses(slug='radon', owner_screen_name='dudarev_ru')
    print statuses
    html = "test"
    return HttpResponse(html)
