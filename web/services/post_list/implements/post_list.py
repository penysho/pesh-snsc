from django.db.models.manager import BaseManager

from web.models import Post
from web.repositories.post.post import PostRepository
from web.services.post_list.post_list import PostListService


class PostListServiceImpl(PostListService):

    def __init__(self, post_repository: PostRepository) -> None:
        self.post_repository = post_repository

    def get_queryset(self, site_id: int) -> BaseManager[Post]:
        return self.post_repository.fetch_posts_by_site_id(site_id=site_id)
