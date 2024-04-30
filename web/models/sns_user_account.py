from django.db import models

from web.models.sns import Sns
from web.models.snsc_base_model import SnscBaseModel


class SnsUserAccount(SnscBaseModel):
    sns = models.OneToOneField(
        Sns,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    name = models.CharField(
        max_length=30, blank=True, null=True, verbose_name="SNSユーザー名(日本語対応)"
    )
    biography = models.TextField(
        blank=True, null=True, verbose_name="SNSユーザー説明文"
    )
    follows_count = models.IntegerField(
        blank=True, null=True, verbose_name="SNSユーザーフォロー数"
    )
    followers_count = models.IntegerField(
        blank=True, null=True, verbose_name="SNSユーザーフォロワー数"
    )
    post_count = models.IntegerField(
        blank=True, null=True, verbose_name="SNSユーザー投稿数"
    )
    profile_picture_url = models.URLField(
        max_length=500,
        blank=True,
        null=True,
        verbose_name="SNSユーザープロフィール画像URL",
    )
    website = models.URLField(
        max_length=500, blank=True, null=True, verbose_name="SNSユーザーウェブサイト"
    )

    class Meta:
        db_table = "sns_user_account"
        verbose_name = "SNSユーザーアカウントマスタ"
        verbose_name_plural = "SNSユーザーアカウントマスタタ"

    def __str__(self):
        return self.name
