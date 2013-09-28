from apiclient.discovery import build

from django.conf import settings

from .base import BaseSource


# TODO(nanvel): move it to settings or set in ENV var



class GooglePlusSource(BaseSource):

    def __init__(self, uid):
        service = build('plus', 'v1')
        self.activities = service.activities()
        self.uid = uid

    def _links(self, content):
        return 'links %s' % content['title']

    def _pictures(self, content):
        return 'pictures %s' % content['title']

    def _videos(self, content):
        return 'images %s' % content['title'] 

    def fetch(self):
        nextPageToken = None
        while True:
            activities_list = self.activities.list(
                    collection='public', userId=self.uid,
                    # TODO(nanvel): move maxResults to settings
                    pageToken=nextPageToken, maxResults=10,
                    key=settings.GOOGLE_PLUS_API_KEY).execute()
            nextPageToken = activities_list['nextPageToken']
            for post in activities_list['items']:
                yield {
                        'links': _links(post),
                        'pictures': _picturse(post),
                        'videos': _videos(post)}
