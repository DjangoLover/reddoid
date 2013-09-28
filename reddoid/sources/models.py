import re

from django.db import models


SOURCE_REGEXPS = [
    re.compile('.+/(\d{21})/.+'),
    re.compile('https://twitter.com/(\w+)'),
]


class Source(models.Model):
    url = models.URLField(null=False)

    @property
    def uid(self):
        """
        Get user id from url
        """
        for r in SOURCE_REGEXPS:
            result = r.match(self.url)
            if result:
                return result.group(1)


class SourcesList(models.Model):
    url = models.URLField(null=False)

    def __unicode__(self):
        url_parts = self.url.split('/')
        if len(url_parts) > 3:
            return url_parts[-3] + '/' + url_parts[-1]
        else:
            return self.url


class Post(models.Model):
    # pid is for post id, taken from the service
    pid = models.CharField(primary_key=True, max_length=120)
    source = models.ForeignKey(Source)
    created_time = models.DateTimeField(null=True)
    content = models.TextField()
    api_content = models.TextField()

    def __unicode__(self):
        return "Post from {}".format(self.source.url)
