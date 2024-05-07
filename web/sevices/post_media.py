from io import BytesIO

import requests
from django.core.files import File

from web.components.common.media import get_media_extension_by_url
from web.models import Post, PostMedia


class PostMediaService:
    def update_or_create_by_response(
        self, post: Post, response: dict[str, int]
    ) -> tuple[Post, bool]:
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
