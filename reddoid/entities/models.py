from django.db import models

from sources.models import Post


class Link(models.Model):
    url = models.URLField(null=False)
    title = models.TextField(null=True)
    score = models.IntegerField(default=0)
    date = models.DateField()
    votes_count = models.IntegerField(default=0)

    class Meta:
        ordering = ('-votes_count',)

    def __unicode__(self):
        return self.url

    def get_votes_count(self):
        return self.votes.aggregate(sum_votes=models.Sum('value'))['sum_votes'] or 0


class LinkPost(models.Model):
    link = models.ForeignKey(Link)
    post = models.ForeignKey(Post)


class Image(models.Model):
    url = models.URLField(null=False)
    title = models.TextField(null=True)
    score = models.IntegerField(default=0)
    date = models.DateField()
    votes_count = models.IntegerField(default=0)

    class Meta:
        ordering = ('-votes_count',)

    def __unicode__(self):
        return self.url

    def get_votes_count(self):
        return self.votes.aggregate(sum_votes=models.Sum('value'))['sum_votes'] or 0



class ImagePost(models.Model):
    image = models.ForeignKey(Image)
    post = models.ForeignKey(Post)
