from apiclient.discovery import build

from django.conf import settings

from .base import BaseSource


class GooglePlusSource(BaseSource):

    def __init__(self, uid):
        service = build('plus', 'v1')
        self.activities = service.activities()
        self.uid = uid

    def fetch(self):
        nextPageToken = None
        while True:
            activities_list = self.activities.list(
                    collection='public', userId=self.uid,
                    # TODO(nanvel): move maxResults to settings
                    pageToken=nextPageToken, maxResults=10,
                    key=settings.GOOGLE_PLUS_API_KEY).execute()
            nextPageToken = activities_list.get('nextPageToken')
            if not nextPageToken:
                raise StopIteration()
            if not len(activities_list['items']):
                raise StopIteration()
            for post in activities_list['items']:
                yield {
                    'id': post['id'],
                    'content': post['object']['content'],
                    'title': post['title'],
                    'attachments': post['object'].get('attachments', {})}
