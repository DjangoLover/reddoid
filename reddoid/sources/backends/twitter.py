from twython import Twython

from django.conf import settings

from .base import BaseSource


class TwitterSource(BaseSource):

    def __init__(self, uid=None, screen_name=None):
        if uid is None and screen_name is None:
            raise ValueError
        self.uid = uid
        self.screen_name = screen_name

    def fetch(self):
        APP_KEY = settings.SOCIAL_AUTH_TWITTER_KEY
        APP_SECRET = settings.SOCIAL_AUTH_TWITTER_SECRET
        twitter = Twython(
            APP_KEY,
            APP_SECRET,
            settings.TWITTER_ACCESS_TOKEN,
            settings.TWITTER_ACCESS_TOKEN_SECRET)
        if self.uid:
            tweets = twitter.get_user_timeline(user_id=self.uid)
        else:
            tweets = twitter.get_user_timeline(screen_name=self.screen_name)
        for tweet in tweets:
            yield {
                'id': tweet['id'],
                'content': tweet['text'],
                'created_at': tweet['created_at'],
                'entities': tweet['entities']
            }
