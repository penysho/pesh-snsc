from django.db import models

from web.models.post import Post
from web.models.snsc_base_model import SnscBaseModel


class PostMedia(SnscBaseModel):
    id = models.BigAutoField(primary_key=True, verbose_name="投稿メディア識別子")
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    type = models.CharField(max_length=20, verbose_name="投稿メディアタイプ")
    sns_url = models.URLField(
        max_length=1000, blank=True, null=True, verbose_name="SNS側でホストされたURL"
    )
    hosted_list_url = models.FileField(
        upload_to="list/",
        blank=True,
        null=True,
        verbose_name="アプリケーションでホストされた一覧ページ用URL",
    )
    hosted_detail_url = models.FileField(
        upload_to="detail/",
        verbose_name="アプリケーションでホストされた詳細ページ用URL",
    )

    class Meta:
        db_table = "post_media"
        verbose_name = "投稿メディアマスタ"
        verbose_name_plural = "投稿メディアマスタ"
