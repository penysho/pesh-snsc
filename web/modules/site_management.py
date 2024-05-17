from injector import Binder, Module

from web.repositories.api.api import ApiRepository
from web.repositories.api.implements.instagram import InstagramRepositoryImpl
from web.repositories.api.implements.tiktok import TiktokRepositoryImpl
from web.repositories.post.implements.post import PostRepositoryImpl
from web.repositories.post.post import PostRepository
from web.repositories.sns.implements.sns import SnsRepositoryImpl
from web.repositories.sns.implements.sns_api_account import SnsApiAccountRepositoryImpl
from web.repositories.sns.implements.sns_user_account import (
    SnsUserAccountRepositoryImpl,
)
from web.repositories.sns.sns import SnsRepository
from web.repositories.sns.sns_api_account import SnsApiAccountRepository
from web.repositories.sns.sns_user_account import SnsUserAccountRepository


class SiteManagementModule(Module):

    def configure(self, binder: Binder) -> None:
        binder.bind(ApiRepository, to=InstagramRepositoryImpl)
        binder.bind(ApiRepository, to=TiktokRepositoryImpl)
        binder.bind(SnsRepository, to=SnsRepositoryImpl)
        binder.bind(SnsApiAccountRepository, to=SnsApiAccountRepositoryImpl)
        binder.bind(SnsUserAccountRepository, to=SnsUserAccountRepositoryImpl)
        binder.bind(PostRepository, to=PostRepositoryImpl)
