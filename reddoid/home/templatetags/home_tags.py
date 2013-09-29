import datetime

from django import template
from django.core.urlresolvers import reverse

register = template.Library()


@register.simple_tag
def date_link(date, entities_name='links', is_next=True):
    if not entities_name:
        entities_name = 'links'
    if is_next:
        next_date = date + datetime.timedelta(days=1)
    else:
        next_date = date - datetime.timedelta(days=1)
    return '<a href="%s">%s</a>' % (
        reverse(entities_name, args=(next_date.year, next_date.month, next_date.day)),
        ('&lt; ' if not is_next else '') + datetime.datetime.strftime(next_date, '%Y-%m-%d') + (' &gt;' if is_next else ''))
