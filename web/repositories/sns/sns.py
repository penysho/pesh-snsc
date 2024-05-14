from abc import ABC, abstractmethod

from django.db.models.manager import BaseManager

from web.models import Sns


class SnsRepository(ABC):

    @abstractmethod
    def fetch_sns_by_type(self, type: str) -> Sns:
        pass

    @abstractmethod
    def fetch_sns_list(self) -> BaseManager:
        pass
