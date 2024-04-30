from django.db import models
from django.utils import timezone

from web.models.site import Site


class Sns(models.Model):
    class SnsType(models.TextChoices):
        INSTAGRAM = "IG", "Instagram"
        TIKTOK = "TK", "TikTok"

    id = models.BigAutoField(primary_key=True, verbose_name="SNS識別子")
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    type = models.CharField(max_length=10, choices=SnsType, verbose_name="SNS種別")
    username = models.CharField(
        max_length=50,
        verbose_name="各SNSユーザーアカウントにおける識別子",
    )
    is_active = models.BooleanField(default=False, verbose_name="使用フラグ")
    created_at = models.DateTimeField(default=timezone.now, verbose_name="登録日")
    updated_at = models.DateTimeField(default=timezone.now, verbose_name="更新日")

    class Meta:
        db_table = "sns"
        verbose_name = "SNSサイト管理用マスタ"
        verbose_name_plural = "SNSサイト管理用マスタ"

    def __str__(self):
        return f"{self.type}-{self.site}"
