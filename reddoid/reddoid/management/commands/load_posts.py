from django.core.management.base import BaseCommand
from django.conf import settings
from django.utils.timezone import utc

from sources.models import Source, Post
from sources.backends import GooglePlusSource, TwitterSource


class Command(BaseCommand):
    # args = '<poll_id poll_id ...>'
    help = 'Load posts from sources'

    def handle(self, *args, **options):
        for s in Source.objects.all():
            if 'twitter' in s.url:
                screen_name = s.url.split('/')[-1]
                print screen_name
                source = TwitterSource(screen_name=screen_name)
                for tweet in source.fetch():
                    print tweet['content']
                    post, is_created = Post.objects.get_or_create(
                        pid=tweet['id'], content=tweet['content'], source_id=s.id)
