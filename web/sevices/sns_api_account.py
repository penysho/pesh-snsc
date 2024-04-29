from web.models import SnsApiAccount


class SnsApiAccountServise:
    def fetch_sns_api_account_by_site(site_id: int):
        return SnsApiAccount.objects.select_related("sns").get(
            sns__site_id=site_id, sns__type="IG", sns__is_active=True
        )
