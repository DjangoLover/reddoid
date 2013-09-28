from django.db import models

from sources.models import Post


class Link(models.Model):
    url = models.URLField(null=False)
    title = models.TextField(null=True)
    score = models.IntegerField(default=0)

    def __unicode__(self):
        return self.url


class LinkPost(models.Model):
    link = models.ForeignKey(Link)
    post = models.ForeignKey(Post)
