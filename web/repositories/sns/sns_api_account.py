from abc import ABC, abstractmethod

from django.db.models.manager import BaseManager

from web.models import SnsApiAccount


class SnsApiAccountRepository(ABC):

    @abstractmethod
    def fetch_sns_api_account_by_type(self, type: str) -> SnsApiAccount:
        pass

    @abstractmethod
    def fetch_sns_api_accounts(self) -> BaseManager[SnsApiAccount]:
        pass
