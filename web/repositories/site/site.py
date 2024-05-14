from abc import ABC, abstractmethod

from django.db.models.manager import BaseManager

from web.models import Site


class SiteRepository(ABC):
    @abstractmethod
    def fetch_sites(self) -> BaseManager[Site]:
        pass

    @abstractmethod
    def fetch_site_by_id(self, id: int) -> Site:
        pass

    @abstractmethod
    def fetch_site_by_name(self, name: str) -> Site:
        pass
