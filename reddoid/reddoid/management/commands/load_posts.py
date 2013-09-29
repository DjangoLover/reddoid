from datetime import datetime
from datetime import date
from django.utils.timezone import utc

from django.core.management.base import BaseCommand
from django.utils import timezone

from entities.models import Link, LinkPost, Image, ImagePost

from sources.models import Source, Post
from sources.backends import GooglePlusSource, TwitterSource

IMAGE_LINK_STOPWORDS = ['instagram.com', 'pic.twitter.com']


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
                    post_created_at = datetime.strptime(
                        tweet['created_at'], '%a %b %d %H:%M:%S +0000 %Y').replace(
                            tzinfo=utc)
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
                    urls = entities.get('urls', [])
                    for url in urls:
                        expanded_url = url.get('expanded_url', None)
                        display_url = url.get('display_url', None)
                        if not expanded_url or not display_url:
                            continue
                        if any([w in expanded_url for w in IMAGE_LINK_STOPWORDS]):
                            print 'this is image url: ', expanded_url
                            continue
                        self.stdout.write(expanded_url)
                        link, is_created = Link.objects.get_or_create(
                            url=expanded_url,
                            date=post_created_at.date(),
                            defaults={
                            })
                        LinkPost.objects.get_or_create(
                            link=link, post=post)
                    images = entities.get('media', [])
                    for img in images:
                        if img['type'] != 'photo':
                            continue
                        expanded_url = img.get('media_url', None)
                        display_url = tweet.get('text', None)
                        if not display_url:
                            display_url = img.get('display_url', None)
                        if not expanded_url or not display_url:
                            continue
                        image, is_created = Image.objects.get_or_create(
                            url=expanded_url,
                            defaults={
                                'title': display_url,
                                'date': date.today()})
                        ImagePost.objects.get_or_create(
                            image=image, post=post)
            elif s.uid:
                source = GooglePlusSource(uid=s.uid)
                counter = 0
                for act in source.fetch():
                    counter += 1
                    if counter > 10:
                        break
                    if not act['content'] and not act['attachments']:
                        continue
                    # self.stdout.write(act['title'])
                    post, is_created = Post.objects.get_or_create(
                        pid=act['id'],
                        defaults={
                            'content': act['content'],
                            'source_id': s.id,
                            'created_time': timezone.now()})
                    entities = act['attachments']
                    for ent in entities:
                        if 'url' in ent:
                            expanded_url = ent.get('url', None)
                            display_url = act.get('title', None)
                            if expanded_url and display_url and expanded_url < 200:
                                # self.stdout.write(expanded_url)
                                link, is_created = Link.objects.get_or_create(
                                    url=expanded_url,
                                    defaults={
                                        'date': date.today()})
                                LinkPost.objects.get_or_create(
                                    link=link, post=post)
                        # imgages
                        if 'fullImage' not in ent:
                            continue
                        expanded_url = ent['fullImage'].get('url', None)
                        display_url = act.get('title', [])[:255]
                        if len(expanded_url) >= 190:
                            continue
                        if not display_url:
                            display_url = expanded_url
                        if not expanded_url or not display_url:
                            continue
                        self.stdout.write(expanded_url)
                        image, is_created = Image.objects.get_or_create(
                            url=expanded_url,
                            defaults={
                                'title': display_url,
                                'date': date.today()})
                        ImagePost.objects.get_or_create(
                            image=image, post=post)
