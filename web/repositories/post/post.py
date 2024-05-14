from abc import ABC, abstractmethod

from web.models import Post, PostMedia, Sns


class PostRepository(ABC):

    @abstractmethod
    def update_or_create_post_by_response(
        self, sns: Sns, response: dict[str, int]
    ) -> tuple[Post, bool]:
        pass

    @abstractmethod
    def update_or_create_post_media_by_response(
        self, sns: Sns, response: dict[str, int]
    ) -> tuple[PostMedia, bool]:
        pass
