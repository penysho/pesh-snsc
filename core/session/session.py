from abc import ABC, abstractmethod

from django.contrib.sessions.backends.base import SessionBase

from web.models import Site


class SnscSession(ABC):

    def __init__(self, session: SessionBase):
        self.session = session

    @abstractmethod
    def get_current_site_id(self) -> int:
        pass

    @abstractmethod
    def create_current_site(self, site: Site) -> int:
        pass
