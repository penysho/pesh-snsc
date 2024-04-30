from django.db import models
from django.utils import timezone

from web.models.snsc_user import SnscUser


class Site(models.Model):
    id = models.BigAutoField(primary_key=True, verbose_name="サイト識別子")
    snsc_users = models.ManyToManyField(SnscUser, through="SiteOwnership")
    name = models.CharField(max_length=50, verbose_name="サイト名")
    is_active = models.BooleanField(default=False, verbose_name="使用フラグ")
    created_at = models.DateTimeField(default=timezone.now, verbose_name="登録日")
    updated_at = models.DateTimeField(default=timezone.now, verbose_name="更新日")

    class Meta:
        db_table = "site"
        verbose_name = "サイトマスタ"
        verbose_name_plural = "サイトマスタ"

    def __str__(self):
        return self.name
