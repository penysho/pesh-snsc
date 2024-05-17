from django.db.models.manager import BaseManager

from web.models import SnsApiAccount
from web.repositories.sns.sns_api_account import SnsApiAccountRepository


class SnsApiAccountRepositoryImpl(SnsApiAccountRepository):

    def fetch_sns_api_account_by_type(self, site_id: int, type: str) -> SnsApiAccount:
        return SnsApiAccount.objects.select_related("sns").get(
            is_active=True,
            sns__site_id=site_id,
            sns__type=type,
            sns__is_active=True,
        )

    def fetch_sns_api_accounts(self, site_id: int) -> BaseManager[SnsApiAccount]:
        return SnsApiAccount.objects.select_related("sns").filter(
            is_active=True, sns__site_id=site_id, sns__is_active=True
        )
