from web.models import Post, PostMedia


class PostMediaService:
    def update_or_create_by_response(
        self, post: Post, response: dict[str, int]
    ) -> tuple[Post, bool]:
        post_media, created = PostMedia.objects.update_or_create(
            post=post.id,
            defaults={
                "type": response["media_type"],
                "sns_url": response.get("media_url"),
            },
            create_defaults={
                "post": post,
                "is_active": True,
                "type": response["media_type"],
                "sns_url": response.get("media_url"),
            },
        )
        return post_media, created
