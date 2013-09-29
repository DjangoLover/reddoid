import datetime

from django.core.urlresolvers import reverse
from django.test import TestCase
from django.utils import simplejson

from sources.tests.factories import PostFactory, SourceFactory


class HomeViewsTestCase(TestCase):

    def test_home_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
                datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d'),
                datetime.datetime.strftime(response.context['date'], '%Y-%m-%d'))

    def test_posts_json(self):
        source = SourceFactory()
        source.save()
        factory = PostFactory(source=source)
        factory.save()
        response = self.client.get(reverse('posts'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
                len(simplejson.loads(response.content)['posts']),
                1)
