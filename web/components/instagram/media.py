from requests import Response

from web.models import SnsApiAccount


def create_ig_get_media_url(sns_api_account: SnsApiAccount):
    return f"https://graph.facebook.com/{sns_api_account.version}/{sns_api_account.api_account_id}?fields=business_discovery.username({sns_api_account.sns.username}){{{"media{caption,children,timestamp,media_product_type,media_url,media_type,permalink,comments_count,like_count}"}}}&access_token={sns_api_account.token}"


def convert_ig_get_media_for_register(response: Response):
    posts = []
    for business_discovery in response.json()["business_discovery"]["media"]["data"]:
        business_discovery["posted_at"] = business_discovery.pop("timestamp")
        business_discovery["sns_url"] = business_discovery.pop("media_url")
        del business_discovery["media_product_type"]
        posts.append(business_discovery)
    return posts
