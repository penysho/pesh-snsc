from django.db import models

from web.models.sns import Sns
from web.models.snsc_base_model import SnscBaseModel


class Post(SnscBaseModel):

    class Status(models.TextChoices):
        PRE_APPROVAL = "PRE", "未承認"
        APPROVED = "APR", "承認"
        REJECTED = "REJ", "却下"
        DELETED = "DEL", "削除"
        PENDING = "PND", "保留"
        PUBLISHED = "PUB", "公開"
        UNPUBLISHED = "UNP", "非公開"
        ARCHIVED = "ARC", "アーカイブ"

    id = models.BigAutoField(primary_key=True, verbose_name="投稿識別子")
    sns = models.ForeignKey(
        Sns,
        on_delete=models.PROTECT,
    )
    sns_post_id = models.CharField(
        max_length=50, verbose_name="各SNSにおける投稿識別子"
    )
    title = models.CharField(max_length=50, blank=True, verbose_name="投稿タイトル")
    like_count = models.PositiveIntegerField(verbose_name="投稿いいね数")
    comments_count = models.PositiveIntegerField(verbose_name="投稿コメント数")
    status = models.CharField(
        max_length=10,
        choices=Status.choices,
        default=Status.PRE_APPROVAL,
        verbose_name="投稿ステータス",
    )
    caption = models.TextField(blank=True, verbose_name="投稿詳細文")
    permalink = models.URLField(max_length=500, verbose_name="投稿リンク")
    posted_at = models.DateTimeField(verbose_name="投稿日")

    class Meta:
        db_table = "post"
        verbose_name = "投稿マスタ"
        verbose_name_plural = "投稿マスタ"

    def __str__(self):
        return self.sns_post_id
