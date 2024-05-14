from io import BytesIO

import requests
from django.core.files import File

from web.components.common.media import get_media_extension_by_url
from web.models import Post, PostMedia, Sns
from web.repositories.post.post import PostRepository


class PostRepositoryImpl(PostRepository):
    def update_or_create_post_by_response(
        self, sns: Sns, response: dict[str, int]
    ) -> tuple[Post, bool]:
        post, created = Post.objects.update_or_create(
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
        return post, created

    def update_or_create_post_media_by_response(
        self, post: Post, response: dict[str, int]
    ) -> tuple[PostMedia, bool]:
        sns_url = response["sns_url"]
        file = File(
            BytesIO(requests.get(sns_url).content),
            name=f"{post.id}.{get_media_extension_by_url(sns_url)}",
        )
        post_media, created = PostMedia.objects.update_or_create(
            post=post.id,
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
        return post_media, created
