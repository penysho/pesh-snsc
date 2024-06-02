from django.db import models

from web.models import Post
from web.models.snsc_base_model import SnscBaseModel


class PostMedia(SnscBaseModel):
    id = models.BigAutoField(primary_key=True, verbose_name="投稿メディア識別子")
    # https://docs.djangoproject.com/en/5.0/ref/models/fields/#django.db.models.ForeignKey.related_name
    # https://docs.djangoproject.com/en/5.0/topics/db/queries/#backwards-related-objects
    # related_nameに逆参照時に指定するモデル名を設定
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="post_media")
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
    list_order = models.PositiveSmallIntegerField(
        default=0, verbose_name="一覧表示する際の優先度"
    )

    class Meta:
        db_table = "post_media"
        verbose_name = "投稿メディアマスタ"
        verbose_name_plural = "投稿メディアマスタ"

        constraints = [
            models.UniqueConstraint(
                fields=["post", "list_order"], name=f"uq_{db_table}_list_order"
            ),
        ]
