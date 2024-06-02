from web.models import Post
from web.services.post_update.post_update import PostUpdateService


class PostUpdateServiceImpl(PostUpdateService):

    def __init__(self, post_repository) -> None:
        self.post_repository = post_repository

    def get_queryset(self, post_id: int) -> Post:
        return self.post_repository.fetch_post_by_id(id=post_id)
