from io import BytesIO

import requests
from django.core.files import File
from django.db import transaction
from django.db.models import Prefetch
from django.db.models.manager import BaseManager

from web.components.common.media import get_media_extension_by_url
from web.dto.api import PostDto
from web.models import Post, PostMedia, PostProduct, Sns
from web.repositories.exceptions import DatabaseException
from web.repositories.post.post import PostRepository


class PostRepositoryImpl(PostRepository):

    def fetch_posts_by_site_id(self, site_id: int) -> BaseManager[Post]:
        try:
            return Post.objects.prefetch_related(
                Prefetch(
                    "post_medias",
                    queryset=PostMedia.objects.filter(is_active=True),
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

    def update_or_create_post_with_medias(
        self,
        sns: Sns,
        post_dto: PostDto,
    ) -> Post:
        with transaction.atomic():
            post = self.update_or_create_post(sns=sns, post_dto=post_dto)
            self.update_or_create_post_medias(post=post, post_dto=post_dto)
            return post

    def update_or_create_post(self, sns: Sns, post_dto: PostDto) -> Post:
        try:
            post, _ = Post.objects.update_or_create(
                sns_post_id=post_dto.id,
                defaults={
                    "title": post_dto.title,
                    "like_count": post_dto.like_count,
                    "comments_count": post_dto.comments_count,
                    "caption": post_dto.caption,
                    "permalink": post_dto.permalink,
                },
                create_defaults={
                    "sns": sns,
                    "title": post_dto.title,
                    "like_count": post_dto.like_count,
                    "comments_count": post_dto.comments_count,
                    "caption": post_dto.caption,
                    "permalink": post_dto.permalink,
                    "posted_at": post_dto.posted_at,
                },
            )
            return post
        except Exception as e:
            raise DatabaseException(Post, e)

    def update_or_create_post_medias(
        self, post: Post, post_dto: PostDto
    ) -> list[PostMedia]:
        try:
            post_medias = []
            # TODO: 画像がされた場合にPostMediaの切り詰めを行う
            for i, post_media in enumerate(post_dto.post_media):
                sns_url = post_media.sns_url
                file = File(
                    BytesIO(requests.get(sns_url).content),
                    name=f"{post.id}_{i + 1}.{get_media_extension_by_url(sns_url)}",
                )
                post_media, _ = PostMedia.objects.update_or_create(
                    post=post,
                    list_order=i + 1,
                    defaults={
                        "type": post_media.type,
                        "sns_url": sns_url,
                        "hosted_detail_url": file,
                    },
                    create_defaults={
                        "type": post_media.type,
                        "sns_url": sns_url,
                        "hosted_detail_url": file,
                    },
                )
                post_medias.append(post_media)
            return post_medias
        except Exception as e:
            raise DatabaseException(PostMedia, e)
