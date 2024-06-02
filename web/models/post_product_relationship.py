from django.db import models

from web.models import Post, PostProduct
from web.models.snsc_base_model import SnscBaseModel


class PostProductRelationship(SnscBaseModel):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    post_product = models.ForeignKey(PostProduct, on_delete=models.CASCADE)

    class Meta:
        db_table = "post_product_relationship"
        verbose_name = "投稿関連商品紐付けテーブル"
        verbose_name_plural = "投稿関連商品紐付けテーブル"
