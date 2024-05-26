from django.db.models.manager import BaseManager

from web.models import Post
from web.services.post_update.post_update import PostUpdateService


class PostUpdateServiceImpl(PostUpdateService):

    def __init__(self, post_repository) -> None:
        self.post_repository = post_repository

    def get_queryset(self, site_id: int) -> BaseManager[Post]:
        return self.post_repository.fetch_posts_with_media(site_id=site_id)
