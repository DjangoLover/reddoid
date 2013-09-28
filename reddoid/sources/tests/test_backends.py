from django.test import TestCase

from ..backends import GooglePlusSource


class GooglePlusBackendTestCase(TestCase):

    def test_google_source(self):
        source = GooglePlusSource(uid='108114175145093679567')
        for s in source.fetch():
            print s
