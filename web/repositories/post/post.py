from abc import ABC, abstractmethod

from django.db.models.manager import BaseManager

from web.models import Post, Sns


class PostRepository(ABC):

    @abstractmethod
    def fetch_posts_by_site_id(self, site_id: int) -> BaseManager[Post]:
        pass

    @abstractmethod
    def fetch_post_by_id(self, id: int) -> BaseManager[Post]:
        pass

    @abstractmethod
    def update_or_create_post_with_media_by_api_response(
        self, sns: Sns, response: dict[str, int]
    ) -> Post:
        pass
