from django.db import models
from django.utils import timezone


class SnscBaseModel(models.Model):
    is_active = models.BooleanField(default=False, verbose_name="使用フラグ")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="登録日")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="更新日")

    class Meta:
        abstract = True
