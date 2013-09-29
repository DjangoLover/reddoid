"""
Load data from Twitter list for testing.

Note that you should have settings installed with

::
    export DJANGO_SETTINGS_MODULE=reddoid.settings.local
"""
import sys
sys.path.insert(0, "../../..")

import json

from twython import Twython
from django.conf import settings

APP_KEY = settings.SOCIAL_AUTH_TWITTER_KEY
APP_SECRET = settings.SOCIAL_AUTH_TWITTER_SECRET
twitter = Twython(
    APP_KEY,
    APP_SECRET,
    settings.TWITTER_ACCESS_TOKEN,
    settings.TWITTER_ACCESS_TOKEN_SECRET)
statuses = twitter.get_user_timeline(screen_name='dudarev_ru')
with open('factories_twitter.py', 'w') as f:
    json.dump(str(statuses), f)
with open('factories_twitter.json', 'w') as f:
    json.dump(statuses, f)
