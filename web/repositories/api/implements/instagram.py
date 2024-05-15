import requests
from requests import Response

from web.models.sns_api_account import SnsApiAccount
from web.repositories.api.api import ApiRepository


class InstagramRepositoryImpl(ApiRepository):

    def fecth_user(self, sns_api_account: SnsApiAccount) -> dict:
        return self.convert_get_user_for_register(requests.get(self.create_get_user_url(sns_api_account)))

    def fecth_media(self, sns_api_account: SnsApiAccount) -> dict:
        return self.convert_get_media_for_register(requests.get(self.create_get_media_url(sns_api_account)))

    def create_get_media_url(self, sns_api_account: SnsApiAccount) -> str:
        return f"https://graph.facebook.com/{sns_api_account.version}/{sns_api_account.api_account_id}?fields=business_discovery.username({sns_api_account.sns.username}){{{"media{caption,children,timestamp,media_product_type,media_url,media_type,permalink,comments_count,like_count}"}}}&access_token={sns_api_account.token}"

    def create_get_user_url(self, sns_api_account: SnsApiAccount) -> str:
        return f"https://graph.facebook.com/{sns_api_account.version}/{sns_api_account.api_account_id}?fields=business_discovery.username({sns_api_account.sns.username}){{{"biography,followers_count,follows_count,media_count,name,profile_picture_url,website"}}}&access_token={sns_api_account.token}"

    def convert_get_media_for_register(self, response: Response) -> dict:
        posts = []
        for business_discovery in response.json()["business_discovery"]["media"]["data"]:
            business_discovery["posted_at"] = business_discovery.pop("timestamp")
            business_discovery["sns_url"] = business_discovery.pop("media_url")
            del business_discovery["media_product_type"]
            posts.append(business_discovery)
        return posts

    def convert_get_user_for_register(self, response: Response) -> dict:
        business_discovery = response.json()["business_discovery"]
        business_discovery["post_count"] = business_discovery.pop("media_count")
        del business_discovery["id"]
        return business_discovery
