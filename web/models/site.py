from django.db import models

from web.models.snsc_base_model import SnscBaseModel
from web.models.snsc_user import SnscUser


class Site(SnscBaseModel):
    id = models.BigAutoField(primary_key=True, verbose_name="サイト識別子")
    snsc_users = models.ManyToManyField(SnscUser, through="SiteOwnership")
    name = models.CharField(max_length=50, verbose_name="サイト名")

    class Meta:
        db_table = "site"
        verbose_name = "サイトマスタ"
        verbose_name_plural = "サイトマスタ"

    def __str__(self):
        return self.name
