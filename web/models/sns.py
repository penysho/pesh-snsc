from django.db import models

from web.models.site import Site
from web.models.snsc_base_model import SnscBaseModel


class Sns(SnscBaseModel):
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

    class Meta:
        db_table = "sns"
        verbose_name = "SNSサイト管理用マスタ"
        verbose_name_plural = "SNSサイト管理用マスタ"

    def __str__(self):
        return f"{self.type}-{self.site}"
