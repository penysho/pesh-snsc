from django.db import models

from web.models import Post
from web.models.snsc_base_model import SnscBaseModel


class PostProduct(SnscBaseModel):
    id = models.BigAutoField(primary_key=True, verbose_name="投稿関連商品識別子")
    posts = models.ManyToManyField(
        Post,
        through="PostProductRelationship",
        related_name="post_products",
    )
    name = models.CharField(max_length=100, verbose_name="投稿関連商品名")
    page_url = models.URLField(max_length=1000, verbose_name="投稿関連商品ページのURL")
    image_url = models.URLField(max_length=1000, verbose_name="投稿関連商品画像のURL")
    list_order = models.PositiveSmallIntegerField(
        default=0, verbose_name="一覧表示する際の優先度"
    )

    class Meta:
        db_table = "post_product"
        verbose_name = "投稿関連商品"
        verbose_name_plural = "投稿関連商品"
