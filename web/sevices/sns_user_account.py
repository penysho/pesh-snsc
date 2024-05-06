from django.db.models.manager import BaseManager

from web.models import SnsUserAccount
from web.models.sns import Sns


class SnsUserAccountServise:

    def __init__(self, site_id: int):
        self.site_id = site_id

    def fetch_sns_user_account_by_type(self, type: str) -> SnsUserAccount:
        return SnsUserAccount.objects.select_related("sns").get(
            is_active=True,
            sns__site_id=self.site_id,
            sns__type=type,
            sns__is_active=True,
        )

    def fetch_sns_user_accounts(self) -> BaseManager[SnsUserAccount]:
        return SnsUserAccount.objects.select_related("sns").filter(
            is_active=True, sns__site_id=self.site_id, sns__is_active=True
        )

    def update_or_create_by_response(
        self, sns: Sns, response: dict[str, int]
    ) -> tuple[SnsUserAccount, bool]:
        sns_user_account, created = SnsUserAccount.objects.update_or_create(
            sns=sns,
            defaults={**response},
            create_defaults={"sns": sns, "is_active": True, **response},
        )
        return sns_user_account, created
