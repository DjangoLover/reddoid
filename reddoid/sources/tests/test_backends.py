from mock import patch

from django.test import TestCase

from ..backends import GooglePlusSource

from .factories import google_plus_feed_factory


class GooglePlusBackendTestCase(TestCase):

    @patch('sources.backends.google_plus.GooglePlusSource', google_plus_feed_factory)
    def test_google_source(self):
        source = GooglePlusSource(uid='108114175145093679567')
        counter = 0
        for s in source.fetch():
            counter += 1
            if counter > 5:
                break
            print s
