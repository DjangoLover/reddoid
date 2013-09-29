import factory

from django.utils import timezone

from ..models import Post, Source

from .data import GOOGLE_PLUS_TEST_FEED, TWITTER_TEST_FEED


def google_plus_feed_factory(cls):
    for post in GOOGLE_PLUS_TEST_FEED:
        yield {
            'id': post['id'],
            'content': post['object']['content']}


def twitter_feed_factory(cls):
    for post in TWITTER_TEST_FEED:
        yield {
            'id': post['id'],
            'content': post['text']}


class SourceFactory(factory.Factory):
    FACTORY_FOR = Source

    url = factory.Sequence(lambda n: 'sourceid%s' % n)


class PostFactory(factory.Factory):
    FACTORY_FOR = Post

    pid = factory.Sequence(lambda n: 'postid%s' % n)
    source = factory.SubFactory(SourceFactory)
    created_time = timezone.now()
    content = factory.Sequence(lambda n: 'Some content %s' % n)
    api_content = factory.Sequence(lambda n: 'Some api content %s' % n)
