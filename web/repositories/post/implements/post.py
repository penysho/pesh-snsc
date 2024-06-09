from io import BytesIO

import requests
from django.core.files import File
from django.db.models import Prefetch
from django.db.models.manager import BaseManager

from web.components.common.media import get_media_extension_by_url
from web.models import Post, PostMedia, PostProduct, Sns
from web.repositories.exceptions import DatabaseException
from web.repositories.post.post import PostRepository


class PostRepositoryImpl(PostRepository):

    def fetch_posts_by_site_id(self, site_id: int) -> BaseManager[Post]:
        try:
            return Post.objects.prefetch_related(
                Prefetch(
                    "post_medias",
                    queryset=PostMedia.objects.filter(is_active=True, list_order=0),
                    to_attr="medias",
                )
            ).filter(is_active=True, sns__site__id=site_id)
        except Exception as e:
            raise DatabaseException(e)

    def fetch_post_by_id(self, id: int) -> BaseManager[Post]:
        try:
            return Post.objects.prefetch_related(
                Prefetch(
                    "post_medias",
                    queryset=PostMedia.objects.filter(is_active=True),
                    to_attr="medias",
                ),
                Prefetch(
                    "post_products",
                    queryset=PostProduct.objects.filter(is_active=True),
                    to_attr="products",
                ),
            ).filter(is_active=True, id=id)
        except Exception as e:
            raise DatabaseException(e)

    def update_or_create_post_with_media_by_api_response(
        self, sns: Sns, response: dict[str, int]
    ) -> Post:
        try:
            post, _ = Post.objects.update_or_create(
                sns_post_id=response["id"],
                defaults={
                    "title": response.get("title"),
                    "like_count": response.get("like_count"),
                    "comments_count": response.get("comments_count"),
                    "caption": response.get("caption"),
                    "permalink": response.get("permalink"),
                },
                create_defaults={
                    "sns": sns,
                    "is_active": True,
                    "sns_post_id": response["id"],
                    "title": response.get("title"),
                    "like_count": response.get("like_count"),
                    "comments_count": response.get("comments_count"),
                    "caption": response.get("caption"),
                    "permalink": response.get("permalink"),
                    "posted_at": response["posted_at"],
                },
            )
        except Exception as e:
            raise DatabaseException(Post, e)

        try:
            sns_url = response["sns_url"]
            file = File(
                BytesIO(requests.get(sns_url).content),
                name=f"{post.id}.{get_media_extension_by_url(sns_url)}",
            )
            PostMedia.objects.update_or_create(
                post=post,
                defaults={
                    "type": response["media_type"],
                    "sns_url": sns_url,
                    "hosted_detail_url": file,
                },
                create_defaults={
                    "post": post,
                    "is_active": True,
                    "type": response["media_type"],
                    "sns_url": sns_url,
                    "hosted_detail_url": file,
                },
            )
        except Exception as e:
            raise DatabaseException(PostMedia, e)

        return post
