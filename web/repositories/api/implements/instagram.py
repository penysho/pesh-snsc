import requests
from requests import Response

from web.dto.api import PostDto, PostMediaDto
from web.models.sns_api_account import SnsApiAccount
from web.repositories.api.api import ApiRepository


class InstagramRepositoryImpl(ApiRepository):

    def fetch_user(self, sns_api_account: SnsApiAccount) -> dict:
        return self.convert_user_dto(requests.get(self.create_fetch_user_url(sns_api_account)))

    def fetch_post(self, sns_api_account: SnsApiAccount) -> list[PostDto]:
        return self.convert_post_dto(requests.get(self.create_fetch_post_url(sns_api_account)))

    def create_fetch_user_url(self, sns_api_account: SnsApiAccount) -> str:
        return f"https://graph.facebook.com/{sns_api_account.version}/{sns_api_account.api_account_id}?fields=business_discovery.username({sns_api_account.sns.username}){{{"biography,followers_count,follows_count,media_count,name,profile_picture_url,website"}}}&access_token={sns_api_account.token}"

    def create_fetch_post_url(self, sns_api_account: SnsApiAccount) -> str:
        return f"https://graph.facebook.com/{sns_api_account.version}/{sns_api_account.api_account_id}?fields=business_discovery.username({sns_api_account.sns.username}){{{"media{caption,children{media_url,media_type},timestamp,media_product_type,media_url,media_type,permalink,comments_count,like_count}"}}}&access_token={sns_api_account.token}"

    def convert_user_dto(self, response: Response) -> dict:
        business_discovery = response.json()["business_discovery"]
        business_discovery["post_count"] = business_discovery.pop("media_count")
        del business_discovery["id"]
        return business_discovery

    def convert_post_dto(self, response: Response) -> list[PostDto]:
        posts = []
        for business_discovery in response.json()["business_discovery"]["media"]["data"]:
            post_media_dto = [
                PostMediaDto(
                    sns_url=business_discovery["media_url"],
                    type=business_discovery["media_type"],
                )
            ] if business_discovery.get("media_url") else []

            if business_discovery.get("children"):
                post_media_dto += [
                    PostMediaDto(
                        sns_url=i["media_url"],
                        type=i["media_type"],
                    ) for i in business_discovery["children"]["data"] if i.get("media_url")
                ]

            post_dto = PostDto(
                id=business_discovery["id"],
                title=business_discovery.get("title"),
                like_count=business_discovery.get("like_count"),
                comments_count=business_discovery.get("comments_count"),
                caption=business_discovery.get("caption"),
                permalink=business_discovery["permalink"],
                posted_at=business_discovery["timestamp"],
                post_media=post_media_dto,
            )
            posts.append(post_dto)
        return posts
