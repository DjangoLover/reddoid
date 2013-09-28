from django.db import models


class Source(models.Model):
    url = models.URLField(null=False)


class SourcesList(models.Model):
    url = models.URLField(null=False)

    def __unicode__(self):
        url_parts = self.url.split('/')
        if len(url_parts) > 3:
            return url_parts[-3] + '/' + url_parts[-1]
        else:
            return self.url
