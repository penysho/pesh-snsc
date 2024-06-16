from injector import inject, noninjectable

from web.factories.api.api import ApiFactory
from web.models import Post, SnsApiAccount, SnsUserAccount
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
        api_repository_factory: ApiFactory,
        sns_repository: SnsRepository,
        sns_api_account_repository: SnsApiAccountRepository,
        sns_user_account_repository: SnsUserAccountRepository,
        post_repository: PostRepository,
    ) -> None:
        self.site_id = site_id
        self.api_repository_factory = api_repository_factory
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
    ) -> SnsUserAccount:
        api_repository = self.api_repository_factory.get_repository_by_sns_api_account(
            sns_api_account
        )
        return self.sns_user_account_repository.update_or_create(
            sns=sns_api_account.sns,
            sns_user_account_dto=api_repository.fetch_user(sns_api_account),
        )

    def update_or_create_posts(self, sns_api_account: SnsApiAccount) -> list[Post]:
        api_repository = self.api_repository_factory.get_repository_by_sns_api_account(
            sns_api_account
        )
        posts = [
            self.post_repository.update_or_create_post_with_medias(
                sns=sns_api_account.sns, post_dto=i
            )
            for i in api_repository.fetch_posts(sns_api_account)
            if i.post_media  # NOTE:投稿メディアが取得できない場合はは投稿の登録を行わない
        ]
        return posts
