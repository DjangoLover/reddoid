import urllib2

from bs4 import BeautifulSoup

from django.core.management.base import BaseCommand

from entities.models import Link


class Command(BaseCommand):
    # args = '<poll_id poll_id ...>'
    help = 'Load titles of links'

    @classmethod
    def _load_title(self, url):
        print url
        try:
            soup = BeautifulSoup(urllib2.urlopen(url))
        except:
            return url
        if not soup.title:
            return url
        else:
            return soup.title.string

    def handle(self, *args, **options):
        for l in Link.objects.all():
            if not l.title:
                title = self._load_title(l.url)
                if title:
                    l.title = title
                    l.save()
