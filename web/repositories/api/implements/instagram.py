from requests import Response
from requests.exceptions import (ConnectionError, HTTPError, RequestException,
                                 Timeout)

from web.dto.api import PostDto, PostMediaDto, SnsUserAccountDto
from web.models.sns_api_account import SnsApiAccount
from web.repositories.api.api import ApiRepository
from web.repositories.exceptions import ApiException


class InstagramRepositoryImpl(ApiRepository):

    def fetch_user(self, sns_api_account: SnsApiAccount) -> SnsUserAccountDto:
        try:
            with self._get_session() as session:
                response = session.get(self.create_fetch_user_url(sns_api_account), timeout=(10, 10))
                response.raise_for_status()
        except ConnectionError as ce:
            raise ApiException(ce)
        except HTTPError as he:
            raise ApiException(he)
        except Timeout as te:
            raise ApiException(te)
        except RequestException as re:
            raise ApiException(re)
        return self.convert_user_dto(response)

    def fetch_posts(self, sns_api_account: SnsApiAccount) -> list[PostDto]:
        try:
            with self._get_session() as session:
                response = session.get(self.create_fetch_posts_url(sns_api_account), timeout=(10, 10))
                response.raise_for_status()
        except ConnectionError as ce:
            raise ApiException(ce)
        except HTTPError as he:
            raise ApiException(he)
        except Timeout as te:
            raise ApiException(te)
        except RequestException as re:
            raise ApiException(re)
        return self.convert_posts_dto(response)

    def create_fetch_user_url(self, sns_api_account: SnsApiAccount) -> str:
        return f"https://graph.facebook.com/{sns_api_account.version}/{sns_api_account.api_account_id}?fields=business_discovery.username({sns_api_account.sns.username}){{{"biography,followers_count,follows_count,media_count,name,profile_picture_url,website"}}}&access_token={sns_api_account.token}"

    def create_fetch_posts_url(self, sns_api_account: SnsApiAccount) -> str:
        return f"https://graph.facebook.com/{sns_api_account.version}/{sns_api_account.api_account_id}?fields=business_discovery.username({sns_api_account.sns.username}){{{"media{caption,children{media_url,media_type},timestamp,media_product_type,media_url,media_type,permalink,comments_count,like_count}"}}}&access_token={sns_api_account.token}"

    def convert_user_dto(self, response: Response) -> SnsUserAccountDto:
        business_discovery = response.json()["business_discovery"]
        return SnsUserAccountDto(
            name=business_discovery.get("name"),
            biography=business_discovery.get("biography"),
            follows_count=business_discovery.get("follows_count"),
            followers_count=business_discovery.get("followers_count"),
            post_count=business_discovery.get("media_count"),
            profile_picture_url=business_discovery.get("profile_picture_url"),
            website=business_discovery.get("website"),
        )

    def convert_posts_dto(self, response: Response) -> list[PostDto]:
        posts = []
        for business_discovery in response.json()["business_discovery"]["media"]["data"]:
            post_media_dtos = [
                PostMediaDto(
                    sns_url=business_discovery["media_url"],
                    type=business_discovery["media_type"],
                )
            ] if business_discovery.get("media_url") else []

            if business_discovery.get("children"):
                post_media_dtos += [
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
                post_medias=post_media_dtos,
            )
            posts.append(post_dto)
        return posts
