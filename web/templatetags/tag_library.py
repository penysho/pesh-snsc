from django import template
from django.conf import settings

register = template.Library()


@register.filter()
def is_local(request):
    print(settings.DEBUG)
    return settings.DEBUG
