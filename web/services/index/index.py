from abc import ABC, abstractmethod

from web.models import Site


class IndexService(ABC):

    @abstractmethod
    def change_site(self) -> Site:
        pass
