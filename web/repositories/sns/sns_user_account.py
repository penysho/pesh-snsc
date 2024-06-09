from abc import ABC, abstractmethod

from django.db.models.manager import BaseManager

from web.models import Sns, SnsUserAccount


class SnsUserAccountRepository(ABC):

    @abstractmethod
    def fetch_sns_user_account_by_type(self, site_id: int, type: str) -> SnsUserAccount:
        pass

    @abstractmethod
    def fetch_sns_user_accounts(self, site_id: int) -> BaseManager[SnsUserAccount]:
        pass

    @abstractmethod
    def update_or_create_by_api_response(
        self, sns: Sns, response: dict[str, int]
    ) -> SnsUserAccount:
        pass
