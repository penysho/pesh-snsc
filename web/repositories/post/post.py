from abc import ABC, abstractmethod

from django.db.models.manager import BaseManager

from web.dto.api import PostDto
from web.models import Post, PostMedia, Sns


class PostRepository(ABC):

    @abstractmethod
    def fetch_posts_by_site_id(self, site_id: int) -> BaseManager[Post]:
        pass

    @abstractmethod
    def fetch_post_by_id(self, id: int) -> BaseManager[Post]:
        pass

    @abstractmethod
    def update_or_create_post_with_medias(
        self,
        sns: Sns,
        post_dto: PostDto,
    ) -> Post:
        pass

    @abstractmethod
    def update_or_create_post(self, sns: Sns, post_dto: PostDto) -> Post:
        pass

    @abstractmethod
    def update_or_create_post_medias(
        self, post: Post, post_dto: PostDto
    ) -> list[PostMedia]:
        pass
