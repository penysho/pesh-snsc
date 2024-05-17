from injector import inject, noninjectable

from web.models import Post, SnsApiAccount, SnsUserAccount
from web.repositories.api.api import ApiRepository
from web.repositories.post.post import PostRepository
from web.repositories.sns.sns import SnsRepository
from web.repositories.sns.sns_api_account import SnsApiAccountRepository
from web.repositories.sns.sns_user_account import SnsUserAccountRepository
from web.services.site_management.site_management import SiteManagementService


class SiteManagementServiceImpl(SiteManagementService):

    @inject
    @noninjectable("site_id")
    def __init__(
        self,
        site_id: int,
        api_repository: ApiRepository,
        sns_repository: SnsRepository,
        sns_api_account_repository: SnsApiAccountRepository,
        sns_user_account_repository: SnsUserAccountRepository,
        post_repository: PostRepository,
    ) -> None:
        self.site_id = site_id
        self.api_repository = api_repository
        self.sns_repository = sns_repository
        self.sns_api_account_repository = sns_api_account_repository
        self.sns_user_account_repository = sns_user_account_repository
        self.post_repository = post_repository

    def create_context_for_get(self) -> dict:
        return {
            "sns_list": self.sns_repository.fetch_sns_list(self.site_id),
            "sns_api_accounts": self.sns_api_account_repository.fetch_sns_api_accounts(
                self.site_id
            ),
            "sns_user_accounts": self.sns_user_account_repository.fetch_sns_user_accounts(
                self.site_id
            ),
        }

    def fetch_sns_api_account(self, type: str) -> SnsApiAccount:
        return self.sns_api_account_repository.fetch_sns_api_account_by_type(
            site_id=self.site_id, type=type
        )

    def update_or_create_sns_user_account(
        self, sns_api_account: SnsApiAccount
    ) -> tuple[SnsUserAccount, bool]:
        if sns_api_account.sns.type == "IG":
            response = self.api_repository.fecth_user(sns_api_account)
            sns_user_account, created = (
                self.sns_user_account_repository.update_or_create_by_response(
                    sns=sns_api_account.sns, response=response
                )
            )
        return sns_user_account, created

    def update_or_create_post(self, sns_api_account: SnsApiAccount) -> list[Post]:
        posts = []
        if sns_api_account.sns.type == "IG":
            response = self.api_repository.fecth_media(sns_api_account)
            for media in response:
                post, _ = self.post_repository.update_or_create_post_by_response(
                    sns=sns_api_account.sns, response=media
                )
                self.post_repository.update_or_create_post_media_by_response(
                    post=post, response=media
                )
                posts.append(post)
        return posts
