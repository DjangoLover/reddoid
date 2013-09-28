from mock import patch

from django.test import TestCase
from ..backends import GooglePlusSource, TwitterSource

from .factories import google_plus_feed_factory, twitter_feed_factory


class GooglePlusBackendTestCase(TestCase):

    @patch('sources.backends.google_plus.GooglePlusSource.fetch', google_plus_feed_factory)
    def test_google_source(self):
        source = GooglePlusSource(uid='108114175145093679567')
        counter = 0
        for s in source.fetch():
            counter += 1
            if counter > 5:
                break
            # Just smoke test
            self.assertTrue(s['content'])
        self.assertEqual(counter, 6)


class TweetBackendTestCase(TestCase):

    @patch('sources.backends.twitter.TwitterSource.fetch', twitter_feed_factory)
    def test_twitter_source(self):
        source = TwitterSource(uid='39025764')
        counter = 0
        for s in source.fetch():
            counter += 1
            if counter > 5:
                break
            # Just smoke test
            self.assertTrue(s['content'])
        self.assertEqual(counter, 6)
