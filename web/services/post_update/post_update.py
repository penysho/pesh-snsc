from abc import ABC, abstractmethod

from django.db.models.manager import BaseManager

from web.models import Post


class PostUpdateService(ABC):

    @abstractmethod
    def get_queryset(self, site_id: int) -> BaseManager[Post]:
        pass
