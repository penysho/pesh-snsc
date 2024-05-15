from web.models import Post, SnsApiAccount, SnsUserAccount
from web.repositories.api.api import ApiRepository
from web.repositories.post.implements.post import PostRepositoryImpl
from web.repositories.sns.implements.sns import SnsRepositoryImpl
from web.repositories.sns.implements.sns_api_account import SnsApiAccountRepositoryImpl
from web.repositories.sns.implements.sns_user_account import (
    SnsUserAccountRepositoryImpl,
)
from web.services.site_register.site_register import SiteRegisterService


class SiteRegisterServiceImpl(SiteRegisterService):

    def __init__(self, site_id: str, api_repository: ApiRepository) -> None:
        self.site_id = site_id
        self.api_repository = api_repository

    def create_context_for_get(self) -> dict:
        return {
            "sns_list": SnsRepositoryImpl(self.site_id).fetch_sns_list(),
            "sns_api_accounts": SnsApiAccountRepositoryImpl(
                self.site_id
            ).fetch_sns_api_accounts(),
            "sns_user_accounts": SnsUserAccountRepositoryImpl(
                self.site_id
            ).fetch_sns_user_accounts(),
        }

    def fetch_sns_api_account(self, type: str) -> SnsApiAccount:
        return SnsApiAccountRepositoryImpl(self.site_id).fetch_sns_api_account_by_type(
            type=type
        )

    def update_or_create_sns_user_account(
        self, sns_api_account: SnsApiAccount
    ) -> tuple[SnsUserAccount, bool]:
        sns_user_account_repository = SnsUserAccountRepositoryImpl(self.site_id)
        if sns_api_account.sns.type == "IG":
            response = self.api_repository.fecth_user(sns_api_account)
            sns_user_account, created = (
                sns_user_account_repository.update_or_create_by_response(
                    sns=sns_api_account.sns, response=response
                )
            )
        return sns_user_account, created

    def update_or_create_post(self, sns_api_account: SnsApiAccount) -> list[Post]:
        post_repository = PostRepositoryImpl()
        posts = []
        if sns_api_account.sns.type == "IG":
            response = self.api_repository.fecth_media(sns_api_account)
            for media in response:
                post, _ = post_repository.update_or_create_post_by_response(
                    sns=sns_api_account.sns, response=media
                )
                post_repository.update_or_create_post_media_by_response(
                    post=post, response=media
                )
                posts.append(post)
        return posts
