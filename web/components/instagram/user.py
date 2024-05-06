from requests import Response

from web.models import SnsApiAccount


def create_ig_get_user_url(sns_api_account: SnsApiAccount):
    return f"https://graph.facebook.com/{sns_api_account.version}/{sns_api_account.api_account_id}?fields=business_discovery.username({sns_api_account.sns.username}){{{"biography,followers_count,follows_count,media_count,name,profile_picture_url,website"}}}&access_token={sns_api_account.token}"


def convert_ig_get_user_for_register(response: Response):
    business_discovery = response.json()["business_discovery"]
    business_discovery["post_count"] = business_discovery.pop("media_count")
    del business_discovery["id"]
    return business_discovery
