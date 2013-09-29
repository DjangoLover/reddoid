from datetime import datetime
from django.utils.timezone import utc

from django.core.management.base import BaseCommand
from django.utils import timezone

from entities.models import Link, LinkPost

from sources.models import Source, Post
from sources.backends import GooglePlusSource, TwitterSource


class Command(BaseCommand):
    # args = '<poll_id poll_id ...>'
    help = 'Load posts from sources'

    def handle(self, *args, **options):
        for s in Source.objects.all():
            if 'twitter' in s.url:
                screen_name = s.uid
                self.stdout.write(screen_name)
                source = TwitterSource(screen_name=screen_name)
                for tweet in source.fetch():
                    self.stdout.write(tweet['content'])
                    print tweet
                    post, is_created = Post.objects.get_or_create(
                        pid=tweet['id'],
                        created_time=datetime.strptime(
                            tweet['created_at'], '%a %b %d %H:%M:%S +0000 %Y').replace(
                                tzinfo=utc),
                        defaults={
                            'content': tweet['content'],
                            'source_id': s.id,
                            'created_time': datetime.strptime(
                                tweet['created_at'], '%a %b %d %H:%M:%S +0000 %Y').replace(
                                    tzinfo=utc)})
                    entities = tweet['entities']
                    urls = entities.get('urls', None)
                    if urls:
                        for url in urls:
                            expanded_url = url.get('expanded_url', None)
                            display_url = url.get('display_url', None)
                            if not expanded_url or not display_url:
                                continue
                            self.stdout.write(expanded_url)
                            link, is_created = Link.objects.get_or_create(
                                url=expanded_url,
                                defaults={'title': display_url})
                            LinkPost.objects.get_or_create(
                                link=link, post=post)
            elif s.uid:
                source = GooglePlusSource(uid=s.uid)
                counter = 0
                for act in source.fetch():
                    counter += 1
                    if counter > 10:
                        break
                    if not act['content'] and not act['attachments']:
                        continue
                    self.stdout.write(act['title'])
                    post, is_created = Post.objects.get_or_create(
                        pid=act['id'],
                        defaults={
                            'content': act['content'],
                            'source_id': s.id,
                            'created_time': timezone.now()})
                    entities = act['attachments']
                    if entities:
                        for ent in entities:
                            expanded_url = ent.get('url', None)
                            display_url = ent.get('content', None)
                            if not expanded_url or not display_url:
                                continue
                            self.stdout.write(expanded_url)
                            link, is_created = Link.objects.get_or_create(
                                url=expanded_url,
                                defaults={'title': display_url})
                            LinkPost.objects.get_or_create(
                                link=link, post=post)
