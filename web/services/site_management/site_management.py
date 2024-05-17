from abc import ABC, abstractmethod

from web.models import Post, SnsApiAccount, SnsUserAccount


class SiteManagementService(ABC):

    @abstractmethod
    def create_context_for_get(self) -> dict:
        pass

    @abstractmethod
    def fetch_sns_api_account(self, type: str) -> SnsApiAccount:
        pass

    @abstractmethod
    def update_or_create_sns_user_account(
        self, sns_api_account: SnsApiAccount
    ) -> tuple[SnsUserAccount, bool]:
        pass

    @abstractmethod
    def update_or_create_post(self, sns_api_account: SnsApiAccount) -> list[Post]:
        pass
