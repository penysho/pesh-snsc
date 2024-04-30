from django.db import models

from web.models.site import Site
from web.models.snsc_base_model import SnscBaseModel
from web.models.snsc_user import SnscUser


class SiteOwnership(SnscBaseModel):
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    snsc_user = models.ForeignKey(SnscUser, on_delete=models.CASCADE)

    class Meta:
        db_table = "site_ownership"
        verbose_name = "サイト所有権紐付けテーブル"
        verbose_name_plural = "サイト所有権紐付けテーブル"
