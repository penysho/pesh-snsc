from django.db import models


class SnscBaseModel(models.Model):
    is_active = models.BooleanField(default=True, verbose_name="使用フラグ")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="登録日")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="更新日")

    class Meta:
        abstract = True
