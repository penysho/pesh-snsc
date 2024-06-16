from django import template
from django.conf import settings

from web.components.common.media import get_media_extension_by_url

register = template.Library()


@register.filter()
def is_local(request):
    return settings.DEBUG


@register.filter()
def is_image(media: str):
    print(media)
    return get_media_extension_by_url(media) in ["jpg", "jpeg", "png", "gif"]
