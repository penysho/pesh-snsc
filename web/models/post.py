from django.db import models
from django.utils import timezone

from web.models.site import Site
from web.models.sns import Sns


class Post(models.Model):
    id = models.BigAutoField(primary_key=True, verbose_name="投稿識別子")
    sns = models.OneToOneField(
        Sns,
        on_delete=models.PROTECT,
        primary_key=False,
    )
    site = models.OneToOneField(
        Site,
        on_delete=models.PROTECT,
        primary_key=False,
    )
    username = models.CharField(max_length=50, verbose_name="投稿ユーザーネーム")
    title = models.CharField(
        max_length=50, blank=True, null=True, verbose_name="投稿タイトル"
    )
    like_count = models.IntegerField(blank=True, null=True, verbose_name="投稿いいね数")
    comments_count = models.IntegerField(
        blank=True, null=True, verbose_name="投稿コメント数"
    )
    caption = models.TextField(blank=True, null=True, verbose_name="投稿詳細文")
    permalink = models.URLField(max_length=500, verbose_name="投稿リンク")
    posted_at = models.DateTimeField(verbose_name="投稿日")
    is_active = models.BooleanField(default=False, verbose_name="使用フラグ")
    created_at = models.DateTimeField(default=timezone.now, verbose_name="登録日")
    updated_at = models.DateTimeField(default=timezone.now, verbose_name="更新日")

    class Meta:
        db_table = "post"
        verbose_name = "投稿マスタ"
        verbose_name_plural = "投稿マスタ"

    def __str__(self):
        return self.title
