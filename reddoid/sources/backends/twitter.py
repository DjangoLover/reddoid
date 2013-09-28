from twython import Twython

from django.conf import settings

from .base import BaseSource


class TwitterSource(BaseSource):

    def __init__(self, uid):
        self.uid = uid

    def fetch(self):
        max_id = None
        while True:
            APP_KEY = settings.SOCIAL_AUTH_TWITTER_KEY
            APP_SECRET = settings.SOCIAL_AUTH_TWITTER_SECRET
            twitter = Twython(APP_KEY, APP_SECRET, settings.ACCESS_TOKEN, settings.ACCESS_TOKEN_SECRET)
            tweets = twitter.get_user_timeline(user_id=self.uid, max_id=max_id)
            max_id = tweets[-1]['id']
            if not len(tweets):
                raise StopIteration()
            for tweet in tweets:
                yield {
                    'id': tweet['id'],
                    'content': tweet['text']
                }
