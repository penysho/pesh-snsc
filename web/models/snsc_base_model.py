from django.db import models
from django.utils import timezone


class SnscBaseModel(models.Model):
    is_active = models.BooleanField(default=False, verbose_name="使用フラグ")
    created_at = models.DateTimeField(default=timezone.now, verbose_name="登録日")
    updated_at = models.DateTimeField(default=timezone.now, verbose_name="更新日")

    def save(self, *args, **kwargs):
        if not self.pk:
            self.created_at = timezone.now()
            self.updated_at = timezone.now()
        else:
            self.updated_at = timezone.now()
        super().save(*args, **kwargs)

    class Meta:
        abstract = True
