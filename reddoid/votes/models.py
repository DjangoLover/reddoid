from django.db import models

from django.contrib.auth.models import User

from entities.models import Image, Link


class ImageVote(models.Model):

    image = models.ForeignKey(Image, related_name='votes')
    user = models.ForeignKey(User, related_name='image_votes')
    value = models.SmallIntegerField()

    class Meta:
        unique_together = ('image', 'user')


class LinkVote(models.Model):

    link = models.ForeignKey(Link, related_name='votes')
    user = models.ForeignKey(User, related_name='link_votes')
    value = models.SmallIntegerField()

    class Meta:
        unique_together = ('link', 'user')
