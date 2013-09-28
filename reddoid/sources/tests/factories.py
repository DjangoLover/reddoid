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
