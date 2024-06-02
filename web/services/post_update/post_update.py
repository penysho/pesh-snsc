from abc import ABC, abstractmethod

from web.models import Post


class PostUpdateService(ABC):

    @abstractmethod
    def get_queryset(self, post_id: int) -> Post:
        pass
