import datetime

from django import template
from django.core.urlresolvers import reverse
from django.utils import timezone

register = template.Library()


@register.simple_tag
def date_link(date, is_next=True):
    if is_next:
        next_date = date + datetime.timedelta(days=1)
    else:
        next_date = date - datetime.timedelta(days=1)
    return '<a href="%s">%s</a>' % (
        reverse('home', args=(next_date.year, next_date.month, next_date.day)),
        datetime.datetime.strftime(next_date, '%Y-%m-%d'))
