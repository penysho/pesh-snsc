import json

from django import template
from django.conf import settings

register = template.Library()


@register.filter()
def is_local(request):
    return settings.DEBUG


@register.filter()
def make_dict(dict_string: str):
    return json.loads(dict_string)
