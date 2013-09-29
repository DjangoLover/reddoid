import datetime

from django.test import TestCase
from django.utils import timezone

from ..templatetags.home_tags import date_link


class TemplateTagsTestCase(TestCase):

    def test_date_link(self):
        date = timezone.now()
        link = date_link(date)
        self.assertIn(str((date + datetime.timedelta(days=1)).day), link)
        link = date_link(date, is_next=False)
        self.assertIn(str((date - datetime.timedelta(days=1)).day), link)
