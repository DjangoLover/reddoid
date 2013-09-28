from django.test import TestCase

from ..models import Source


class ModelsTestCase(TestCase):

    def test_source_model(self):
        TEST_DATA_SET = [
            {'url': 'https://plus.google.com/u/0/108114175145093679567/posts',
            'uid': '108114175145093679567'},
            {'url': 'https://plus.google.com/108114175145093679567/posts',
            'uid': '108114175145093679567'},
            {'url': 'https://twitter.com/polyenoom',
            'uid': 'polyenoom'},
            {'url': 'http://some/bad/url',
            'uid': None},
        ]
        for data in TEST_DATA_SET:
            source = Source(url=data['url'])
            self.assertEqual(source.uid, data['uid'])
