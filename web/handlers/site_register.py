import requests

from web.components.instagram.media import (
    convert_ig_get_media_for_register,
    create_ig_get_media_url,
)
from web.components.instagram.user import (
    convert_ig_get_user_for_register,
    create_ig_get_user_url,
)
from web.models.sns_api_account import SnsApiAccount
from web.sevices.post import PostService
from web.sevices.post_media import PostMediaService
from web.sevices.sns_user_account import SnsUserAccountServise


class SiteRegisterHandler:

    def __init__(self, site_id: int):
        self.site_id = site_id

    def update_or_create_sns_user_account(self, sns_api_account: SnsApiAccount):
        service = SnsUserAccountServise(self.site_id)
        if sns_api_account.sns.type == "IG":
            response = convert_ig_get_user_for_register(
                requests.get(create_ig_get_user_url(sns_api_account))
            )

        sns_user_account, created = service.update_or_create_by_response(
            sns=sns_api_account.sns,
            response=response,
        )
        return sns_user_account, created

    def update_or_create_post(self, sns_api_account: SnsApiAccount):
        post_service = PostService()
        post_media_service = PostMediaService()
        if sns_api_account.sns.type == "IG":
            response = convert_ig_get_media_for_register(
                requests.get(create_ig_get_media_url(sns_api_account))
            )
            for media in response:
                post, _ = post_service.update_or_create_by_response(
                    sns=sns_api_account.sns, response=media
                )
                post_media, _ = post_media_service.update_or_create_by_response(
                    post=post, response=media
                )
