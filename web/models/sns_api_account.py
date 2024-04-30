from django.db import models
from django.utils import timezone

from web.models.sns import Sns


class SnsApiAccount(models.Model):
    id = models.BigAutoField(
        primary_key=True, verbose_name="SNS情報取得アカウント識別子"
    )
    sns = models.ForeignKey(Sns, on_delete=models.CASCADE)
    api_account_id = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name="各SNSにおける情報取得アカウント識別子",
    )
    version = models.CharField(
        max_length=10, blank=True, null=True, verbose_name="SNS情報取得バージョン"
    )
    token = models.CharField(
        max_length=1000, blank=True, null=True, verbose_name="SNS情報取得トークン"
    )
    is_active = models.BooleanField(default=False, verbose_name="使用フラグ")
    created_at = models.DateTimeField(default=timezone.now, verbose_name="登録日")
    updated_at = models.DateTimeField(default=timezone.now, verbose_name="更新日")

    class Meta:
        db_table = "sns_api_account"
        verbose_name = "SNS情報取得アカウントマスタ"
        verbose_name_plural = "SNS情報取得アカウントマスタ"

    def __str__(self):
        return f"{self.sns}"
