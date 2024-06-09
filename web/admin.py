from django.contrib import admin
from django.contrib.auth import get_user_model

from web.models import (
    Post,
    PostMedia,
    PostProduct,
    PostProductRelationship,
    Site,
    SiteOwnership,
    Sns,
    SnsApiAccount,
    SnsUserAccount,
)

# Register your models here.

SnscUser = get_user_model()

admin.site.register(SnscUser)
admin.site.register(Site)
admin.site.register(SiteOwnership)
admin.site.register(Sns)
admin.site.register(SnsApiAccount)
admin.site.register(SnsUserAccount)
admin.site.register(Post)
admin.site.register(PostMedia)
admin.site.register(PostProduct)
admin.site.register(PostProductRelationship)
