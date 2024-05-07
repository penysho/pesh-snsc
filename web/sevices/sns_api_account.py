from django.db.models.manager import BaseManager

from web.models import SnsApiAccount


class SnsApiAccountServise:

    def __init__(self, site_id: str):
        self.site_id = site_id

    def fetch_sns_api_account_by_type(self, type: str) -> SnsApiAccount:
        return SnsApiAccount.objects.select_related("sns").get(
            is_active=True,
            sns__site_id=self.site_id,
            sns__type=type,
            sns__is_active=True,
        )

    def fetch_sns_api_accounts(self) -> BaseManager[SnsApiAccount]:
        return SnsApiAccount.objects.select_related("sns").filter(
            is_active=True, sns__site_id=self.site_id, sns__is_active=True
        )
