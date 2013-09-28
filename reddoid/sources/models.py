from django.db import models


class Source(models.Model):
    url = models.URLField(null=False)

    def __unicode__(self):
        if 'twitter' in self.url:
            url_parts = self.url.split('/')
            if len(url_parts) > 1:
                return "twitter: " + url_parts[-1]
            else:
                return "twitter source"
        else:
            return self.url


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
