from django.db.models.manager import BaseManager
from requests import Response

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

    def convert_ig_response_for_register(self, response: Response):
        business_discovery = response.json()["business_discovery"]
        business_discovery["post_count"] = business_discovery.pop("media_count")
        del business_discovery["id"]
        return business_discovery

    def update_or_create_by_ig_response(self, sns: Sns, response: Response):
        business_discovery = self.convert_ig_response_for_register(response)
        sns_user_account, created = SnsUserAccount.objects.update_or_create(
            sns=sns,
            defaults={**business_discovery},
            create_defaults={"sns": sns, "is_active": True, **business_discovery},
        )
        return sns_user_account, created
