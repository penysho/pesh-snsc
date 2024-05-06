from web.models import Post
from web.models.sns import Sns


class PostService:
    def update_or_create_by_response(
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
