from django.db import models
from django.utils import timezone

from web.models.site import Site
from web.models.snsc_user import SnscUser


class SiteOwnership(models.Model):
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    snsc_user = models.ForeignKey(SnscUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now, verbose_name="登録日")
    updated_at = models.DateTimeField(default=timezone.now, verbose_name="更新日")

    class Meta:
        db_table = "site_ownership"
        verbose_name = "サイト所有権紐付けテーブル"
        verbose_name_plural = "サイト所有権紐付けテーブル"
