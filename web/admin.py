from django.contrib import admin
from django.contrib.auth import get_user_model

from web.models import Site, SiteOwnership

# Register your models here.

SnscUser = get_user_model()

admin.site.register(SnscUser)
admin.site.register(Site)
admin.site.register(SiteOwnership)
